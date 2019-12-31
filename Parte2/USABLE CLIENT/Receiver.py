import pika
import time
import threading
from random import choice


def auto_read():
	global ID
	global conect
	connection2=pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
	channel2=connection2.channel()
	channel2.queue_declare(queue=ID)
	channel2.queue_bind(exchange='Handler', queue=ID, routing_key=ID)
	while(conect):
		method, prop, body =channel2.basic_get(queue=ID, auto_ack=True)
		if(method!=None):
			aux=body.decode('ascii')
			aux2=aux.split('-')
			if(aux2[0]=='MSJ'):
				if(aux2[1]==ID):
					print('Received from yourself: {} {}'.format(aux2[4], aux2[5]))
				else :
					print('Received from: {}, {} {}'.format(aux2[1], aux2[4], aux2[5]))
			elif (aux2[0]=='USR'):
				print(aux2[1])
			elif (aux2[0]=='LOG'):
				while(True):
					method, prop, body =channel2.basic_get(queue=ID, auto_ack=True)
					if(method!=None):
						if(body.decode('ascii')!=str(0)):
							print(body.decode('ascii'))
						else:
							break



connection=pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel=connection.channel()
channel.basic_publish(exchange='Handler', routing_key='Request', body='REQ')
while(True):
	method, prop, body = channel.basic_get(queue='Reply', auto_ack=True)
	if(method!=None):
		ID=body.decode('ascii')
		break
threading.Thread(target=auto_read).start()

conect=True
while(conect):
	option=input("Que desea hacer? (Send/Users/Log/Exit): \n")  # '¿' literalmente hizo explotar el programa, why? no lo se, por eso use el formato gringo de interrogacion
	if(option=='Send'):
		who=input("A quien desea enviar?: ")
		msj=input("Ingrese mensaje: ")
		coso='MSJ-'+ID+'-'+str(who)+'-'+msj
		channel.basic_publish(exchange='Handler', routing_key='Request', body=coso)
	elif(option=='Users'):
		coso='USR-'
		coso+=ID
		channel.basic_publish(exchange='Handler', routing_key='Request', body=coso)
	elif(option=='Log'):
		coso='LOG-'
		coso+=ID
		channel.basic_publish(exchange='Handler', routing_key='Request', body=coso)
	elif(option=='Exit'):
		conect=False
print('Desconectado')
connection.close()

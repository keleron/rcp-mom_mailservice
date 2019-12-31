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


time.sleep(15)

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
auto=0
while(conect and auto<10):
	print('Que desea hacer? (Send/Users/Log/Exit):')
	if(auto<3):
		option=choice(['Send', 'Users'])
	else:
		option=choice(['Send', 'Users', 'Log'])
	print(option)
	auto+=1
	#option=input("¿Que desea hacer? (Send/Users/Log/Exit): \n")
	if(option=='Send'):
		#who=input("¿A quien desea enviar?: ")
		who=choice([0,1,2])
		#msj=input("Ingrese mensaje: ")
		msj=choice(['Bruh', 'Xiaomi', 'Esto no prendio', 'Fuck ascii, 2 malditas horas perdidas por tu culpa', 'A la grande le puse cuca', 'We tried'])
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
	time.sleep(3)
print('Desconectado')
connection.close()

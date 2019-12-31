import pika
import datetime
import time

ID=0
USERS=[]
MEN=0

def on_consume(ch, method, prop, body):
	global ID
	global USERS
	global MEN
	temp=body.decode('ascii')
	print(temp)
	temp=temp.split('-')
	if(temp[0]=='REQ'):
		channel.basic_publish(exchange='Handler', routing_key='Reply', body=str(ID))
		USERS.append(ID)
		ID+=1
		print(USERS)
		print(ID)
	elif (temp[0]=='MSJ'):
		day='{:%Y/%m/%d %H:%M:%S}'.format(datetime.datetime.now())
		if(int(temp[1]) in USERS):
			msg=temp[0]+'-'+temp[1]+'-'+str(MEN)+'-'+temp[2]+'-'+temp[3]+'-'+day
			logger=temp[1]+'-'+str(MEN)+'-'+temp[2]+'-'+temp[3]+'-'+day
			print(msg)
			MEN+=1
			log=open('log.txt', 'a')
			log.write(logger+'\n')
			log.close()
			channel.basic_publish(exchange='Handler', routing_key=temp[2], body=msg)

	elif (temp[0]=='USR'):
		mensaje=temp[0]+'-Clients: '
		for User in USERS:
			mensaje+=str(User)
			mensaje+=', '
		print(mensaje)
		channel.basic_publish(exchange='Handler', routing_key=temp[1], body=mensaje)
	elif (temp[0]=='LOG'):
		channel.basic_publish(exchange='Handler', routing_key=temp[1], body='LOG')
		logger=open('log.txt','r')
		for lines in logger:
			aux=lines.split('-')
			if(temp[1]==aux[0]):
				print(lines)
				channel.basic_publish(exchange='Handler', routing_key=temp[1], body=lines)
		logger.close()
		channel.basic_publish(exchange='Handler', routing_key=temp[1], body='0')






time.sleep(15)
start=open('log.txt', 'w')
connection=pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel=connection.channel()
channel.queue_declare(queue='Request')
channel.queue_declare(queue='Reply')
channel.exchange_declare(exchange='Handler', exchange_type='direct')
channel.queue_bind(exchange='Handler', queue='Request', routing_key='Request')
channel.queue_bind(exchange='Handler', queue='Reply', routing_key='Reply')
channel.basic_consume(queue='Request', on_message_callback=on_consume, auto_ack=True)
channel.start_consuming()

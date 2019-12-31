Formato de request (SERVER):


Type - FROM - TO - msg

Ej: MSJ-2-1-Queen  --> Usuario 2 le envia el mensaje "Queen" al usuario 1
	LOG-4			 --> Usuario 4 desea conocer los mensajes enviados
	USR-3			 --> Usuario 3 quiere conocer la lista de usuarios
	REQ              --> Usuario solicita que se le asigne un ID

Formato del log:

FROM - msgID -  TO - msg - STAMP

Similar al anterior, stamp es el timestamp del momento en que fue recibido por el server y el msgID es el ID unico de cada mensaje asignado segun la recepcion por el servidor

Importante:
No mandar palabra con Ñ, porque se cae, el '¿' tambien lo mata, no he probado que caracteres mas los mata, pero lo mas seguro son todos lo que no se pueden representar con ascii


Notas:

-El broker de RabbitMQ es un container por si mismo dado que para poder hacer funcionar las conexiones este debia estar iniciado con antelacion antes de la ejecucion del script en python y dado el deployment esto no sucedia en cada container, por lo mismo, los container del producer y los consumidores tienen un sleep de 15 segundos para asegurar que se inicie el broker y realizar la conexion

-Compose genera 2 clientes que estan automatizados, generan a lo mucho 10 solicitudes distintas dentro del rango de enviar mensajes, pedir el listado de usuario y el log de los mensajes enviados por ellos mismos, despues de dichas 10 solicitudes se desconectan

-En la carpeta USABLE CLIENT se encuentra la version del cliente sin automatizacion, que se puede usar para conectarse al servidor, viene con su propio dockerfile por lo que se puede generar la imagen haciendo el build respectivo y generar la cantidad de containers deseadas
	-Es importante que al momento de crear y ejecutar el container, se especifique el parametro (--net 'nombre de la red generada por el compose') que se puede obtener con 'docker network ls' de manera que pueda encontrar al container que contiene el broker de rabbitmq
	-Lo ideal es ejecutar los container una vez que el container de Rabbitmq este en funcionamiento, es probable que se demore en cargar la solicitud de input dado que debe esperar que el producer (sender) despierte para manejar la solicitud

El funcionamiento de los id:
	
	-El sender esta pendiente de la cola "Request", puede recibir 4 tipo de solicitudes como las que estan al principio, cuando recien se inicia un cliente, automaticamente realiza un REQ, de manera que el sender le asigna su ID de usuario, es importante mencionar que no se implemento una forma de guardar el ID despues de finalizada la ejecucion del programa, por lo cual al volver a iniciarse pedira nuevamente una ID
		-Se podria haber implementado, pero como no se usan credenciales ni el servidor guarda la lista de usuarios despues de su finalizacion (la cual debe ser forzada porque no tiene manera sana de cerrarse) se pueden dar casos extraños como que se inicie el cliente 4 nuevamente, pero el servidor se haya reiniciado y no aparezca en la lista de clientes cuando se pida, por lo mismo, esta pensando para que sus iteraciones sean reiniciadas para evitar esos problemas
	-Una vez con id asignado se le permite al usuario hacer request (salvo los 2 clientes que se hacen en el deployment del compose, que por limitaciones de los stdin estan automatizados). AKA enviar mensaje, pedir la lista de usuario o de mensajes enviados
	-El id de los mensajes se asigna una vez que lo recibe el servidor (sender) independiente de que el usuario al cual se encuentre destinado el mensaje no exista (aun), dada la naturaleza de rabbitmq, al intentar enviar el mensaje a dicho usuario, el mensaje sera desechado
Timestamp:
	-El timestamp se genera cuando el mensaje es recibido por el servidor, es añadido al mensaje original y es enviado a su destinatario

Log:

	-Para recuperar el log:
	sudo docker cp 'sender:/SD/'log'.txt /tmp/'log'.txt ---> el archivo quedara guardado en la carpeta tmp de la raiz del sistema (linux), en caso de usar windows se debe cambiar la raiz por una compatible
	-El log cada vez que se ejecute sender va a ser sobreescrito
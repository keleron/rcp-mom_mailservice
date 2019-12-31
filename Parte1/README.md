# Parte 1 - gRCP 
Construir con `docker-compose build --no-cache` y correr con `docker-compose up`. Finalmente para entrar al contenedor con el `app.log` se utiliza el comando `sudo docker exec -it ps_server /bin/bash` seguido de `cat app.log`

## Consideraciones especiales
Debido a que docker-compose no permite una consola interactiva los mensajes se cargan desde un archivo con inputs. Donde el primer argumento de `python3 cliente argv[1]` será el nombre del archivo a utilizar, en caso de no especificar archivo, los inputs serán los comunes y corrientes. 

Dentro del mismo `docker-compose.yml` se especifican dos clientes distintos meramente para que el proceso de automatizacion el container `ps_client` esté vivo y el `ps_client2` le mande mensajes. 

```PYTHON
def fun(a=""):
    print(a, end=" ")
    global f; return f.readline().strip()

if len(argv)>1:
    f = open(argv[1], "r")
    flag = True
    input = fun
else:
    flag = False
```

## Como agregar mas clientes

- Desde tu propia maquina puedes crear una nueva carpeta con los archivos `client.py`, `mail_pb2_grpc.py` y `mail_pb2.py` y correr con `python3 client.py`
- Debido a que docker-compose no permite el uso del parametro `replicas` sin usar swarm, se tendría que agregar otro servicio exactamente igual para agregar otro cliente.
- La ultima opcion es usar el Dockerfile, crear una imagen y correrla. 
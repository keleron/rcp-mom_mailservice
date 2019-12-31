# Parte 1 - gRCP 
Construir con `docker-compose build --no-cache` y correr con `docker-compose up`. Finalmente para entrar al contenedor con el `app.log` se utiliza el comando `sudo docker exec -it ps_server /bin/bash` seguido de `cat app.log`

## Consideraciones especiales
- Debido a que docker-compose no permite una consola interactiva los mensajes se cargan desde un archivo con inputs. Donde el primer argumento de `python3 cliente argv[1]` será el nombre del archivo a utilizar.
```PYTHON
if len(argv)>1:
    f = open(argv[1], "r")
    flag = True
    input = fun
else:
    flag = False
```
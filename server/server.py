from datetime import datetime as dt

from concurrent import futures
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

whole = ""
enviados = dict()
bandeja  = dict()
_id = 1
#sudo docker run -t -i tarea:server /bin/bash

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    global enviados, bandeja

    def ShowBandeja(self, request, context):
        m = "\n\n".join(bandeja[request.username])
        return helloworld_pb2.Request(username=m)

    def ShowEnviados(self, request, context):
        m = "\n\n".join(enviados[request.username])
        return helloworld_pb2.Request(username=m)

    def ListAllUsers(self, request, context):
        m = "\n".join(enviados.keys())
        m = helloworld_pb2.Request(username=m)
        return m

    def Log(self, request, context):
        m = f"USUARIO {request.username} LOGGEADO"
        if not request.username in enviados.keys():
            enviados[request.username] = []
            bandeja[request.username] = []
            m = f"USUARIO {request.username} REGISTRADO"
        print(m)
        return helloworld_pb2.Request(username=m)


    def SendText(self, request, context):
        global _id
        m = f"[{request.date}] [{_id}] # {request.from_user} -> {request.to_user}\n\t{request.text}"
        _id+=1
        print(m)
        reply = helloworld_pb2.Text(from_user="SERVER", to_user = request.from_user \
            ,text = "RECIVIDO", date="NO DATE")

        enviados[request.from_user].append(m)
        bandeja[request.to_user].append(m)

        return reply


def serve():
    print(chr(27) + "[2J")
    print("...SERVER STARTING...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()

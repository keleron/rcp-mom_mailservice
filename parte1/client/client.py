from __future__ import print_function
import logging
import threading
# from time import sleep
from datetime import datetime as dt
from time import sleep
from sys import argv

import grpc
import mail_pb2
import mail_pb2_grpc

menu1 = """
---------------------{}------------------------
 1- Enviar
 2- Bandeja
 3- Lista de Usuarios
 4- Enviados
"""
def fun(a=""):
    print(a, end=" ")
    global f; return f.readline().strip()

if len(argv)>1:
    f = open(argv[1], "r")
    flag = True
    input = fun
else:
    flag = False

def run(username, stub):
    while (True):
        # print(chr(27) + "[2J")
        print(menu1.format(username))
        menu = input(">>> ")
        if flag: sleep(1)
        if menu=="1":
            while True:
                to_user = input("to user: ")
                m = mail_pb2.Request(username="empty")

                lu = stub.ListAllUsers(m).username.split("\n")

                if not to_user in lu:
                    print("DESTINATARIO NO EXISTE")
                    continue

                body = input("   body:\n\t")
                date = dt.now().strftime('%Y-%m-%d %H:%M:%S')
                curr_mensaje = mail_pb2.Text(from_user=username, to_user = to_user,text = body, date=date)
                stub.SendText(curr_mensaje)
                # print("\t(Press any key to continue)"); getch.getch()
                break

        if menu == "2":
            m = mail_pb2.Request(username=username)
            lu = stub.ShowBandeja(m).username
            print(lu)
            input()
            # print("\t(Press any key to continue)"); getch.getch()

        elif menu == "3":
            m = mail_pb2.Request(username=username)
            users = stub.ListAllUsers(m)
            print(users.username)
            input()
            # print("\t(Press any key to continue)"); getch.getch()
        
        elif menu == "4":
            m = mail_pb2.Request(username=username)
            lu = stub.ShowEnviados(m).username
            print(lu)
            input(); sleep(1)
            # print("\t(Press any key to continue)"); getch.getch()
        elif menu == "5":
            return
        # print("\t(Press any key to continue)"); getch.getch()




if __name__ == '__main__':
    # print(chr(27) + "[2J")
    print("INICIANDO CLIENTE")
    # server_ip = input().strip(); sleep(1);
    server_ip = "localhost"
    # server_ip = "SERVER"
    username = input("username: ");
    
    channel = grpc.insecure_channel(f'{server_ip}:50051')
    stub = mail_pb2_grpc.GreeterStub(channel)
    m = mail_pb2.Request(username = username)
    response = stub.Log(m)
    run(username, stub)

    print("TERMINANDO CLIENTE")

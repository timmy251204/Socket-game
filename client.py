import socket
from threading import Thread
import random

client = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM
)


client.connect(
    ((str(input())), 9090)

)


unit = 0
print("""Вы играете в шахматы""")
print("""Задача ладей поставить мат ,Короля спастись, а зрителя наслаждаться игрой""")
print("""Ход вам нужно писать в формате координата начала хода, тире, координата конца хода и ваш секретный код""")


def listen_server():
    while True:
        data = client.recv(2048)
        print(data.decode('utf-8'))


def send_server():
    listen_thread = Thread(target=listen_server)
    listen_thread.start()
    while True:
        client.send(input("").encode("utf-8"))

if __name__ == '__main__':
    send_server()

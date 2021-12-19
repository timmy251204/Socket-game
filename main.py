import socket
import threading
import game
def doska(board):
    s = ''
    for i in range(0,8):
        for j in range(8):
            s += board[i][j]
        s += '\n'
    return s
server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM

)

server.bind(
    ("127.0.0.1", 9090)
)

server.listen(5)
users = []
print("Server is listening")
board = [['/', '/', '/', '/','/', '/', '/', '/'],['L', '/', '/', '/','/', '/', '/', '/'],
         ['/', '/', '/', '/','K', '/', '/', '/'],['/', '/', '/', '/','/', '/', '/', '/'],
         ['/', '/', '/', '/','/', '/', '/', '/'],['/', '/', '/', '/','/', '/', '/', '/'],
         ['/', '/', '/', '/','/', '/', '/', '/'],['/', '/', '/', '/','/', '/', '/', 'L']]


def send_all(data):
    for user in users:
        # user.send(data)
        user.send(bytes(data, encoding="UTF-8"))


def listen_user(user):
    print('Listening user')
    while True:
        data = user.recv(1024)
        data = data.decode(encoding='UTF-8')
        print(data)
        message = game.move(data,board)
        send_all(message)
        if message == 'Ахахаххахахахах лаьди выиграли':
            break


def start_server():
    while True:
        user_socket, address = server.accept()
        print(f"User <{address[0]}> connected")
        users.append(user_socket)
        listen_accepted_user = threading.Thread(
            target=listen_user,
            args=(user_socket,)
            )
        user_socket.send(doska(board).encode('utf-8'))
        if len(users) == 1:
            user_socket.send("Вы играете за ладью, ваш секретный код $".encode('utf-8'))
        elif len(users) == 2:
            user_socket.send("Вы играете за короля, ваш секретный код &".encode('utf-8'))
        else:
            user_socket.send("Вы просто зритель".encode('utf-8'))
        listen_accepted_user.start()
if __name__ == '__main__':
    start_server()

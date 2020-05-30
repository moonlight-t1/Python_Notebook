import socket
import os
from threading import Thread


def recv_message(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
sock.connect(("127.0.0.1", 12000))

th = Thread(target=recv_message, args=(sock, ))  # 쓰레드는 argument는 튜플 형태로 넘겨준다
th.daemon = True
th.start()

os.system("cls")
while True:
    msg = input("입력: ")
    sock.send(msg.encode())

    if msg == "/q":
        break

sock.close()

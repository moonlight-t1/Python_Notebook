"""
서버 역할
1. 소켓 생성
2. 바인딩
3. 접속대기
4. 접속수락
5. 데이터 송/수신
6. 접속종료
"""

import socket
print("1. 소켓 생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPV4, TCP 소켓

print("2. 바인딩")  # 서버에 이 운영체제와 ip를 쓴다고 알려준다
sock.bind(("", 12000))

print("3. 접속대기")
sock.listen()

print("4. 접속수락")  # 접속이 된 클라이언트 소켓과 주소가 리턴이 된다
c_sock, addr = sock.accept()

print("5. 데이터 송/수신")
receive_data = c_sock.recv(1024)
print("수신된 데이터: {}".format(receive_data))

print("6. 접속종료")
c_sock.close()  # 클라이언트 소켓 종료
sock.close()  # 리슨하고 있는 소켓 종료

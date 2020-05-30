import socketserver
import os


# BaseRequestHandler를 상속한다
class MyHandler(socketserver.BaseRequestHandler):
    users = {}

    # 모든 사람에게 메세지 전송
    def send_all_message(self, msg):
        for sock, _ in self.users.values():  # user 키 값을 이용해 sock 을 가져온다
            sock.send(msg.encode())

    def handle(self):
        print(self.client_address)

        # 유저 등록
        while True:
            self.request.send("채팅 닉네임을 입력하세요 : ".encode())
            nickname = self.request.recv(1024).decode()
            if nickname in self.users:
                self.request.send("이미 등록된 닉네임 입니다.\n".encode())
            else:
                self.users[nickname] = (
                    self.request, self.client_address)  # 튜플 형태로 유저 정보 저장
                print("현재 {} 명 참여중".format(len(self.users)))
                self.send_all_message("[{}] 님이 입장 했습니다.".format(nickname))
                break

        # 채팅
        while True:
            msg = self.request.recv(1024)
            if msg.decode() == "/q":
                self.request.close()
                break
            self.send_all_message("[{}] {}".format(nickname, msg.decode()))

        if nickname in self.users:
            del self.users[nickname]
            self.send_all_message("[{}] 님이 퇴장하셨습니다.".format(nickname))
            print("현재 {} 명이 참여중".format(len(self.users)))


# 두 클래스를 상속받아 믹스인 클래스를 만든다
class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


os.system("cls")
server = ChatServer(("", 12000), MyHandler)  # 주소 + 포트, 핸들러
server.serve_forever()  # 서버 구동
server.shutdown()  # 서버 종료
server.server_close()  # 서버 닫기

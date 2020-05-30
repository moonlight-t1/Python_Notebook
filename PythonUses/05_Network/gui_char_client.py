import tkinter
import socket
from threading import Thread

IP = ""
PORT = 0


def recv_message(sock):
    while True:
        msg = sock.recv(1024)
        chat_list.insert(tkinter.END, msg.decode())  # chat_list를 tkinter에 삽입한다
        chat_list.see(tkinter.END)  # chat_list를 보여준다


def connect(event=None):
    global IP, PORT
    connect_string = input_string.get()  # IP와 PORT를 가져온다.
    addr = connect_string.split(":")  # IP와 PORT를 분리한다
    IP = addr[0]
    PORT = int(addr[1])
    w_connect.destroy()


def send_message(event=None):
    msg = input_msg.get()
    sock.send(msg.encode())
    input_msg.set("")
    if msg == "/bye":
        sock.close()
        window.quit()
    pass


w_connect = tkinter.Tk()
w_connect.title("접속대상")


tkinter.Label(w_connect, text="접속대상").grid(row=0, column=0)  # 라벨
input_string = tkinter.StringVar(value="127.0.0.1:12000")  # 파이썬의 string을 넘겨준다
input_addr = tkinter.Entry(
    w_connect, textvariable=input_string, width=20)  # 입력창
input_addr.grid(row=0, column=1, padx=5, pady=5)
c_button = tkinter.Button(w_connect, text="접속하기", command=connect)  # 버튼
c_button.grid(row=0, column=2, padx=5, pady=5)

width = 330
height = 45

# 화면을 가운데 뜨게 하기 위해서
# 컴퓨터 전체 해상도를 구한다.
screen_width = w_connect.winfo_screenwidth()
screen_height = w_connect.winfo_screenheight()

# 구한 해상도에서 가운데 위치를 구한다.
x = int((screen_width / 2) - (width / 2))
y = int((screen_height / 2) - (height / 2))

# geometry
w_connect.geometry('{}x{}+{}+{}'.format(width, height, x, y))
w_connect.mainloop()

# 채팅창
window = tkinter.Tk()
window.title("클라이언트")

# 스크롤바
frame = tkinter.Frame(window)
scroll = tkinter.Scrollbar(frame)  # 스크롤바는 frame에 있다
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# 채팅 리스트
chat_list = tkinter.Listbox(
    frame, height=15, width=50, yscrollcommand=scroll.set)
chat_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
frame.pack()

input_msg = tkinter.StringVar()
inputbox = tkinter.Entry(window, textvariable=input_msg)
inputbox.bind("<Return>", send_message)  # 리턴키가 눌리면 send_message 동작
inputbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH,
              expand=tkinter.YES, padx=5, pady=5)  # pack 함수를 이용해서 위치
send_button = tkinter.Button(window, text="전송", command=send_message)
send_button.pack(side=tkinter.RIGHT, fill=tkinter.X, padx=5, pady=5)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
sock.connect((IP, PORT))

th = Thread(target=recv_message, args=(sock, ))  # 쓰레드는 argument는 튜플 형태로 넘겨준다
th.daemon = True
th.start()

window.mainloop()

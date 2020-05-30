"""
매직 패킷은 16진수 FF 상수값이 6번 반복 + 대상 컴퓨터의 맥어드레서가 16번 반복(16진수)되어야 한다.
"""

import struct
import socket
import os

mycoms = {
    "pc1": "AA-BB-CC-DD-EE-FF",
    "pc2": "AA-BB-CC-DD-EE-FF",
    "Notebook": "AA-BB-CC-DD-EE-FF",
}

mac = "38-D5-47-0E-90-40"  # 접속할 컴퓨터 맥 주소


def wake_on_lan(mac):
    addrs = mac.split("-")  # split 한다
    # 16진수로 정수 형태로 바꾼다음 B 한칸 한칸에 담는다
    hw_addr = struct.pack("BBBBBB", int(addrs[0], 16), int(addrs[1], 16), int(
        addrs[2], 16), int(addrs[3], 16), int(addrs[4], 16), int(addrs[5], 16))

    magic = b"\xFF" * 6 + hw_addr * 16  # 16진수 FF가 바이트 형태로 6번 반복
    print(magic)

    # 매직 패킷은 UDP 형태로 보내야 한다
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # BROADCAST는 통볼르 한다는 의미이다.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # 공유기에 연결된 모든 네트워크에 magic 패킷을 쏜다.
    # 하드웨에 주소값에 해당되는 컴퓨터만 반응한다.
    s.sendto(magic, ('192.168.0.255', 7))  # 255 아이피는 broadcast용으로 사용된다
    s.close()


if __name__ == "__main__":
    os.system("cls")
    count = 1
    for name, mac in mycoms.items():
        print("{} {} ({})".format(count, mac, name))
        count += 1
    print("=" * 70)
    select = int(input("매직패킷을 보낼 PC 번호를 입력하세요."))
    name, mac = list(mycoms.items())[select - 1]
    # print(name, mac)
    wake_on_lan(mac)

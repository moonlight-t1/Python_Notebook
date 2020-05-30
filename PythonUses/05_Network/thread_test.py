import time
import threading


def 주문받기():
    for i in range(5):
        print("주문받기 {}".format(i))
        time.sleep(1)


def 우편발송():
    for i in range(5):
        print("우편발송 {}".format(i))
        time.sleep(0.5)


# 쓰레드 할당
th1 = threading.Thread(target=주문받기)
th2 = threading.Thread(target=우편발송)

# 메인 쓰레드가 죽으면 각각의 쓰레드는 종료된다
th1.daemon = True
th2.daemon = True

th1.start()
th2.start()

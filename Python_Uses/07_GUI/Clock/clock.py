from PyQt5 import QtWidgets
from PyQt5 import QtCore


class MyClock(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mouseClick = False
        self.setWindowTitle("시계")
        self.initWidgets()
        self.setFixedSize(250, 100)  # 크기 고정
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 타이틀 바 삭제
        self.show()

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.mouseClick = True
            self.oldPos = e.globalPos()  # 마우스 현재 좌표가 튜플 형태로
            print(self.oldPos)

    def mouseReleaseEvent(self, e):
        self.mouseClick = False

    def keyPressEvent(self, e):
        # ESC 키 누르면 종료
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mouseMoveEvent(self, e):
        if self.mouseClick:  # 사용자가 마우스 클릭을 한 상태에서만 동작
            delta = QtCore.QPoint(
                e.globalPos() - self.oldPos)  # 현재위치에서 지난 위치 뺀 값
            self.move(self.x() + delta.x(), self.y() +
                      delta.y())  # delta 만큼 이동
            self.oldPos = e.globalPos()  # 이동한 좌표하 oldPos가 된다
            print(self.oldPos)

    def initWidgets(self):
        self.layout = QtWidgets.QVBoxLayout()
        self.lcd = QtWidgets.QLCDNumber()  # LCD 숫자를 표현하는 클래스가 PyQt에 있다
        self.lcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)  # Flat 속성
        self.lcd.setDigitCount(8)  # 8자리
        self.lcd.setFrameStyle(QtWidgets.QFrame.NoFrame)  # 프레임 없앤다

        self.timer = QtCore.QTimer()  # timer 생성
        self.timer.timeout.connect(self.show_time)  # timeout 이벤트 연결
        self.timer.start(1000)  # 1초에 한번씩 동작

        self.show_time()

        # 레이아웃에 시계를 담아준다.
        self.layout.addWidget(self.lcd)
        self.setLayout(self.layout)

    # 시계
    def show_time(self):
        time = QtCore.QTime.currentTime()
        self.currentTime = time.toString("hh:mm:ss")  # 포맷팅
        self.lcd.display(self.currentTime)


app = QtWidgets.QApplication([])
win = MyClock()
app.exec_()

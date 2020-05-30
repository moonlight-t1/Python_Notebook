from PyQt5 import QtWidgets
from PyQt5 import QtCore


class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  # 부모의 생성자를 먼저 호출해야 한다
        self.setWindowTitle("파이썬 GUI")

        label1 = QtWidgets.QLabel("라벨1 입니다", self)  # 라벨 생성
        label1.setAlignment(QtCore.Qt.AlignCenter)  # QtCore에는 정렬 등이 있다
        label1.resize(60, 25)

        label2 = QtWidgets.QLabel("라벨2 입니다.", self)
        label2.setAlignment(QtCore.Qt.AlignRight)
        # HTML stylesheet를 사용할 수 있다
        label2.setStyleSheet("color:red; font-size:20px")

        layout = QtWidgets.QVBoxLayout()  # 레이아웃 생성, VBOX 는 Vertical로 배치한다
        layout.addWidget(label1)  # 레이아웃에 위젯을 넣는다
        layout.addWidget(label2)  # 레이아웃에 위젯을 넣는다

        self.setLayout(layout)
        self.show()


app = QtWidgets.QApplication([])
win = MyWindows()
app.exec_()

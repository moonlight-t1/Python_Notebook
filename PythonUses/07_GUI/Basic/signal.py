from PyQt5 import QtWidgets


class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  # 부모의 생성자를 먼저 호출해야 한다
        self.setWindowTitle("푸시버튼")

        button1 = QtWidgets.QPushButton(self)
        button1.setText("버튼1")

        button2 = QtWidgets.QPushButton(self)
        button2.setText("버튼2")

        button1.clicked.connect(self.button_clicked) # 버튼이 클릭하면 함수와 연결한다
        button2.clicked.connect(self.button_clicked)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)
        self.show()

    # 슬롯 함수
    def button_clicked(self):
        sender = self.sender()
        QtWidgets.QMessageBox.about(self, "버튼테스트", sender.text()) # sender 변수에 text를 담아 보낸다


app = QtWidgets.QApplication([])
win = MyWindows()
app.exec_()

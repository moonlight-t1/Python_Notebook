from PyQt5 import QtWidgets
import sys


# 보통은 클래스를 만들어서 사용한다
class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()  # 부모의 생성자를 먼저 호출해야 한다
        self.setWindowTitle("파이썬 GUI")
        self.resize(400, 300)
        self.show()


app = QtWidgets.QApplication([])
win = MyWindows()
sys.exit(app.exec_())


# app = QtWidgets.QApplication([])  # Qt 인스턴스
# win = QtWidgets.QDialog()
# win.setWindowTitle("파이썬 GUI")
# win.show()
# app.exec_()

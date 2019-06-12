import socket
import time
import random
import sys
from PyQt5 import QtWidgets, QtCore


class Win(QtWidgets.QWidget):
    def __init__(self):
        super(Win, self).__init__(flags=QtCore.Qt.Widget)
        self.resize(400, 300)

        self.bt = QtWidgets.QPushButton('同步Socket')
        self.bt.setFixedHeight(40)
        self.sld = QtWidgets.QSlider()
        self.sld.setOrientation(QtCore.Qt.Horizontal)
        self.lb = QtWidgets.QLabel()
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.bt)
        lay.addWidget(self.lb)
        lay.addWidget(self.sld)

        self.skt = socket.socket()
        self.skt.connect(('localhost', 23232))

        self.bt.clicked.connect(lambda: self.skt_rw(random.random()))

        self.le = QtWidgets.QLineEdit()

    def skt_rw(self, a):
        self.skt.send(bytes(str(a), encoding='utf-8'))
        # time.sleep(0.1)
        data = self.skt.recv(1024).decode('utf-8')
        self.lb.setText(data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())

from queue import Queue
import socket
import time
import random
import sys
from PyQt5 import QtWidgets, QtCore


class Win(QtWidgets.QWidget):
    def __init__(self):
        super(Win, self).__init__(flags=QtCore.Qt.Widget)
        self.resize(400, 300)

        self.bt = QtWidgets.QPushButton('异步Socket')
        self.bt.setFixedHeight(40)
        self.sld = QtWidgets.QSlider()
        self.sld.setOrientation(QtCore.Qt.Horizontal)
        self.lb = QtWidgets.QLabel()
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.bt)
        lay.addWidget(self.lb)
        lay.addWidget(self.sld)
        self.tcp_thread = TcpThread()

        self.bt.clicked.connect(lambda: self.tcp_thread.msg_queue.put(random.random()))
        self.tcp_thread.receive_data.connect(self.receive)

        self.tcp_thread.start()

    def receive(self, s: list):
        print(s)
        self.lb.setText(s[0])

    def skt_rw(self, a):
        with self.skt_lock:
            self.skt.write(bytes(str(a), encoding='utf-8'))
            time.sleep(0.1)
            print(self.skt.readAll())


class TcpThread(QtCore.QThread):
    receive_data = QtCore.pyqtSignal(list)

    def __init__(self):
        super(TcpThread, self).__init__()
        self.msg_queue = Queue()
        self.skt = socket.socket()
        self.skt.connect(('localhost', 23232))

    def run(self):

        while True:
            if not self.msg_queue.empty():
                a = self.msg_queue.get()
                self.skt.send(bytes(str(a), encoding='utf-8'))
                # time.sleep(0.1)
                data = self.skt.recv(1024).decode('utf-8')
                self.receive_data.emit([data])
            # time.sleep(0.1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())

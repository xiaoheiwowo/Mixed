from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QPainter, QPen
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from threading import Thread

import pygks as pk
import win32api as win32
import PyHook3
import pythoncom

caps = win32.GetKeyState(pk.VK_CAPITAL)
qt = 0


class CapsLockWidget(QWidget):

    start_timer = QtCore.pyqtSignal()

    def __init__(self):
        super(CapsLockWidget, self).__init__()
        self.setFixedSize(150, 150)

        self.setWindowTitle("CapsLock")
        self.setObjectName('MainWin')
        # self.setFocusPolicy(Qt.StrongFocus)

        # self.tray_icon = QSystemTrayIcon(self)
        # self.icon = QtGui.QIcon('logo.png')
        # self.tray_icon.setIcon(self.icon)
        # self.tray_icon.show()

        # self.setStyleSheet('#MainWin{background:blue}')
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.timer_1 = QtCore.QTimer()

        self.start_timer.connect(self.timer_start)
        self.timer_1.timeout.connect(self.hide)
        self.start_timer.emit()
        # print('run')

    def timer_start(self):
        self.timer_1.start(1000)

    def win_hide(self):
        self.timer_1.stop()
        self.hide()

    # def keyPressEvent(self, event):
    #     if type(event) == QKeyEvent and event.key() == Qt.Key_CapsLock:
    #         # print(hex(event.key()))
    #         # print('CapsLock')
    #         print(win32.GetKeyState(pk.VK_CAPITAL))

    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)
        qp.begin(self)
        self.draw_frame(qp)
        qp.end()
        self.show()

    def draw_frame(self, qp):
        pen = QPen(Qt.darkGray, 1, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(Qt.darkGray)
        # qp.setBrush(QtGui.QColor(0, 0, 0, 50))
        qp.drawRoundedRect(0, 0, 150, 150, 10, 10)
        qp.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        qp.setFont(QtGui.QFont("Concolas", 100, QtGui.QFont.Bold))
        global caps
        if caps == 0:
            qp.drawText(40, 120, 'A')
        else:
            qp.drawText(40, 105, 'a')


class QtThread(Thread):
    def __init__(self):
        super(QtThread, self).__init__()

    def run(self):
        self.app = QApplication(sys.argv)
        self.win = CapsLockWidget()
        self.win.show()
        sys.exit(self.app.exec_())


def onKeyboardEvent(event):
    # print(type(event.Key))
    # print(event.Key)
    if event.Key == 'Capital':
        global caps
        caps = win32.GetKeyState(pk.VK_CAPITAL)

        global qt
        qt = QtThread()
        qt.start()
        # print(caps)
    return True


if __name__ == '__main__':
    # 创建一个“钩子”管理对象
    hm = PyHook3.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()


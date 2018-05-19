#!/usr/bin/python3
import sys
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class App(QWebEngineView):
    """docstring for App"""

    def __init__(self):
        super().__init__()
        self.title = ''
        self.web_url = ''
        self.time_alive = 10
        self.left = 10
        self.top = 10
        self.width = 1080
        self.height = 164

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.load(QUrl(self.web_url))
        self.show()
        QTimer.singleShot(self.time_alive * 1000, self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    if len(sys.argv) > 1:
        args = sys.argv[1].split(' ')
        ex.web_url = args[0]
        ex.time_alive = float(args[1])
        ex.left = int(args[2])
        ex.top = int(args[3])
        ex.width = int(args[4])
        ex.height = int(args[5])
    ex.initUI()
    sys.exit(app.exec_())

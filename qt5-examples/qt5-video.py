from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *

import sys


class Widget(QVideoWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Video'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


class Player(QMediaPlayer):
    """docstring for Player"""

    def __init__(self):
        super().__init__()

    def set_output(self, app):
        self.setVideoOutput(app)


class Playlist(QMediaPlaylist):
    """docstring for Playlist"""

    def __init__(self, player):
        super().__init__(player)
        self.setCurrentIndex(1)

    def add_content(self, video_src):
        content = QMediaContent(QUrl.fromLocalFile(video_src))
        self.addMedia(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    player = Player()
    playlist = Playlist(player)
    src = ""
    playlist.add_content(src)
    player.play()
    sys.exit(app.exec_())

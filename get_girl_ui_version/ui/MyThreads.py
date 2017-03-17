# -*- coding: utf-8 -*-
from PyQt5 import QtCore
import GetMezi


class AlbumsThread(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self, path, albums):
        """Constructor"""
        super(AlbumsThread, self).__init__(None)
        self.path = path
        self.albums = albums

    def run(self):
        GetMezi._download_albums(self.path, self.albums)
        self.finishSignal.emit(['hello,','world','!'])


class SingleAlbumThread(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(list)
    def __init__(self, path, title, url):
        super(SingleAlbumThread, self).__init__(None)
        self.path = path
        self.title = title
        self.url = url

    def run(self):
        GetMezi._download_imgs(self.path, self.title, self.url)
        self.finishSignal.emit(['hello,','world','!'])
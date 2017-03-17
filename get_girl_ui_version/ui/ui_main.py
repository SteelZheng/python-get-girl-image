# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\zhenggang\Desktop\spider.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import re
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from ui.MyThreads import *
import GetMezi


class Ui_Dialog(QDialog):
    TYPE_MORE = 0
    TYPE_SINGLE = 1

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.setEnabled(True)
        Dialog.resize(477, 219)
        Dialog.setMinimumSize(QtCore.QSize(477, 219))
        Dialog.setMaximumSize(QtCore.QSize(477, 219))
        Dialog.setMouseTracking(False)
        Dialog.setWindowIcon(QIcon('phoenix.ico'))
        self.setWindowFlags(QtCore.Qt.Window)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 431, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.urlL_ineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.urlL_ineEdit.setObjectName("urlL_ineEdit")
        self.horizontalLayout_2.addWidget(self.urlL_ineEdit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 431, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.save_path_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.save_path_lineEdit.setEnabled(False)
        self.save_path_lineEdit.setObjectName("save_path_lineEdit")
        self.horizontalLayout_3.addWidget(self.save_path_lineEdit)
        self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_3)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(Dialog.slot_openFileManager)

        self.horizontalLayout_3.addWidget(self.toolButton)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.downloadButton = QtWidgets.QPushButton(Dialog)
        self.downloadButton.setObjectName("downloadButton")
        self.downloadButton.clicked.connect(Dialog.slot_startDownload)

        self.horizontalLayout_7.addWidget(self.downloadButton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def slot_startDownload(self):
        url = self.urlL_ineEdit.text()
        path = self.save_path_lineEdit.text()
        type = self.comboBox.currentIndex()
        try:
            if url is None or url.strip() == "":
                QMessageBox.information(self, "提示", "请输入爬取地址！", QMessageBox.Yes)
            elif not re.match('http:\/\/.*?\/', url):
                QMessageBox.information(self, "提示", "网址格式不正确！", QMessageBox.Yes)
            elif path is None or path.strip() == "":
                QMessageBox.information(self, "提示", "请选择图片保存路径！", QMessageBox.Yes)
            else:
                html = GetMezi._get_html(url)
                soup = GetMezi._get_soup(html)
                if self.TYPE_MORE == type:
                    albums = GetMezi._get_img_dirs(soup)
                    if None == albums:
                        QMessageBox.information(self, "提示", "无法获取该网页下的相册内容，妹子图网页内容有可能发生了变化，请联系作者获取最新的程序！", QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, "提示", "已开始下载...", QMessageBox.Yes)
                        self.downloadButton.setDisabled(True)
                        self.bwThread = AlbumsThread(path, albums)
                        self.bwThread.finishSignal.connect(self.resetDownloadBtn)
                        self.bwThread.start()

                elif self.TYPE_SINGLE == type:
                    title = GetMezi._get_page_title(soup)
                    QMessageBox.information(self, "提示", "已开始下载...", QMessageBox.Yes)
                    self.downloadButton.setDisabled(True)
                    self.bwThread = SingleAlbumThread(path, title, url)
                    self.bwThread.finishSignal.connect(self.resetDownloadBtn)
                    self.bwThread.start()

        except Exception as e:
            print(e)
            QMessageBox.information(self, "错误", "请检查‘爬取类型’和‘爬取地址’是否匹配，\n 多个相册（网页上有多个相册）\n 例如：http://www.mzitu.com/ \n 或 http://www.mzitu.com/xinggan \n 单一相册（网页上单张照片页面）：\n http://www.mzitu.com/75636 ", QMessageBox.Yes)


    def resetDownloadBtn(self):
        self.downloadButton.setDisabled(False)
        QMessageBox.information(self, "提示", "下载完毕", QMessageBox.Yes)


    def slot_openFileManager(self):
        open = QFileDialog()
        self.path = open.getExistingDirectory()
        self.save_path_lineEdit.setText(self.path)
        print(self.path)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "妹子图--定做软件请联系作者QQ:420430604"))
        self.label.setText(_translate("Dialog", "爬取类型："))
        self.comboBox.setItemText(0, _translate("Dialog", "多个相册    "))
        self.comboBox.setItemText(1, _translate("Dialog", "单一相册    "))
        self.label_2.setText(_translate("Dialog", "爬取地址："))
        self.label_3.setText(_translate("Dialog", "保存地址："))
        self.toolButton.setText(_translate("Dialog", "选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "妹子图"))
        self.downloadButton.setText(_translate("Dialog", "开始下载"))
        self.urlL_ineEdit.setText("http://www.mzitu.com/")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Ui_Dialog()
    main.show()
    sys.exit(app.exec_())

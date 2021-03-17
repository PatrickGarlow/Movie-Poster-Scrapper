# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelMovieTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelMovieTitle.setGeometry(QtCore.QRect(10, 10, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelMovieTitle.setFont(font)
        self.labelMovieTitle.setObjectName("labelMovieTitle")
        self.labelMoviePassword = QtWidgets.QLabel(self.centralwidget)
        self.labelMoviePassword.setGeometry(QtCore.QRect(10, 50, 331, 491))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.labelMoviePassword.setFont(font)
        self.labelMoviePassword.setObjectName("labelMoviePassword")
        self.buttonDownload = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDownload.setGeometry(QtCore.QRect(10, 580, 341, 51))
        self.buttonDownload.setObjectName("buttonDownload")
        self.buttonCopyLink = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCopyLink.setGeometry(QtCore.QRect(250, 550, 101, 28))
        self.buttonCopyLink.setObjectName("buttonCopyLink")
        self.labelMovieLink = QtWidgets.QLabel(self.centralwidget)
        self.labelMovieLink.setGeometry(QtCore.QRect(10, 550, 231, 31))
        self.labelMovieLink.setObjectName("labelMovieLink")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Result"))
        self.labelMovieTitle.setText(_translate("MainWindow", "Movie Title"))
        self.labelMoviePassword.setText(_translate("MainWindow", "TextLabel"))
        self.buttonDownload.setText(_translate("MainWindow", "Download"))
        self.buttonCopyLink.setText(_translate("MainWindow", "PushButton"))
        self.labelMovieLink.setText(_translate("MainWindow", "Link"))


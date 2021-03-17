# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MobiePosterScrapper.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib
import requests
from PyQt5.QtWidgets import QFileDialog
from bs4 import BeautifulSoup
import csv
import sys
import time
import PyPDF2
import xlrd

class Result_MainWindow(object):
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
def scrapper(input_string):
    poster_url2 = "/media/movie_posters/default.png"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    movie_title = input_string
    query = movie_title.replace(' ', '+').replace(":", "%3A").replace('(', '%28').replace(')', '%29')

    URL = 'https://www.imdb.com/find?q=' + query + '&ref_=nv_sr_sm'

    headers = {"user-agent": USER_AGENT}
    try:
        resp1 = requests.get(URL, headers=headers)

        soup1 = BeautifulSoup(resp1.content, "html.parser")

        soup1.findAll('td', {"class": "primary_photo"})[0].a['href']

        movie_url = 'https://www.imdb.com' + soup1.findAll('td', {"class": "primary_photo"})[0].a['href']

        resp2 = requests.get(movie_url, headers=headers)
        soup2 = BeautifulSoup(resp2.content, "html.parser")
        if soup2.find('div', {"class": "poster"}) == None:
            poster_url2 = "/media/movie_posters/default.png"
        else:
            poster_url1 = 'https://www.imdb.com' + soup2.find('div', {"class": "poster"}).a['href']
            resp3 = requests.get(poster_url1, headers=headers)
            soup3 = BeautifulSoup(resp3.content, "html.parser")
            poster_url2list = soup3.findAll('div', {'class': 'iUyzNI'})
            if len(poster_url2list) > 1:
                poster_url2 = poster_url2list[0].img['src']
            elif len(poster_url2list) == 1:
                poster_url2 = soup3.find('div', {'class': 'iUyzNI'}).img['src']
    except:
        poster_url2 = "/media/movie_posters/default.png"
    return poster_url2
class MoviePosterScrapper_MainWindow(object):
    def getSingleTitle(self):
        return self.lineEditSingleIn
    def startSinglePoster(self):
        #opens new window
        pass

    def getTypeIn(self):
        return self.comboFileTypeIn.currentText()
    def getTypeOut(self):
        return self.comboFileTypeOut.currentText()
    def getFormatOut(self):
        return self.comboFormatOut.currentText()

    def getfile(self):
        pass

    def startMultiple(self):
        if self.getFormatOut() == "Format" or self.getTypeIn() == "File Type" or self.getTypeOut() == "File Type":
            self.labelError.setText("One of the fields is incorrect.")
        else:
            in_Type = self.getTypeIn()
            out_Type = self.getTypeOut()
            out_Format = self.getFormatOut()
            titles_list = []
            file_in = ""
            if self.getTypeIn() == ".txt":
                rd = open(file_in, "r")
                for line in rd:
                    titles_list.append(line)
            elif self.getTypeIn() == ".xlsx":
                loc = file_in
                wb = xlrd.open_workbook(loc)
                sheet = wb.sheet_by_index(0)
                sheet.cell_value(0, 0)
                for i in range(sheet.nrows):
                    titles_list.append(sheet.cell_value(i, 0))
            elif self.getTypeIn() == ".csv":
                rd = csv.reader(fd, delimiter=",", quotechar='"')
                for row in rd:
                    titles_list.append(row)
            elif self.getTypeIn() == ".tsv":
                rd = csv.reader(fd, delimiter="\t", quotechar='"')
                for row in rd:
                    titles_list.append(row)
            elif self.getTypeIn() == ".pdf":
                pdfFileObj = open(file_in, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                num = pdfReader.numPages
                for x in range(num):
                    pageObj = pdfReader.getPage(x)
                    print(pageObj.extractText())
            print(titles_list)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 279)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 451, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.tabHome = QtWidgets.QWidget()
        self.tabHome.setObjectName("tabHome")
        self.labelHomeTitle = QtWidgets.QLabel(self.tabHome)
        self.labelHomeTitle.setGeometry(QtCore.QRect(10, 10, 421, 141))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.labelHomeTitle.setFont(font)
        self.labelHomeTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHomeTitle.setWordWrap(True)
        self.labelHomeTitle.setObjectName("labelHomeTitle")
        self.tabWidget.addTab(self.tabHome, "")
        self.tabSingle = QtWidgets.QWidget()
        self.tabSingle.setObjectName("tabSingle")
        self.lineEditSingleIn = QtWidgets.QLineEdit(self.tabSingle)
        self.lineEditSingleIn.setGeometry(QtCore.QRect(20, 40, 311, 28))
        self.lineEditSingleIn.setObjectName("lineEditSingleIn")
        self.labelSingleTitle = QtWidgets.QLabel(self.tabSingle)
        self.labelSingleTitle.setGeometry(QtCore.QRect(20, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSingleTitle.setFont(font)
        self.labelSingleTitle.setObjectName("labelSingleTitle")
        self.buttonSingleSearch = QtWidgets.QPushButton(self.tabSingle)
        self.buttonSingleSearch.setGeometry(QtCore.QRect(340, 40, 93, 28))
        self.buttonSingleSearch.setObjectName("buttonSingleSearch")
        self.buttonSingleSearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.tabWidget.addTab(self.tabSingle, "")
        self.tabMultiple = QtWidgets.QWidget()
        self.tabMultiple.setObjectName("tabMultiple")
        self.buttonChooseFile = QtWidgets.QPushButton(self.tabMultiple)
        self.buttonChooseFile.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.buttonChooseFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonChooseFile.setObjectName("buttonChooseFile")
        self.buttonChooseFile.clicked.connect(self.getfile)
        self.labelMultipleInput = QtWidgets.QLabel(self.tabMultiple)
        self.labelMultipleInput.setGeometry(QtCore.QRect(20, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMultipleInput.setFont(font)
        self.labelMultipleInput.setObjectName("labelMultipleInput")
        self.comboFileTypeIn = QtWidgets.QComboBox(self.tabMultiple)
        self.comboFileTypeIn.setGeometry(QtCore.QRect(130, 50, 121, 28))
        self.comboFileTypeIn.setObjectName("comboFileTypeIn")
        self.comboFileTypeIn.addItem("")
        self.comboFileTypeIn.addItem("")
        self.comboFileTypeIn.addItem("")
        self.comboFileTypeIn.addItem("")
        self.comboFileTypeIn.addItem("")
        self.comboFileTypeIn.addItem("")
        self.comboFileTypeIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboFileTypeOut = QtWidgets.QComboBox(self.tabMultiple)
        self.comboFileTypeOut.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.comboFileTypeOut.setObjectName("comboFileTypeOut")
        self.comboFileTypeOut.addItem("")
        self.comboFileTypeOut.addItem("")
        self.comboFileTypeOut.addItem("")
        self.comboFileTypeOut.addItem("")
        self.comboFileTypeOut.addItem("")
        self.comboFileTypeOut.addItem("")
        self.comboFileTypeOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboFormatOut = QtWidgets.QComboBox(self.tabMultiple)
        self.comboFormatOut.setGeometry(QtCore.QRect(130, 120, 121, 31))
        self.comboFormatOut.setObjectName("comboFormatOut")
        self.comboFormatOut.addItem("")
        self.comboFormatOut.addItem("")
        self.comboFormatOut.addItem("")
        self.comboFormatOut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.pushMultipleStart = QtWidgets.QPushButton(self.tabMultiple)
        self.pushMultipleStart.setGeometry(QtCore.QRect(270, 50, 101, 101))
        self.pushMultipleStart.setObjectName("pushMultipleStart")
        self.pushMultipleStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushMultipleStart.clicked.connect(self.startMultiple)

        self.labelMultipleOutput = QtWidgets.QLabel(self.tabMultiple)
        self.labelMultipleOutput.setGeometry(QtCore.QRect(20, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMultipleOutput.setFont(font)
        self.labelMultipleOutput.setObjectName("labelMultipleOutput")
        self.labelError = QtWidgets.QLabel(self.tabMultiple)
        self.labelError.setGeometry(QtCore.QRect(20, 160, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelError.setFont(font)
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.labelError.setStyleSheet('color: #ff0000')

        self.tabWidget.addTab(self.tabMultiple, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Poster Scrapper"))
        self.labelHomeTitle.setText(_translate("MainWindow", "Movie Poster Scrapper"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHome), _translate("MainWindow", "Home"))
        self.labelSingleTitle.setText(_translate("MainWindow", "Enter Movie Title"))
        self.buttonSingleSearch.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSingle), _translate("MainWindow", "Single Movie"))
        self.buttonChooseFile.setText(_translate("MainWindow", "Choose File"))
        self.labelMultipleInput.setText(_translate("MainWindow", "Input File"))

        self.comboFileTypeIn.setItemText(0, _translate("MainWindow", "File Type"))
        self.comboFileTypeIn.setItemText(1, _translate("MainWindow", ".txt"))
        self.comboFileTypeIn.setItemText(2, _translate("MainWindow", ".xlsx"))
        self.comboFileTypeIn.setItemText(3, _translate("MainWindow", ".csv"))
        self.comboFileTypeIn.setItemText(4, _translate("MainWindow", ".tsv"))
        self.comboFileTypeIn.setItemText(5, _translate("MainWindow", ".pdf"))

        self.comboFileTypeOut.setItemText(0, _translate("MainWindow", "File Type"))
        self.comboFileTypeOut.setItemText(1, _translate("MainWindow", ".txt"))
        self.comboFileTypeOut.setItemText(2, _translate("MainWindow", ".xlsx"))
        self.comboFileTypeOut.setItemText(3, _translate("MainWindow", ".csv"))
        self.comboFileTypeOut.setItemText(4, _translate("MainWindow", ".tsv"))
        self.comboFileTypeOut.setItemText(5, _translate("MainWindow", ".pdf"))

        self.comboFormatOut.setItemText(0, _translate("MainWindow", "Format"))
        self.comboFormatOut.setItemText(1, _translate("MainWindow", "Link"))
        self.comboFormatOut.setItemText(2, _translate("MainWindow", "Movie Title & Link"))
        self.pushMultipleStart.setText(_translate("MainWindow", "Start"))
        self.labelMultipleOutput.setText(_translate("MainWindow", "Output File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMultiple), _translate("MainWindow", "Multiple Movies"))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = MoviePosterScrapper_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: NewSession.py

# Band and Zones 要重建
# 找不到salary data的Label
# Regression & Grade Graph 要增加上下限

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
import pandas as pd, pickle, CompaniesCode, BenchmarkJobsCode, PolicyLinesCode, MatchwithFastCatJobsCode, UpdateSurveyData, CompensationMetricCode, GradesandRangesCode, visualizationManager
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class pickleHandler(object):

    def pickleLoad(self, file_Name):
        fileObject = open(file_Name, 'r')
        try:
            userData = pickle.load(fileObject)
        except:
            userData = pd.DataFrame()

        fileObject.close()
        return userData

    def pickleStore(self, file_Name, userData):
        fileObject = open(file_Name, 'wb')
        pickle.dump(userData, fileObject)
        fileObject.close()


class Ui_MainWindow(pickleHandler):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8('MainWindow'))
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        MainWindow.setBaseSize(QtCore.QSize(600, 500))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8('centralwidget'))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 121))
        self.label.setText(_fromUtf8(''))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8('LightGray.png')))
        self.label.setObjectName(_fromUtf8('label'))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(21, 34, 101, 51))
        self.label_3.setText(_fromUtf8(''))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8('qq.png')))
        self.label_3.setObjectName(_fromUtf8('label_3'))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(135, 43, 205, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8('label_4'))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(344, 14, 241, 91))
        self.label_5.setText(_fromUtf8(''))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8('gray.png')))
        self.label_5.setObjectName(_fromUtf8('label_5'))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 119, 600, 381))
        self.label_2.setText(_fromUtf8(''))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8('blue - Copy.png')))
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(353, 24, 47, 13))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8('label_6'))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(352, 44, 70, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8('label_7'))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(473, 21, 100, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_8.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8('label_8'))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(473, 45, 80, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_9.setPalette(palette)
        self.label_9.setObjectName(_fromUtf8('label_9'))
        self.storeButton = QtGui.QPushButton(self.centralwidget)
        self.storeButton.setGeometry(QtCore.QRect(350, 35, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.storeButton.setFont(font)
        self.storeButton.setObjectName(_fromUtf8('SessionManagerButton'))
        self.ExitButton = QtGui.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(471, 35, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ExitButton.setFont(font)
        self.ExitButton.setObjectName(_fromUtf8('ExitButton'))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(19, 129, 311, 331))
        self.groupBox.setTitle(_fromUtf8(''))
        self.groupBox.setObjectName(_fromUtf8('groupBox'))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox) # box for grades and range
        self.groupBox_3.setGeometry(QtCore.QRect(10, 228, 281, 60))
        self.groupBox_3.setTitle(_fromUtf8(''))
        self.groupBox_3.setObjectName(_fromUtf8('groupBox_3'))
        self.GradesandRanges_2 = QtGui.QRadioButton(self.groupBox_3)
        self.GradesandRanges_2.setGeometry(QtCore.QRect(43, 10, 150, 17))
        self.GradesandRanges_2.setChecked(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.GradesandRanges_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.GradesandRanges_2.setFont(font)
        self.GradesandRanges_2.setObjectName(_fromUtf8('GradesandRanges_2'))
        self.BandsandZones = QtGui.QRadioButton(self.groupBox_3)
        self.BandsandZones.setGeometry(QtCore.QRect(43, 30, 150, 17))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.BandsandZones.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.BandsandZones.setFont(font)
        self.BandsandZones.setObjectName(_fromUtf8('BandsandZones'))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(6, 7, 47, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_10.setPalette(palette)
        self.label_10.setObjectName(_fromUtf8('label_10'))
        #button
        self.BandsandZonesButton = QtGui.QPushButton(self.groupBox)
        self.BandsandZonesButton.setGeometry(QtCore.QRect(30, 300, 190, 23))
        self.BandsandZonesButton.setObjectName(_fromUtf8('BandsandZonesButton'))
        self.GradesandRangesButton = QtGui.QPushButton(self.groupBox)
        self.GradesandRangesButton.setGeometry(QtCore.QRect(30, 300, 190, 23))
        self.GradesandRangesButton.setObjectName(_fromUtf8('GradesandRangesButton'))
        self.BandsandZonesButton.setVisible(0)
        self.last_choise = False

        self.PolicyLinesButton = QtGui.QPushButton(self.groupBox)
        self.PolicyLinesButton.setGeometry(QtCore.QRect(30, 190, 190, 23))
        self.PolicyLinesButton.setObjectName(_fromUtf8('PolicyLinesButton'))
        self.CompensationMetricButton = QtGui.QPushButton(self.groupBox)
        self.CompensationMetricButton.setGeometry(QtCore.QRect(30, 161, 190, 23))
        self.CompensationMetricButton.setObjectName(_fromUtf8('CompensationMetricButton'))
        self.UpdateSurveyDataButton = QtGui.QPushButton(self.groupBox)
        self.UpdateSurveyDataButton.setGeometry(QtCore.QRect(30, 133, 190, 23))
        self.UpdateSurveyDataButton.setObjectName(_fromUtf8('UpdateSurveyDataButton'))
        self.CompaniesButton = QtGui.QPushButton(self.groupBox)
        self.CompaniesButton.setGeometry(QtCore.QRect(30, 103, 190, 23))
        self.CompaniesButton.setObjectName(_fromUtf8('CompaniesButton'))
        self.MatchiwthFastCatJobsButton = QtGui.QPushButton(self.groupBox)
        self.MatchiwthFastCatJobsButton.setGeometry(QtCore.QRect(30, 72, 190, 23))
        self.MatchiwthFastCatJobsButton.setObjectName(_fromUtf8('MatchiwthFastCatJobsButton'))
        self.labelList = {}
        self.BenchmarkJobsButton = QtGui.QPushButton(self.groupBox)
        self.BenchmarkJobsButton.setGeometry(QtCore.QRect(30, 42, 190, 23))
        self.BenchmarkJobsButton.setObjectName(_fromUtf8('BenchmarkJobsButton'))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(11, 0, 105, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_12.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8('label_12'))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(349, 129, 231, 331))
        self.groupBox_2.setTitle(_fromUtf8(''))
        self.groupBox_2.setObjectName(_fromUtf8('groupBox_2'))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(19, 0, 150, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_11.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8('label_11'))
        self.SalaryDataButton = QtGui.QPushButton(self.groupBox_2)
        self.SalaryDataButton.setGeometry(QtCore.QRect(40, 40, 150, 23))
        self.SalaryDataButton.setObjectName(_fromUtf8('SalaryDataButton'))
        self.RegressionButton = QtGui.QPushButton(self.groupBox_2)
        self.RegressionButton.setGeometry(QtCore.QRect(40, 70, 150, 23))
        self.RegressionButton.setObjectName(_fromUtf8('RegressionButton'))
        self.GradesDataButton = QtGui.QPushButton(self.groupBox_2)
        self.GradesDataButton.setGeometry(QtCore.QRect(40, 100, 150, 23))
        self.GradesDataButton.setObjectName(_fromUtf8('GradesDataButton'))
        self.GradesGraphButton = QtGui.QPushButton(self.groupBox_2)
        self.GradesGraphButton.setGeometry(QtCore.QRect(40, 130, 150, 23))
        self.GradesGraphButton.setObjectName(_fromUtf8('GradesGraphButton'))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(14, 249, 250, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_13.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8('label_13'))
        self.SalaryDataLabel = QtGui.QLabel(self.groupBox_2)
        self.SalaryDataLabel.setGeometry(QtCore.QRect(198, 45, 21, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.SalaryDataLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SalaryDataLabel.setFont(font)
        self.SalaryDataLabel.setObjectName(_fromUtf8('SalaryDataLabel'))
        self.RegressionLabel = QtGui.QLabel(self.groupBox_2)
        self.RegressionLabel.setGeometry(QtCore.QRect(198, 75, 21, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.RegressionLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RegressionLabel.setFont(font)
        self.RegressionLabel.setObjectName(_fromUtf8('RegressionLabel'))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName(_fromUtf8('menubar'))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8('statusbar'))
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QObject.connect(self.ExitButton, QtCore.SIGNAL(_fromUtf8('clicked()')), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.loadButton = QtGui.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(350, 58, 111, 23))
        self.loadButton.setFont(font)
        self.loadButton.setObjectName(_fromUtf8('resetButton'))
        self.dumpButton = QtGui.QPushButton(self.centralwidget)
        self.dumpButton.setGeometry(QtCore.QRect(350, 91, 111, 23))
        self.dumpButton.setFont(font)
        self.dumpButton.setObjectName(_fromUtf8('resetButton'))
        QtCore.QObject.connect(self.dumpButton, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.justPrintData())
        QtCore.QObject.connect(self.storeButton, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.storeSessionData(MainWindow))
        QtCore.QObject.connect(self.loadButton, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.loadSessionData(MainWindow))
        QtCore.QObject.connect(self.SalaryDataButton, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.reportSalaryData(MainWindow))
        QtCore.QObject.connect(self.RegressionButton, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.regression())
        QtCore.QObject.connect(self.GradesGraphButton, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.gradesGraph())
        QtCore.QObject.connect(self.GradesDataButton, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.gradesReport())
        self.doAllConnections(MainWindow)
        self.creatCheckMarkBoxes()
        self.creatCheckMarkBoxes()
        self.retranslateUi(MainWindow)
        self.dumpSessionData()
        QtCore.QObject.connect(self.GradesandRanges_2, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.dumpSessionData('isRange'))
        QtCore.QObject.connect(self.BandsandZones, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.dumpSessionData('isRange'))

    def creatCheckMarkBoxes(self):
        yList = sorted([45, 76, 106, 137, 193, 304, 165,304])
        self.checkBox = {}
        self.labelCounter = {}
        for name, y in zip(self.listofFileNames[:-1]+['BandsandZonesCode'], yList):
            box = QtGui.QCheckBox(self.groupBox)
            box.setText(_fromUtf8(''))
            box.setGeometry(QtCore.QRect(10, y, 17, 17))
            self.checkBox[name] = box
            label = QtGui.QLabel(self.groupBox) # show the numbers
            label.setGeometry(QtCore.QRect(230, y, 46, 16))
            font = QtGui.QFont()
            font.setPointSize(12)
            label.setFont(font)
            label.setObjectName(_fromUtf8(name))
            label.setText(QtGui.QApplication.translate('MainWindow', '', None, QtGui.QApplication.UnicodeUTF8))
            self.labelCounter[name] = label
        self.checkBox['BandsandZonesCode'].setVisible(0)
            

        return

    def doAllConnections(self, MainWindow):
        self.listOfCompanies = []
        listOfUIFiles = [
        BenchmarkJobsCode, MatchwithFastCatJobsCode, CompaniesCode,
        UpdateSurveyData, CompensationMetricCode, PolicyLinesCode,
        GradesandRangesCode, GradesandRangesCode]
        listofButtons = [self.BenchmarkJobsButton, self.MatchiwthFastCatJobsButton, self.CompaniesButton,
        self.UpdateSurveyDataButton, self.CompensationMetricButton, self.PolicyLinesButton,
        self.GradesandRangesButton, self.BandsandZonesButton]

        self.listofFileNames = map(lambda x: str(x).replace("'", '').split()[1], listOfUIFiles)
        self.myui = {}
        Dialog = {}
        for name, file, button in zip(self.listofFileNames, listOfUIFiles, listofButtons):
            self.bindButton(Dialog, button, file, name)

    def initializeDataForms(self, name):
        if name == 'MatchwithFastCatJobsCode':
            self.populateFastCat()
        userData = self.readTempSessionData()
        if name == 'GradesandRangesCode':
            if self.BandsandZones.isChecked():
                self.myui['GradesandRangesCode'].setGradeVSRange(1)
            else:
                self.myui['GradesandRangesCode'].setGradeVSRange(0)
            if (self.myui['GradesandRangesCode'].gradeNum) < 0 :
                self.myui['GradesandRangesCode'].populateGridLayout(0)
            else:
                self.myui['GradesandRangesCode'].populateGridLayout(self.myui['GradesandRangesCode'].gradeNum)
        self.myui[name].loadData(userData[name])

    def populateFastCat(self):
        userData = self.readTempSessionData()
        jobs = userData['BenchmarkJobsCode']
        if len(jobs) == 0:
            return
        self.myui['MatchwithFastCatJobsCode'].populateGridLayout(jobs)

    @pyqtSlot()
    def runQTDialog(self, dialog, name):
        self.initializeDataForms(name)
        dialog.exec_()
        if self.BandsandZones.isChecked() and name == 'GradesandRangesCode':
            self.checkBox['BandsandZonesCode'].setChecked(True)
        else:
            self.checkBox[name].setChecked(True)
        self.dumpSessionData(name)

    def bindButton(self, Dialog, button, file, name):
        Dialog[name] = QtGui.QDialog()
        self.myui[name] = file.Ui_Dialog()
        self.myui[name].setupUi(Dialog[name])
        QtCore.QObject.connect(button, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.runQTDialog(Dialog[name], name))

    def storeSessionData(self, MainWindow):
        userData = self.readTempSessionData()
        fileName = self.getInputTextDialog(MainWindow)
        if fileName == -1:
            return
        self.justPrintData()
        self.pickleStore(fileName, userData)

    def justPrintData(self):
        userData = self.readTempSessionData()
        for name in userData.keys():
            print name
            print userData[name]

        print '----------------------'

    def loadSessionData(self, MainWindow):
        while 1:
            fileName = self.getInputTextDialog(MainWindow)
            if fileName == -1:
                return
            try:
                fileObject = open(fileName, 'r')
                break
            except:
                QtGui.QMessageBox.critical(MainWindow, 'Error', 'File Not Found, try again!', QtGui.QMessageBox.Ok)

        userData = self.pickleLoad(fileName)
        self.pickleStore('sessionDefault', userData)
        for name, row in userData.iteritems():
            if name == 'isRange':
                self.GradesandRanges_2.setChecked(not userData[name])
                self.BandsandZones.setChecked(userData[name])
                continue
            elif name == 'last_choise':
                self.last_choise = not userData[name]
                continue
            self.checkBox[name].setChecked(True)
            self.labelCounter[name].setText(str(len(userData[name])))
        if self.BandsandZones.isChecked() != self.last_choise:
            if self.BandsandZones.isChecked():
                self.GradesandRangesButton.setVisible(0)
                self.checkBox["GradesandRangesCode"].setVisible(0)
                self.labelCounter["GradesandRangesCode"].setVisible(0)
                self.BandsandZonesButton.setVisible(1)
                self.checkBox["BandsandZonesCode"].setVisible(1)
                self.labelCounter["BandsandZonesCode"].setVisible(1)
                self.myui['GradesandRangesCode'].setGradeVSRange(1)
            else:
                self.GradesandRangesButton.setVisible(1)
                self.checkBox["GradesandRangesCode"].setVisible(1)
                self.labelCounter["GradesandRangesCode"].setVisible(1)
                self.BandsandZonesButton.setVisible(0)
                self.checkBox["BandsandZonesCode"].setVisible(0)
                self.labelCounter["BandsandZonesCode"].setVisible(0)
                self.myui['GradesandRangesCode'].setGradeVSRange(0)

    def getInputTextDialog(self, MainWindow):
        text, ok = QtGui.QInputDialog.getText(MainWindow, 'Enter File Name', 'Enter your file name:')
        if ok:
            fileName = str(text)
            return fileName
        return -1
        return fileName

    def readTempSessionData(self, name='sessionDefault'):
        file_Name = name
        userData = self.pickleLoad(file_Name)
        return userData

    def dumpSessionData(self, tableName=None):
        if tableName == None:
            userData = {name:self.myui[name].getUserData() for name in self.myui.keys()}
        else:
            userData = self.readTempSessionData()
            if tableName == 'isRange':
                userData['isRange'] = self.BandsandZones.isChecked()
            else:
                userData[tableName] = self.myui[tableName].getUserData()
                if tableName == 'GradesandRangesCode':
                    self.labelCounter['BandsandZonesCode'].setText(str(len(userData[tableName])))
                self.labelCounter[tableName].setText(str(len(userData[tableName])))
        userData['isRange'] = self.BandsandZones.isChecked()
        if self.BandsandZones.isChecked() != self.last_choise:
            if self.BandsandZones.isChecked():
                self.GradesandRangesButton.setVisible(0)
                self.checkBox["GradesandRangesCode"].setVisible(0)
                self.labelCounter["GradesandRangesCode"].setVisible(0)
                self.BandsandZonesButton.setVisible(1)
                self.checkBox["BandsandZonesCode"].setVisible(1)
                self.labelCounter["BandsandZonesCode"].setVisible(1)
                self.myui['GradesandRangesCode'].setGradeVSRange(1)
            else:
                self.GradesandRangesButton.setVisible(1)
                self.checkBox["GradesandRangesCode"].setVisible(1)
                self.labelCounter["GradesandRangesCode"].setVisible(1)
                self.BandsandZonesButton.setVisible(0)
                self.checkBox["BandsandZonesCode"].setVisible(0)
                self.labelCounter["BandsandZonesCode"].setVisible(0)
                self.myui['GradesandRangesCode'].setGradeVSRange(0)
        self.last_choise = self.BandsandZones.isChecked()
        userData['last_choise'] = self.last_choise
        file_Name = 'sessionDefault'
        self.pickleStore(file_Name, userData)
        return

    @QtCore.pyqtSlot()
    def reportSalaryData(self, MainWindow):
        item, ok = QtGui.QInputDialog.getItem(MainWindow, 'Reports', 'list of Reports', ('Detail', 'Summary', 'Both'), 0, False)
        if ok and item:
            self.defineVisulaizer()
            if item == 'Detail':
                self.myVis.printDetailedReport()
            elif item == 'Summary':
                self.myVis.printSummaryReport()
            else:
                self.myVis.printDetailedReport()
                self.myVis.printSummaryReport()
            QtGui.QMessageBox.information(MainWindow, 'Done', 'Your report is written in reports folder.', QtGui.QMessageBox.Ok)

    @QtCore.pyqtSlot()
    def regression(self):
        self.defineVisulaizer()
        self.myVis.drawRegressionLine()

    @QtCore.pyqtSlot()
    def gradesGraph(self):
        self.defineVisulaizer()
        if not self.GradesandRanges_2.isChecked():
            self.myVis.drawGradeRange()
        else:
            self.myVis.drawGradeGraph()

    @QtCore.pyqtSlot()
    def gradesReport(self):
        self.defineVisulaizer()
        self.myVis.reportGradeGraph()
        if not self.GradesandRanges_2.isChecked():
            self.myVis.reportRanges()
        messStr = 'Your report is written in reports/BandsData.html'
        if not self.GradesandRanges_2.isChecked():
            messStr = messStr + ' and reports/Bands&ZonesData.html'
        QtGui.QMessageBox.information(MainWindow, 'Done', messStr + '.', QtGui.QMessageBox.Ok)

    @QtCore.pyqtSlot()
    def defineVisulaizer(self):
        userData = self.readTempSessionData()
        self.myVis = visualizationManager.Visualizer(userData)
        self.myVis.queryndividuals()
        self.myVis.genCompensationMetrics()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate('MainWindow', 'MainWindow', None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate('MainWindow', 'Phase II Main Menu', None, QtGui.QApplication.UnicodeUTF8))
        self.storeButton.setText(QtGui.QApplication.translate('MainWindow', 'Store', None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setText(QtGui.QApplication.translate('MainWindow', 'Load', None, QtGui.QApplication.UnicodeUTF8))
        self.dumpButton.setText(QtGui.QApplication.translate('MainWindow', 'Check Data', None, QtGui.QApplication.UnicodeUTF8))
        self.ExitButton.setText(QtGui.QApplication.translate('MainWindow', 'Exit', None, QtGui.QApplication.UnicodeUTF8))
        self.GradesandRanges_2.setText(QtGui.QApplication.translate('MainWindow', 'Grades and Ranges', None, QtGui.QApplication.UnicodeUTF8))
        self.BandsandZones.setText(QtGui.QApplication.translate('MainWindow', 'Bands and Zones', None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate('MainWindow', 'Use:', None, QtGui.QApplication.UnicodeUTF8))
        self.GradesandRangesButton.setText(QtGui.QApplication.translate('MainWindow', 'Grades and Ranges', None, QtGui.QApplication.UnicodeUTF8))
        self.BandsandZonesButton.setText(QtGui.QApplication.translate('MainWindow', 'Bands and Zones', None, QtGui.QApplication.UnicodeUTF8))
        self.PolicyLinesButton.setText(QtGui.QApplication.translate('MainWindow', 'Policy Lines', None, QtGui.QApplication.UnicodeUTF8))
        self.CompensationMetricButton.setText(QtGui.QApplication.translate('MainWindow', 'Compensation Metric', None, QtGui.QApplication.UnicodeUTF8))
        self.UpdateSurveyDataButton.setText(QtGui.QApplication.translate('MainWindow', 'Update Survey Data', None, QtGui.QApplication.UnicodeUTF8))
        self.CompaniesButton.setText(QtGui.QApplication.translate('MainWindow', 'Companies', None, QtGui.QApplication.UnicodeUTF8))
        self.MatchiwthFastCatJobsButton.setText(QtGui.QApplication.translate('MainWindow', 'Match with FastCat Jobs', None, QtGui.QApplication.UnicodeUTF8))
        self.BenchmarkJobsButton.setText(QtGui.QApplication.translate('MainWindow', 'Benchmark Jobs', None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate('MainWindow', 'Select Data', None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate('MainWindow', 'View and Print', None, QtGui.QApplication.UnicodeUTF8))
        self.SalaryDataButton.setText(QtGui.QApplication.translate('MainWindow', 'Salary Data', None, QtGui.QApplication.UnicodeUTF8))
        self.RegressionButton.setText(QtGui.QApplication.translate('MainWindow', 'Regression', None, QtGui.QApplication.UnicodeUTF8))
        self.GradesDataButton.setText(QtGui.QApplication.translate('MainWindow', 'Grades Data', None, QtGui.QApplication.UnicodeUTF8))
        self.GradesGraphButton.setText(QtGui.QApplication.translate('MainWindow', 'Grades Graph', None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate('MainWindow', 'Note: The Regression \nand Grades Graph may \ntake time to Calculate.', None, QtGui.QApplication.UnicodeUTF8))
        self.SalaryDataLabel.setText(QtGui.QApplication.translate('MainWindow', '0', None, QtGui.QApplication.UnicodeUTF8))
        self.RegressionLabel.setText(QtGui.QApplication.translate('MainWindow', '0', None, QtGui.QApplication.UnicodeUTF8))
        return


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# okay decompiling NewSession.pyc

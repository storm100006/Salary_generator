# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: CompaniesCode.py
from PyQt4 import QtCore, QtGui
from abc import abstractmethod, ABCMeta
import pandas as pd
from myGUISupperClasses import myBasicFormSuperClass, myGUIdataBaseTableSuperClass
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(myBasicFormSuperClass, myGUIdataBaseTableSuperClass):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8('Dialog'))
        Dialog.resize(1200, 800)
        self.BenchmarJobs = QtGui.QLabel(Dialog)
        self.BenchmarJobs.setGeometry(QtCore.QRect(0, 0, 651, 85))
        self.BenchmarJobs.setText(_fromUtf8(''))
        self.BenchmarJobs.setObjectName(_fromUtf8('BenchmarJobs'))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 85, 650, 415))
        self.label.setText(_fromUtf8(''))
        self.label.setObjectName(_fromUtf8('label'))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 16, 200, 30))
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
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.DoneButton = QtGui.QPushButton(Dialog)
        self.DoneButton.setGeometry(QtCore.QRect(550, 10, 75, 23))
        self.DoneButton.setObjectName(_fromUtf8('DoneButton'))
        self.TableofContents = QtGui.QTableView(Dialog)
        self.TableofContents.setGeometry(QtCore.QRect(5, 85, 640, 391))
        self.TableofContents.setObjectName(_fromUtf8('TableofContents'))
        self.retranslateUi(Dialog)
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtCore.Qt.gray)
        self.BenchmarJobs.setAutoFillBackground(True)
        self.BenchmarJobs.setPalette(pal)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.resizeEvent = lambda event: self.onResize(Dialog, event)
        self.fillTheTable(CSVfileName='tblCompanyInfo.csv', columns=[
         'CompanyID', 'Industry', 'Size', 'ROA', 'TotalSales1000s', 'BaseSalaryDivTotalComp', 'BenefitsDivBaseSalary', 'StockOptionsDivBaseSalary', 'BonusDivBaseSalary', 'Description'], toc=self.TableofContents)
        self.doButtonConnections(Dialog, self.DoneButton)

    def onResize(self, Dialog, event):
        size = Dialog.size()
        self.TableofContents.resize(size.width() - 5, size.height() - 85 - 10)
        self.TableofContents.resizeColumnsToContents()
        self.BenchmarJobs.setGeometry(QtCore.QRect(0, 0, size.width(), 185))
        self.DoneButton.setGeometry(QtCore.QRect(size.width() - 80, 16, 75, 23))

    def loadData(self, loaded):
        self.userData = loaded
        indexList = self.userData.index.values.tolist()
        self.TableofContents.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        for i in indexList:
            self.TableofContents.selectRow(i)

        self.TableofContents.setSelectionBehavior(QtGui.QTableView.SelectRows)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate('Dialog', 'Dialog', None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate('Dialog', 'Select Companies', None, QtGui.QApplication.UnicodeUTF8))
        self.DoneButton.setText(QtGui.QApplication.translate('Dialog', 'Done', None, QtGui.QApplication.UnicodeUTF8))
        return

    def translateUserData(self):
        return self.getSelectedRowsValue(self.TableofContents)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
# okay decompiling CompaniesCode.pyc

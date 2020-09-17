# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: MatchwithFastCatJobsCode.py
from PyQt4 import QtCore, QtGui
from abc import abstractmethod, ABCMeta
import pandas as pd
from myGUISupperClasses import myBasicFormSuperClass, myGridLayoutSuperClass
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(myBasicFormSuperClass, myGridLayoutSuperClass):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8('Dialog'))
        Dialog.resize(600, 400)
        Dialog.setMinimumSize(QtCore.QSize(600, 400))
        Dialog.setMaximumSize(QtCore.QSize(600, 400))
        self.jobRows = QtGui.QLabel(Dialog)
        self.jobRows.setGeometry(QtCore.QRect(0, 0, 600, 100))
        self.jobRows.setText(_fromUtf8(''))
        self.jobRows.setPixmap(QtGui.QPixmap(_fromUtf8('LightGray.png')))
        self.jobRows.setObjectName(_fromUtf8('label'))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 600, 450))
        self.label_2.setText(_fromUtf8(''))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8('DarkGray.png')))
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.DoneButton = QtGui.QPushButton(Dialog)
        self.DoneButton.setGeometry(QtCore.QRect(500, 10, 80, 30))
        self.DoneButton.setObjectName(_fromUtf8('DoneButton'))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 5, 280, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8('label_3'))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.doButtonConnections(Dialog, self.DoneButton)
        self.createGridLayout(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate('Dialog', 'Dialog', None, QtGui.QApplication.UnicodeUTF8))
        self.DoneButton.setText(QtGui.QApplication.translate('Dialog', 'Done', None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate('Dialog', 'Assigning Job Evaluation Points', None, QtGui.QApplication.UnicodeUTF8))
        return

    def populateGridLayout(self, df):
        self.df = df
        QtGuifastCatJobs = list(pd.read_csv('tblFastCatJobs.csv')['JobTitle'].values)
        self.deleteAllInGrid()
        for i, row in df.iterrows():
            combo = QtGui.QComboBox()
            combo.addItems(QtGuifastCatJobs)
            gePoint = QtGui.QLineEdit()
            label_ID = QtGui.QLabel(_fromUtf8(str(row['JobID'])))
            label_name = QtGui.QLabel(_fromUtf8(row['Name']))
            label_index = QtGui.QLabel(_fromUtf8(str(i)))
            self.grid.addWidget(gePoint, *(i, 3))
            self.grid.addWidget(label_index, *(i, 0))
            self.grid.addWidget(label_ID, *(i, 1))
            self.grid.addWidget(label_name, *(i, 2))
            self.grid.addWidget(combo, *(i, 4))

    def loadData(self, loaded):
        if len(loaded) == 0:
            return
        assert len(loaded) is self.grid.rowCount(), ('"FAST CAT MATCH SIZE MISMATCH {1} {0}').format(len(loaded), self.grid.rowCount())
        for i, row in loaded.iterrows():
            self.grid.itemAtPosition(i, 3).widget().setText(_fromUtf8(str(row['JEpoint'])))
            index = self.grid.itemAtPosition(i, 4).widget().findText(row['fastCatEQ'], QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.grid.itemAtPosition(i, 4).widget().setCurrentIndex(index)

    def translateUserData(self):
        return pd.DataFrame(map(lambda i: {'JEpoint': self.readTextInputNumber(self.grid.itemAtPosition(i, 3).widget()), 'Job': str(self.grid.itemAtPosition(i, 2).widget().text()), 
           'JobID': float(self.grid.itemAtPosition(i, 1).widget().text()), 
           'fastCatEQ': str(self.grid.itemAtPosition(i, 4).widget().currentText())}, range(len(self.df))))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
# okay decompiling MatchwithFastCatJobsCode.pyc

# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Ui_range.py
from PyQt4 import QtCore, QtGui
from myGUISupperClasses import myBasicFormSuperClass, myGridLayoutSuperClass
import pandas as pd
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_range(QtGui.QDialog, myGridLayoutSuperClass):

    def __init__(self, index=0):
        super(Ui_range, self).__init__()
        self.createBasicLook(index)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.createGridLayout(self)
        self.setupGradeSizeCombo()

    def createBasicLook(self, index):
        self.setObjectName(_fromUtf8('Dialog'))
        self.resize(600, 425)
        label = QtGui.QLabel(self)
        label.setGeometry(QtCore.QRect(0, 0, 601, 61))
        label.setText(_fromUtf8(''))
        label.setPixmap(QtGui.QPixmap(_fromUtf8('/LightGray.png')))
        label.setObjectName(_fromUtf8('label'))
        label_2 = QtGui.QLabel(self)
        label_2.setGeometry(QtCore.QRect(0, 61, 601, 364))
        label_2.setText(_fromUtf8(''))
        label_2.setPixmap(QtGui.QPixmap(_fromUtf8('/DarkGray.png')))
        label_2.setObjectName(_fromUtf8('label_2'))
        label_3 = QtGui.QLabel(self)
        label_3.setGeometry(QtCore.QRect(10, 4, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        label_3.setFont(font)
        label_3.setObjectName(_fromUtf8('label_3'))
        DoneButton = QtGui.QPushButton(self)
        DoneButton.setGeometry(QtCore.QRect(520, 10, 75, 23))
        DoneButton.setObjectName(_fromUtf8('DoneButton'))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setWindowTitle(QtGui.QApplication.translate('Dialog', 'Dialog', None, QtGui.QApplication.UnicodeUTF8))
        label_3.setText(QtGui.QApplication.translate('Dialog', 'Zone ' + str(index), None, QtGui.QApplication.UnicodeUTF8))
        DoneButton.setText(QtGui.QApplication.translate('Dialog', 'Done', None, QtGui.QApplication.UnicodeUTF8))
        QtCore.QObject.connect(DoneButton, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.updateTheUserData_action())
        return

    def setupGradeSizeCombo(self):
        self.grid.addWidget(QtGui.QLabel('Number of Zones'), 0, 0, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel(''), 0, 2, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel(''), 0, 3, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel(''), 0, 4, QtCore.Qt.AlignTop)
        comboBox = QtGui.QComboBox()
        comboBox.addItems([''] + map(str, range(1, 20)))
        self.grid.addWidget(comboBox, 0, 1, QtCore.Qt.AlignTop)
        self.grid.itemAtPosition(0, 1).widget().currentIndexChanged.connect(self.populateGridLayout)

    @QtCore.pyqtSlot()
    def populateGridLayout(self, text=-1):
        if text == -1:
            text = self.grid.itemAtPosition(0, 1).widget().currentText()
        self.deleteAllInGrid(exclude=[0])
        self.populateGridHeader()
        self.gradeNum = (lambda x: int(x) if x != '' else 0)(text)
        if self.gradeNum == 0:
            return
        self.populateGridHeader()
        for i in range(2, 2 + self.gradeNum):
            label = QtGui.QLabel(_fromUtf8(str(i - 1)))
            self.grid.addWidget(QtGui.QLineEdit(), i, 1, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLineEdit(), i, 2, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLineEdit(), i, 3, QtCore.Qt.AlignTop)
            self.grid.addWidget(label, i, 0, QtCore.Qt.AlignTop)

    def populateGridHeader(self):
        self.grid.setRowStretch(20, 20)
        self.grid.addWidget(QtGui.QLabel('Zone #'), 1, 0, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel('JE Point'), 1, 1, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel('Min Value'), 1, 2, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel('Max value'), 1, 3, QtCore.Qt.AlignTop)

    def exec_(self, data=pd.DataFrame()):
        self.userData = pd.DataFrame()
        self.loadData(data)
        QtGui.QDialog.exec_(self)
        return self.userData

    def translateUserData(self):
        if self.gradeNum == -1:
            return pd.DataFrame()
        return pd.DataFrame(map(lambda x: {'ID': x - 1, 'JE Point': self.readTextInputNumber(self.grid.itemAtPosition(x, 1).widget()),
           'Min': self.readTextInputNumber(self.grid.itemAtPosition(x, 2).widget()), 
           'Max': self.readTextInputNumber(self.grid.itemAtPosition(x, 3).widget())}, range(2, self.gradeNum + 2)))

    def readTextInputNumber(self, value):
        text = value.text()
        return float(text if text != '' else '0')

    def loadData(self, data):
        self.grid.itemAtPosition(0, 1).widget().setCurrentIndex(len(data))
        for index, row in data.iterrows():
            i = index + 2
            self.grid.itemAtPosition(i, 2).widget().setText(_fromUtf8(str(row['Min'])))
            self.grid.itemAtPosition(i, 1).widget().setText(_fromUtf8(str(row['JE Point'])))
            self.grid.itemAtPosition(i, 3).widget().setText(_fromUtf8(str(row['Max'])))

    @QtCore.pyqtSlot()
    def updateTheUserData_action(self):
        self.userData = self.translateUserData()
        self.close()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = Ui_range()
    a = Dialog.exec_()
    print a
# okay decompiling Ui_range.pyc

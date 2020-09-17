# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: CompensationMetricCode.py
from PyQt4 import QtCore, QtGui
from myGUISupperClasses import myBasicFormSuperClass, myGUIdataBaseTableSuperClass
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(myBasicFormSuperClass, myGUIdataBaseTableSuperClass):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8('Dialog'))
        Dialog.resize(400, 250)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 40))
        self.label.setText(_fromUtf8(''))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8('LightGray.png')))
        self.label.setObjectName(_fromUtf8('label'))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 400, 210))
        self.label_2.setText(_fromUtf8(''))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8('DarkGray.png')))
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 4, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8('label_3'))
        self.DoneButton = QtGui.QPushButton(Dialog)
        self.DoneButton.setGeometry(QtCore.QRect(310, 8, 75, 23))
        self.DoneButton.setObjectName(_fromUtf8('DoneButton'))
        self.ListofContents = QtGui.QTableView(Dialog)
        self.ListofContents.setGeometry(QtCore.QRect(5, 46, 390, 200))
        self.ListofContents.setObjectName(_fromUtf8('ListofContents'))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.fillTheTable(CSVfileName='tblCompensationMetric.csv', columns=[
         'CompensationMetric'], toc=self.ListofContents)
        self.doButtonConnections(Dialog, self.DoneButton, None, None)
        self.ListofContents.setSelectionBehavior(QtGui.QTableView.SelectRows)
        return

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate('Dialog', 'Dialog', None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate('Dialog', 'Select Compensation Metric', None, QtGui.QApplication.UnicodeUTF8))
        self.DoneButton.setText(QtGui.QApplication.translate('Dialog', 'Done', None, QtGui.QApplication.UnicodeUTF8))
        return

    def translateUserData(self):
        return self.getSelectedRowsValue(self.ListofContents)

    def loadData(self, loaded):
        if len(loaded) <= 0:
            return
        self.userData = loaded
        index = self.userData.index.values.tolist()[0]
        self.ListofContents.selectRow(index)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
# okay decompiling CompensationMetricCode.pyc

# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: PolicyLinesCode.py
from PyQt4 import QtCore, QtGui
import pandas as pd
from myGUISupperClasses import myBasicFormSuperClass
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(myBasicFormSuperClass):

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8('Dialog'))
        Dialog.resize(380, 250)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 380, 40))
        self.label.setText(_fromUtf8(''))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8('./LightGray.png')))
        self.label.setObjectName(_fromUtf8('label'))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 380, 211))
        self.label_2.setText(_fromUtf8(''))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8('./DarkGray.png')))
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 4, 170, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8('label_3'))
        self.DoneButton = QtGui.QPushButton(Dialog)
        self.DoneButton.setGeometry(QtCore.QRect(290, 10, 75, 23))
        self.DoneButton.setObjectName(_fromUtf8('DoneButton'))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 52, 360, 51))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8('line'))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 140, 360, 51))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8('line_2'))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 143, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8('label_4'))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 55, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8('label_5'))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 87, 360, 20))
        self.label_6.setObjectName(_fromUtf8('label_6'))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 177, 360, 20))
        self.label_7.setObjectName(_fromUtf8('label_7'))
        self.PolicyOneValue = QtGui.QLineEdit(Dialog)
        self.PolicyOneValue.setGeometry(QtCore.QRect(11, 115, 70, 20))
        self.PolicyOneValue.setObjectName(_fromUtf8('PolicyOneValue'))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(85, 119, 46, 13))
        self.label_8.setObjectName(_fromUtf8('label_8'))
        self.checkBoxforPolicy1 = QtGui.QCheckBox(Dialog)
        self.checkBoxforPolicy1.setGeometry(QtCore.QRect(121, 116, 200, 17))
        self.checkBoxforPolicy1.setObjectName(_fromUtf8('checkBoxforPolicy1'))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(85, 206, 46, 13))
        self.label_9.setObjectName(_fromUtf8('label_9'))
        self.checkBoxforPolicy2 = QtGui.QCheckBox(Dialog)
        self.checkBoxforPolicy2.setGeometry(QtCore.QRect(121, 203, 200, 17))
        self.checkBoxforPolicy2.setObjectName(_fromUtf8('checkBoxforPolicy2'))
        self.PolicyTwoValue = QtGui.QLineEdit(Dialog)
        self.PolicyTwoValue.setGeometry(QtCore.QRect(11, 202, 70, 20))
        self.PolicyTwoValue.setObjectName(_fromUtf8('PolicyTwoValue'))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.doButtonConnections(Dialog, self.DoneButton, None, None)
        return

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate('Dialog', 'Dialog', None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate('Dialog', 'Select Policy Lines', None, QtGui.QApplication.UnicodeUTF8))
        self.DoneButton.setText(QtGui.QApplication.translate('Dialog', 'Done', None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate('Dialog', 'Policy 2', None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate('Dialog', 'Policy 1', None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate('Dialog', 'Enter a percentage above or below the market Line for Policy 1', None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate('Dialog', 'Enter a percentage above or below the market Line for Policy 2', None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate('Dialog', '%', None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxforPolicy1.setText(QtGui.QApplication.translate('Dialog', 'Display Policy Line 1 on Graphs', None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate('Dialog', '%', None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxforPolicy2.setText(QtGui.QApplication.translate('Dialog', 'Display Policy Line 2 on Graphs', None, QtGui.QApplication.UnicodeUTF8))
        return

    def translateUserData(self):
        return pd.DataFrame([
         {'Display': self.checkBoxforPolicy1.isChecked(), 'Percent': self.readTextInputNumber(self.PolicyOneValue), 
            'Name': 'Policy1'},
         {'Display': self.checkBoxforPolicy2.isChecked(), 'Percent': self.readTextInputNumber(self.PolicyTwoValue), 
            'Name': 'Policy2'}])

    def loadData(self, loaded):
        if len(loaded) <= 0:
            return
        self.checkBoxforPolicy1.setChecked(loaded.get_value(0, 'Display'))
        self.checkBoxforPolicy2.setChecked(loaded.get_value(1, 'Display'))
        self.PolicyOneValue.setText(_fromUtf8(str(loaded.get_value(0, 'Percent'))))
        self.PolicyTwoValue.setText(_fromUtf8(str(loaded.get_value(1, 'Percent'))))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
# okay decompiling PolicyLinesCode.pyc

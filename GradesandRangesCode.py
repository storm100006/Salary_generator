# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: GradesandRangesCode.py
from PyQt4 import QtCore, QtGui
from myGUISupperClasses import myBasicFormSuperClass, myGridLayoutSuperClass
import pandas as pd, Ui_range, copy
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(myBasicFormSuperClass, myGridLayoutSuperClass):
    isRange = False
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8('Dialog'))
        Dialog.resize(600, 425)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 61))
        self.label.setText(_fromUtf8(''))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8('LightGray.png')))
        self.label.setObjectName(_fromUtf8('label'))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 61, 601, 364))
        self.label_2.setText(_fromUtf8(''))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8('DarkGray.png')))
        self.label_2.setObjectName(_fromUtf8('label_2'))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 4, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8('label_3'))
        self.DoneButton = QtGui.QPushButton(Dialog)
        self.DoneButton.setGeometry(QtCore.QRect(500, 10, 75, 23))
        self.DoneButton.setObjectName(_fromUtf8('DoneButton'))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.gradeNum = -1
        self.doButtonConnections(Dialog, self.DoneButton)
        self.createGridLayout(Dialog)
        self.setupGradeSizeCombo()
        self.rangeData = {}

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate('Dialog', 'Dialog', None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate('Dialog', 'Grades and Ranges', None, QtGui.QApplication.UnicodeUTF8))
        self.DoneButton.setText(QtGui.QApplication.translate('Dialog', 'Done', None, QtGui.QApplication.UnicodeUTF8))
        return

    def translateUserData(self):
        if self.gradeNum == -1:
            return pd.DataFrame()
        return {'grade': pd.DataFrame(map(lambda x: {'ID': x - 1, 'GEmin': self.readTextInputNumber(self.grid.itemAtPosition(x, 1).widget()), 
                     'GEmax': self.readTextInputNumber(self.grid.itemAtPosition(x, 2).widget()), 
                     'range': self.readTextInputNumber(self.grid.itemAtPosition(x, 3).widget()), 
                     'policy': str(self.grid.itemAtPosition(x, 4).widget().currentText())}, range(2, self.gradeNum + 2))), 
           'range': self.rangeData}

    def setupGradeSizeCombo(self):
        try:
            self.grid.itemAtPosition(0, 0).widget().deleteLater()
            print("delete")
        except:
            pass
        self.grid.addWidget(QtGui.QLabel(''), 0, 0, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel(''), 0, 2, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel(''), 0, 3, QtCore.Qt.AlignTop)
        self.grid.addWidget(QtGui.QLabel(''), 0, 4, QtCore.Qt.AlignTop)
        if self.isRange:
            self.grid.addWidget(QtGui.QLabel(''), 0, 5, QtCore.Qt.AlignTop)
        comboBox = QtGui.QComboBox()
        comboBox.addItems([''] + map(str, range(1, 20)))
        self.grid.addWidget(comboBox, 0, 1, QtCore.Qt.AlignTop)
        self.grid.itemAtPosition(0, 1).widget().currentIndexChanged.connect(self.populateGridLayout)

    def loadData(self, data):
        if len(data) <= 0:
            return
        loaded = data['grade']
        self.grid.itemAtPosition(0, 1).widget().setCurrentIndex(len(loaded))
        for index, row in loaded.iterrows():
            i = index + 2
            self.grid.itemAtPosition(i, 1).widget().setText(_fromUtf8(str(row['GEmin'])))
            self.grid.itemAtPosition(i, 2).widget().setText(_fromUtf8(str(row['GEmax'])))
            self.grid.itemAtPosition(i, 3).widget().setText(_fromUtf8(str(row['range'])))
            index = self.grid.itemAtPosition(i, 4).widget().findText(row['policy'], QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.grid.itemAtPosition(i, 4).widget().setCurrentIndex(index)
        if self.rangeData != None and data['range'] == dict():
            pass
        else:
            self.rangeData = data['range']

    @QtCore.pyqtSlot()
    def populateGridLayout(self, text):
        self.deleteAllInGrid(exclude=[0])
        self.populateGridHeader()
        self.gradeNum = (lambda x: int(x) if x != '' else 0)(self.grid.itemAtPosition(0, 1).widget().itemText(text))
        if self.gradeNum == 0:
            return
        self.populateGridHeader()
        for i in range(2, 2 + self.gradeNum):
            label = QtGui.QLabel(_fromUtf8(str(i - 1)))
            combo = QtGui.QComboBox()
            combo.addItems(['Base', 'Policy1', 'Policy2'])
            self.grid.addWidget(QtGui.QLineEdit(), i, 1, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLineEdit(), i, 2, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLineEdit(), i, 3, QtCore.Qt.AlignTop)
            self.grid.addWidget(label, i, 0, QtCore.Qt.AlignTop)
            self.grid.addWidget(combo, i, 4, QtCore.Qt.AlignTop)
            if self.isRange:
                index = copy.deepcopy(i - 2)
                self.grid.addWidget(QtGui.QPushButton('zones'), i, 5, QtCore.Qt.AlignTop)
                QtCore.QObject.connect(self.grid.itemAtPosition(i, 5).widget(), QtCore.SIGNAL(_fromUtf8('clicked()')), lambda x=index: self.rangeBottun(x))
                self.rangeData[index] = pd.DataFrame()

    @QtCore.pyqtSlot()
    def rangeBottun(self, index):
        rangeDialog = Ui_range.Ui_range(index + 1)
        output = rangeDialog.exec_(data=self.rangeData[index])
        self.rangeData[index] = output

    def setGradeVSRange(self, isGrade):
        self.isRange = isGrade

    def populateGridHeader(self):
        self.grid.setRowStretch(20, 20)
        try:
            self.grid.itemAtPosition(1, 0).widget().deleteLater()
            self.grid.itemAtPosition(2, 0).widget().deleteLater()
            self.grid.itemAtPosition(3, 0).widget().deleteLater()
            self.grid.itemAtPosition(4, 0).widget().deleteLater()
            self.grid.itemAtPosition(5, 0).widget().deleteLater()
        except:
            pass
        if self.isRange:
            self.grid.itemAtPosition(0, 0).widget().setText(QtGui.QApplication.translate('Dialog', 'Number of Bands', None, QtGui.QApplication.UnicodeUTF8))
            self.grid.addWidget(QtGui.QLabel('Band #'), 1, 0, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLabel('Lower JE Points'), 1, 1, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLabel('Upper JE Points'), 1, 2, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLabel('Range\n(%over/under mid)'), 1, 3, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLabel('Policy'), 1, 4, QtCore.Qt.AlignTop)
            self.label_3.setText(QtGui.QApplication.translate('Dialog', 'Bands and Zones', None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.grid.itemAtPosition(0, 0).widget().setText(QtGui.QApplication.translate('Dialog', 'Number of Grades', None, QtGui.QApplication.UnicodeUTF8))
            self.grid.addWidget(QtGui.QLabel('Grade #'), 1, 0, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLabel('Lower JE Points'), 1, 1, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLabel('Upper JE Points'), 1, 2, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLabel('Range\n(%over/under mid)'), 1, 3, QtCore.Qt.AlignTop)
            self.grid.addWidget(QtGui.QLabel('Policy'), 1, 4, QtCore.Qt.AlignTop)
            self.label_3.setText(QtGui.QApplication.translate('Dialog', 'Grades and Ranges', None, QtGui.QApplication.UnicodeUTF8))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
# okay decompiling GradesandRangesCode.pyc

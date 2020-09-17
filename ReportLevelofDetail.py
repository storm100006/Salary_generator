# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Report Level of Detail.ui'
#
# Created: Tue Feb 07 15:19:14 2017
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(400, 200)
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("DarkGray.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 5, 381, 190))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 360, 70))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 81, 140, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.groupBox_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.Summary = QtGui.QRadioButton(self.groupBox_2)
        self.Summary.setGeometry(QtCore.QRect(10, 22, 82, 17))
        self.Summary.setObjectName(_fromUtf8("Summary"))
        self.Detail = QtGui.QRadioButton(self.groupBox_2)
        self.Detail.setGeometry(QtCore.QRect(10, 48, 82, 17))
        self.Detail.setObjectName(_fromUtf8("Detail"))
        self.Both = QtGui.QRadioButton(self.groupBox_2)
        self.Both.setGeometry(QtCore.QRect(10, 76, 82, 17))
        self.Both.setObjectName(_fromUtf8("Both"))
        self.PreviewButton = QtGui.QPushButton(self.groupBox)
        self.PreviewButton.setGeometry(QtCore.QRect(234, 113, 130, 25))
        self.PreviewButton.setObjectName(_fromUtf8("PreviewButton"))
        self.CancelButton = QtGui.QPushButton(self.groupBox)
        self.CancelButton.setGeometry(QtCore.QRect(233, 143, 130, 25))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QtGui.QApplication.translate("dialog", "Report Level of Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dialog", "Select whether you like to view Summary (statistics only) or\n"
"Detail information for the selected jobs. NOTE: This report \n"
"takes a minute or two to run.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("dialog", "Select Level of Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.Summary.setText(QtGui.QApplication.translate("dialog", "Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.Detail.setText(QtGui.QApplication.translate("dialog", "Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.Both.setText(QtGui.QApplication.translate("dialog", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.PreviewButton.setText(QtGui.QApplication.translate("dialog", "Preview...", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelButton.setText(QtGui.QApplication.translate("dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dialog = QtGui.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())


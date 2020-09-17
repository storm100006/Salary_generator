# Python bytecode 2.7 (62211)
# Embedded file name: BenefitsPercentage.py
from PyQt4 import QtCore, QtGui
import pandas as pd
from os import listdir
from os.path import getmtime
import time

class SessionLoader(QtGui.QDialog):
    def __init__(self):
        super(SessionLoader, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(245, 300)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText(QtCore.QString("Select a session :"))
        self.button = QtGui.QPushButton(self)
        self.button.setGeometry(self.width()-100, 10, 90, 30)
        self.button.setText(QtCore.QString("Select"))
        self.fileTable = QtGui.QTableView(self)
        self.fileTable.setGeometry(QtCore.QRect(10, 50, self.width()-20, self.height()-70))

        self.fileList = self.getSessionList()
        df = pd.DataFrame(self.fileList, columns = ["Session Name", "Last Modified"])
        self.fileTable.setModel(PandasModel(df))
        self.fileTable.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.fileTable.resizeColumnsToContents()
        self.fileTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        self.button.clicked.connect(lambda: self.close())
        self.fileTable.clicked.connect(self.fileSelected)
        self.fileTable.doubleClicked.connect(self.fileDoubleClicked)

    def fileSelected(self, index):
        fileData = self.fileList[index.row()]
        self.selectedFileName = fileData[0]

    def fileDoubleClicked(self, index):
        fileData = self.fileList[index.row()]
        self.selectedFileName = fileData[0]
        self.close()

    def getSelectedFileName(self):
        return self.selectedFileName

    def getSessionList(self):
        path = 'SessionFiles'
        sessionFiles = [f for f in listdir(path) if f != "sessionDefault"]
        times = [self.lastModifiedTime(fileName) for fileName in sessionFiles]
        return zip(sessionFiles, times)

    def lastModifiedTime(self, fileName):
        mtime = getmtime('SessionFiles/{}'.format(fileName))
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))

class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return

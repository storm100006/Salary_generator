# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: myGUISupperClasses.py
from PyQt4 import QtCore, QtGui
from abc import abstractmethod, ABCMeta
from baseUtils import baseUtils
import pandas as pd
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class myGUIdataBaseTableSuperClass(baseUtils):

    def getSelectedRowsIndex(self, toc):
        indecies = toc.selectedIndexes()
        if len(indecies) == 0:
            return pd.DataFrame()
        return pd.Series(map(lambda x: x.row(), indecies)).drop_duplicates().reset_index(drop=True).T

    def fillTheTable(self, CSVfileName, columns, toc):
        df = pd.read_csv(CSVfileName)
        self.cleanColumnNames(df)
        df = df[columns]
        self.df = df
        toc.resizeColumnsToContents()
        model = PandasModel(df)
        toc.setModel(model)
        toc.resizeColumnsToContents()
        toc.setAlternatingRowColors(True)
        toc.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        QtCore.QObject.connect(toc, QtCore.SIGNAL(_fromUtf8('clicked()')), self.viewClicked)

    @QtCore.pyqtSlot()
    def viewClicked(self, clickedIndex):
        row = clickedIndex.row()
        self.TableofContents.selectRow(row)
        print row

    def getSelectedRowsValue(self, toc):
        rows = self.getSelectedRowsIndex(toc)
        return self.df.iloc[rows].reset_index(drop=True)


class myBasicFormSuperClass(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.userData = pd.DataFrame()

    @abstractmethod
    def loadData(self, loaded):
        print 'Abstract'

    @abstractmethod
    def translateUserData(self):
        pass

    @QtCore.pyqtSlot()
    def updateTheUserData_action(self, Dialog):
        self.userData = self.translateUserData()
        Dialog.close()

    def doButtonConnections(self, Dialog, done, selectAll=None, unselectAll=None):
        self.userData = pd.DataFrame()
        QtCore.QObject.connect(done, QtCore.SIGNAL(_fromUtf8('clicked()')), lambda : self.updateTheUserData_action(Dialog))

    def getUserData(self):
        return self.userData

    def readTextInputNumber(self, value):
        text = value.text()
        return float(text if text != '' else '0')


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


class myGridLayoutSuperClass:

    def createGridLayout(self, Dialog):
        scroll = QtGui.QScrollArea(Dialog)
        size = Dialog.size()
        scroll.setGeometry(QtCore.QRect(0, 50, size.width() - 5, size.height() - 50))
        scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        viewport = QtGui.QWidget(Dialog)
        scroll.setWidget(viewport)
        scroll.setWidgetResizable(True)
        self.grid = QtGui.QGridLayout(viewport)
        viewport.setLayout(self.grid)

    @abstractmethod
    def populateGridLayout(self, df):
        pass

    def deleteAllInGrid(self, exclude=[]):
        if self.grid.rowCount() == 1:
            return
        for i in range(self.grid.rowCount()):
            if i in exclude:
                continue
            for j in range(self.grid.columnCount()):
                x = self.grid.itemAtPosition(i, j)
                if x:
                    if x.widget():
                        x.widget().deleteLater()
                        x.widget().setParent(None)

        return
# okay decompiling myGUISupperClasses.pyc

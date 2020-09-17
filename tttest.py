# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
class filedalogdemo(QWidget):
    def __init__(self):
        os.chdir('./SessionFiles')
        super(filedalogdemo,self).__init__()
        layout=QVBoxLayout()
        self.btn1=QPushButton("Load Session")
        self.btn1.clicked.connect(self.getfile)
        layout.addWidget(self.btn1)
        self.text=QTextEdit()
        layout.addWidget(self.text)
        self.setLayout(layout)
        self.setWindowTitle("Choosing")
    def getfile(self):

        fname = QFileDialog.getOpenFileName(self,'Open File')
        # = QFileDialog.getSaveFileName(self,'Save File')
        #self.le.setPixmap(QPixmap(fname))
        #print fname
        #print fname[0]
        print type(fname)
        print fname
        fname = unicode(fname.toUtf8(), 'utf-8', 'ignore')
        fn = list(fname)
        print 'fn',type(fn)
        print fn
        fn1 = fname[0]
        print 'fn1',type(fn1)
        print fn1
        fn2 = fn1.split('/')
        print 'fn2',type(fn2)
        print fn2[-1]
        fn3 = str(fn2[-1])
        print 'fn3',type(fn3)
        print fn3
        # fn2 = fname[0].encode('utf-8')
        # #fn2 = fn1.symptom.decode('unicode-escape')
        # print 'fn2',type(fn2)
        # print fn2
        # fn3 = fn2.split('/')
        # print 'fn3non', type(fn3)
        # print fn3
        # fn3 = fn3[-1].encode('utf-8')
        # print 'fn3',type(fn3)
        # print fn3
        # fn4 = str(fn3[-1])
        # print 'fn4',type(fn4)
        # print fn4

        # fileName = fname[0].encode('utf-8').split('/')
        # fileName = str(fileName[-1])
        # print type(fileName)
        #fn1 = fn[0].split('/')
        #print '000'+fn1
    # def getfiles(self):
    #     dlg=QFileDialog()
    #     dlg.setFileMode(QFileDialog.AnyFile)
    #     dlg.setFilter(QDir.Files)
    #     if dlg.exec_():
    #         filenames = dlg.selectedFiles()
    #         #filename = filenames[0].encode('utf-8')
    #         df = pd.read
    #         print 'filename',type(filename)
    #         print filename
    #         # tmpsplit = filenames[0].split('/')
    #         # filename = tmpsplit[-1]
    #         # print filename
    #         # print type(filename)
    #         f = open(filename,'r')
    #
    #         with f:
    #             data=f.read()
    #             self.text.setText(data)
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=filedalogdemo()
    win.show()
    sys.exit(app.exec_())

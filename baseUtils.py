# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: baseUtils.py
import string

class baseUtils:

    def filterAlNum(self, str):
        return ('').join((ch for ch in str if ch.isalnum()))

    def cleanColumnNames(self, df):
        df.columns = map(lambda name: self.filterAlNum(name), df.columns)

    def header_prepender(self, filename, line):
        with open(filename, 'r+') as (f):
            content = f.read()
            f.seek(0, 0)
            f.write(line + '\n' + content)
# okay decompiling baseUtils.pyc

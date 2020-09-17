# -*- coding: utf-8 -*-

# uncompyle6 version 3.2.6
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: visualizationManager.py
import pandas as pd, matplotlib.pyplot as plt, matplotlib.patches as patches, numpy as np
from baseUtils import baseUtils
from PyQt4 import QtGui


class Visualizer(baseUtils):

    def __init__(self, userData, Qwidget=None):
        self.userData = userData
        self.Qwidget = Qwidget

    def queryndividuals(self):
        self.df_individuals = pd.read_csv('tblIndividuals.csv', index_col=0)
        self.df_individuals = self.df_individuals.replace('[\\$,]', '', regex=True).astype(float)
        self.cleanColumnNames(self.df_individuals)
        if 'CompanyID' not in self.userData['CompaniesCode'].columns or 'JobID' not in self.userData['BenchmarkJobsCode'].columns:
            # QtGui.QMessageBox.critical(MainWindow, 'Error', 'BenchmarkJobs or Companies are not filled!', QtGui.QMessageBox.Ok)
            raise ValueError('BenchmarkJobs or Companies are not filled!')
        self.individuals = self.df_individuals.reset_index().set_index('Company').loc[self.userData['CompaniesCode']['CompanyID']].reset_index().set_index('JobID').loc[self.userData['BenchmarkJobsCode']['JobID']].reset_index()
        self.individuals = self.individuals.reset_index().set_index('JobID').merge(self.userData['BenchmarkJobsCode'][['JobID', 'Name']].set_index('JobID'), right_index=True, left_index=True, how='left').reset_index()
        del self.individuals['JobCode']

    def genCompensationMetrics(self):
        # Updates BaseSalary, Bonuses, StockOptions, Benefits
        updateRate = self.userData['UpdateSurveyData'].get_value(0, 0)
        method = self.userData['CompensationMetricCode'].get_value(0, 'CompensationMetric')
        self.individuals['BaseSalary'] = self.individuals['BaseSalary'].apply(lambda x: x * (1 + updateRate / 100.0))
        self.individuals['Bonuses'] = self.individuals['Bonuses'].apply(lambda x: x * (1 + updateRate / 100.0))
        self.individuals['StockOptions'] = self.individuals['StockOptions'].apply(lambda x: x * (1 + updateRate / 100.0))
        self.individuals['Benefits'] = self.individuals['Benefits'].apply(lambda x: x * (1 + updateRate / 100.0))
        self.individuals['metric'] = self.individuals['BaseSalary']
        self.individuals['TotalCash'] = self.individuals.apply(lambda row: row['BaseSalary'] + row['Bonuses'], axis=1)
        self.individuals['TotalCompensation'] = self.individuals.apply(lambda row: row['TotalCash'] + row['Benefits'] + row['StockOptions'], axis=1)
        if method.find('Total') > 0:
            self.addTotalCompensation()
        else:
            if method.find('Cash') > 0:
                self.addTotalCash()
        # grouped = self.individuals[['JobID', 'Company', 'metric']].groupby('JobID')
        # groupedWM = self.individuals[['JobID', 'Company', 'metric']].groupby(['JobID', 'Company'])
        # 'numpy.float64' object has no attribute 'apply'
        
        # self.finalData = groupedWM.mean().mean() if method.find('Mean') <= 5 else (grouped.mean() if method.find('Weighted') > 0 else (grouped.quantile(0.25) if method.find('25') > 0 else (grouped.quantile(0.50) if method.find('50') > 0 else (grouped.quantile(0.75) if method.find('75') > 0 else 0))))
        # for id, df in grouped:
            # self.finalData = df.groupby('Company').mean().mean() if method.find('Mean') <= 5 else (df.mean() if method.find('Weighted') > 0 else (df.quantile(0.25) if method.find('25') > 0 else (df.quantile(0.50) if method.find('50') > 0 else (df.quantile(0.75) if method.find('75') > 0 else 0))))
        # 'numpy.float64' object has no attribute 'apply'
        data = pd.DataFrame({'JobID':[], 'Company':[], 'metric':[]})
        if (method.find('Mean') > 0) and  (method.find('Weighted') <= 0):
            grouped = self.individuals[['JobID', 'Company', 'metric']].groupby(['JobID','Company'])
            for job in grouped:
                metric = job[1].mean()
                data = data.append(pd.DataFrame([[job[0][0], job[0][1], metric.values[2]]], columns=['JobID', 'Company', 'metric']))
            grouped = data.groupby('JobID')
        else:
            grouped = self.individuals[['JobID', 'Company', 'metric']].groupby('JobID')
        self.finalData = grouped.mean() if method.find('Mean') > 0 else (grouped.quantile(0.25) if method.find('25') > 0 else (grouped.quantile(0.50) if method.find('50') > 0 else (grouped.quantile(0.75) if method.find('75') > 0 else 0)))
 
        if type(self.finalData) == int:
            raise ValueError('Final Data Calculation is not correct!')
            
        for index, row in self.userData['PolicyLinesCode'].iterrows():
            self.finalData[row['Name']] = self.finalData['metric'].apply(lambda x: x * (1 + float(row['Percent']) / 100))

        self.finalData = self.finalData.merge(right=self.userData['MatchwithFastCatJobsCode'][['JEpoint', 'Job', 'JobID']], right_on='JobID', left_index=True, how='left')
    def addTotalCash(self):
        self.individuals['metric'] = self.individuals['TotalCash']

    def addTotalCompensation(self):
        self.individuals['metric'] = self.individuals['TotalCompensation']

    def printDetailedReport(self):
        grouped = self.individuals[['Name', 'Company', 'BaseSalary', 'Bonuses', 'TotalCash', 'StockOptions', 'Benefits', 'TotalCompensation']].groupby('Name')
        for id, df in grouped:
            # del df['Name']
            # df.reset_index(drop = True).applymap(lambda x: ('{:,.0f}').format(x) else ('${:,.0f}').format(x)).to_html('/reports/DetailedReport_' + str(id) + '.html')
            del df['Name']
            # df.reset_index(drop = True)
            df['Company'] = df['Company'].map(lambda x: ('{:,.0f}').format(x))
            df['BaseSalary'] = df['BaseSalary'].map(lambda x: ('${:,.0f}').format(x))
            df['Bonuses'] = df['Bonuses'].map(lambda x: ('${:,.0f}').format(x))
            df['TotalCash'] = df['TotalCash'].map(lambda x: ('${:,.0f}').format(x))
            df['StockOptions'] = df['StockOptions'].map(lambda x: ('${:,.0f}').format(x))
            df['Benefits'] = df['Benefits'].map(lambda x: ('${:,.0f}').format(x))
            df['TotalCompensation'] = df['TotalCompensation'].map(lambda x: ('${:,.0f}').format(x))
            df = df.reset_index(drop = True)
            df.index = df.index + 1
            df.to_html('reports/DetailedReport_' + str(id) + '.html')
            self.addHeaderToHTML(str('reports/DetailedReport_' + str(id) + '.html'), [
             'Detailed Report', str(id),
             ('JE point: {0},\t Incumbents: {1}').format(self.getJE(id), len(df))])

    def getJE(self, name):
        je = self.userData['MatchwithFastCatJobsCode'].set_index('Job').loc[name]['JEpoint']
        return je

    def printSummaryReport(self):
        grouped = self.individuals[['Name', 'Company', 'BaseSalary', 'Bonuses', 'TotalCash', 'StockOptions', 'Benefits', 'TotalCompensation']].groupby('Name')
        summaryDF = pd.DataFrame(columns=['Weighted Mean', 'Mean', '25th', '50th', '75th'], index=['BaseSalary', 'TotalCash', 'TotalCompensation'])
        
        for id, df in grouped:
            summaryDF['Weighted Mean'] = df.mean()
            summaryDF['Mean'] = df.groupby('Company').mean().mean() #Each company gets a mean (Xbar), gets mean from all the means (Xbarbar)
            summaryDF['25th'] = df.quantile(0.25)
            summaryDF['50th'] = df.quantile(0.5)
            summaryDF['75th'] = df.quantile(0.75)
            summaryDF.applymap(lambda x: ('${:,.0f}').format(x)).to_html('reports/SummaryReport_' + str(id) + '_Base&Total' + '.html')
            self.addHeaderToHTML('reports/SummaryReport_' + str(id) + '_Base&Total' + '.html', data=[
             'Summary Report', str(id), ('JE point: {0}, Incumbents: {1}').format(self.getJE(id), len(df))])

        summaryDFBonusStock = pd.DataFrame(columns=['Mean', 'As a % of Base', '% who Receive'], index=['Bonuses', 'StockOptions'])
                    
         # Mean = Total Bonus of the employees who get bonuses / Number of Employees who get bonuses
         # As a % of Base = Total Bonus of the employees who get bonuses / Total Base Salary of the employees who get bonuses
         # % who Receive = Employees who get bonuses / Total employees

        for id, df in grouped:
            NumberBonus = float(0)
            NumberStockOptions = float(0)
            TotalBonus = float(0)
            TotalStock = float(0)
            TotalBase_B = float(0)
            TotalBase_S = float(0)
            for n in range(df.shape[0]): # length of the data (how many rows)
                if int(df.iloc[n, 3]) != 0:
                    NumberBonus += 1
                    TotalBonus += df.iloc[n, 3]
                    TotalBase_B += df.iloc[n, 2] # no need to * (1 + updateRate / 100.0), but basesalary already be multiplied
                if int(df.iloc[n, 5]) != 0:
                    NumberStockOptions += 1
                    TotalStock += df.iloc[n, 5]
                    TotalBase_S += df.iloc[n, 2] # no need to * (1 + updateRate / 100.0), but basesalary already be multiplied              
            if NumberBonus != 0: # normally will go this way
                summaryDFBonusStock.loc['Bonuses', 'Mean'] = df['Bonuses'].sum() / NumberBonus
                summaryDFBonusStock.loc['Bonuses', 'As a % of Base'] = TotalBonus / TotalBase_B
                summaryDFBonusStock.loc['Bonuses', '% who Receive'] = NumberBonus / df.shape[0]
            else: # if no one gets the bonuses
                summaryDFBonusStock.loc['Bonuses', 'Mean'] = df['Bonuses'].sum() #0
                summaryDFBonusStock.loc['Bonuses', 'As a % of Base'] = TotalBonus #0
                summaryDFBonusStock.loc['Bonuses', '% who Receive'] = NumberBonus #0
            if NumberStockOptions != 0: # normally will go this way
                summaryDFBonusStock.loc['StockOptions', 'Mean'] = df['StockOptions'].sum() / NumberStockOptions         
                summaryDFBonusStock.loc['StockOptions', 'As a % of Base'] = TotalStock / TotalBase_S
                summaryDFBonusStock.loc['StockOptions', '% who Receive'] = NumberStockOptions / df.shape[0]
            else: # if no one gets the stockoptions
                summaryDFBonusStock.loc['StockOptions', 'Mean'] = df['StockOptions'].sum() #0       
                summaryDFBonusStock.loc['StockOptions', 'As a % of Base'] = TotalStock #0
                summaryDFBonusStock.loc['StockOptions', '% who Receive'] = NumberStockOptions #0
            summaryDFBonusStock['Mean'] = summaryDFBonusStock['Mean'].map(lambda x: ('${:,.0f}').format(x))
            summaryDFBonusStock['As a % of Base'] = summaryDFBonusStock['As a % of Base'].map(lambda x: ('{:,.1f}%').format(x * 100))
            summaryDFBonusStock['% who Receive'] = summaryDFBonusStock['% who Receive'].map(lambda x: ('{:,.1f}%').format(x * 100))
            summaryDFBonusStock.to_html('reports/SummaryReport_' + str(id) + '_Bonus&Stock' + '.html')
            self.addHeaderToHTML('reports/SummaryReport_' + str(id) + '_Bonus&Stock' + '.html', data=[
             'Summary Report', str(id), ('JE point: {0}, Incumbents: {1}').format(self.getJE(id), len(df))])

    def addHeaderToHTML(self, filename, data=[]):
        header = ('<header>\n<h1>{0}</h1>\n<h3>{1}</h3>\n<p>{2}</p>\n</header>').format(*data)
        self.header_prepender(filename, header)

    def addHeaderToHTML2(self, filename, data=[]):
        header = ('<header>\n')
        self.header_prepender(filename, header)

    def reportGradeGraph(self):
        # self.calcRegLines()

        # Create the multindexing object
        # method = self.userData["CompensationMetricCode"].get_value(0, "CompensationMetric")
        # places = ["Min", "Mid", "Max"]
        # tup = [(index,row["policy"],row["range"]) for index,row in self.userData["GradesandRangesCode"]["grade"].iterrows()]
        # index = pd.MultiIndex.from_tuples({(grd,pol,rng,pl) for pl in places for grd,pol,rng in tup}
                                            # , names=['Grade#',"Policy","Range" ,'JE place'])

        # populate the Table
        # gradesData = pd.DataFrame(index=index,columns=["JE Point",method])
        # for index, row in self.userData["GradesandRangesCode"]["grade"].iterrows():
            # gradesData.loc[index,row["policy"],row["range"],"Min"][method] = self.regLine[row["policy"]](row["GEmin"])
            # gradesData.loc[index,row["policy"],row["range"],"Mid"][method] = self.regLine[row["policy"]]((row["GEmin"] + row["GEmax"])/2)
            # gradesData.loc[index,row["policy"],row["range"],"Max"][method] = self.regLine[row["policy"]](row["GEmax"])

            # gradesData.loc[index,row["policy"],row["range"],"Min"]["JE Point"] = row["GEmin"]
            # gradesData.loc[index,row["policy"],row["range"],"Mid"]["JE Point"] = (row["GEmin"] + row["GEmax"])/2
            # gradesData.loc[index,row["policy"],row["range"],"Max"]["JE Point"] = (row["GEmax"])


        # gradesData.sort_index().applymap(lambda x: '${:,.0f}'.format(x)).to_html("/reports/GradesData.html")
    
        self.calcRegLines()
        
        # Create the multindexing object
        method = self.userData['CompensationMetricCode'].get_value(0, 'CompensationMetric')
        places = ['Min', 'Mid', 'Max']
        tup = [ (index, row['policy'], row['range']) for index, row in self.userData['GradesandRangesCode']['grade'].iterrows() ]
        index = pd.MultiIndex.from_tuples({(grd + 1, pol, rng, pl) for pl in places for grd, pol, rng in tup}, names=[
         'Grade#', 'Policy', 'Range%', 'JE place'])
         
        # populate the Table
        gradesData = pd.DataFrame(index=index, columns=['JE Point', method])
        for index, row in self.userData['GradesandRangesCode']['grade'].iterrows():
            gradesData.loc[(index + 1, row['policy'], row['range'], 'Min')]['JE Point'] = row['GEmin']
            gradesData.loc[(index + 1, row['policy'], row['range'], 'Mid')]['JE Point'] = (row['GEmin'] + row['GEmax']) / 2
            gradesData.loc[(index + 1, row['policy'], row['range'], 'Max')]['JE Point'] = row['GEmax']
            
            gradesData.loc[(index + 1, row['policy'], row['range'], 'Min')][method] = (self.regLine[row['policy']]((row['GEmin'] + row['GEmax']) / 2)) * (1 - row['range'] / 100)
            gradesData.loc[(index + 1, row['policy'], row['range'], 'Mid')][method] = self.regLine[row['policy']]((row['GEmin'] + row['GEmax']) / 2)
            gradesData.loc[(index + 1, row['policy'], row['range'], 'Max')][method] = (self.regLine[row['policy']]((row['GEmin'] + row['GEmax']) / 2)) * (1 + row['range'] / 100)

        # gradesData[row['range']] = gradesData[row['range']].map(lambda x: ('{:,.1f}%').format(x))
        gradesData['JE Point'] = gradesData['JE Point'].map(lambda x: ('{:,.0f}').format(x))
        gradesData[method] = gradesData[method].map(lambda x: ('${:,.0f}').format(x))
        gradesData = gradesData.sort_index()
        gradesData.to_html('reports/BandsData_' + str(method) + '.html')
        self.addHeaderToHTML2('reports/BandsData_' + str(method) + '.html', data=['Grades Data'])

    def reportRanges(self): # redundant?! -> for bands and zone
        tup = [ (grdNum + 1, rngNum + 1) for grdNum, grdRow in self.userData['GradesandRangesCode']['range'].iteritems() for rngNum, rngRow in grdRow.iterrows()
              ]
        index = pd.MultiIndex.from_tuples(tup, names=['Band#', 'Zone#'])
        print tup
        rangesData = pd.DataFrame(index=index, columns=['JE Point', 'Min', 'Max'])
        for gradeNum, eachGrade in self.userData['GradesandRangesCode']['range'].iteritems():
            if len(eachGrade) == 0:
                continue
            print eachGrade
            for rangeNum, eachRange in eachGrade.iterrows():
                rng = int(eachRange['ID'])
                tmp = rangesData.loc[(gradeNum + 1, rng)]['JE Point']
                rangesData.loc[(gradeNum + 1, rng)]['JE Point'] = int(eachRange['JE Point'])
                rangesData.loc[(gradeNum + 1, rng)]['Min'] = int(eachRange['Min'])
                rangesData.loc[(gradeNum + 1, rng)]['Max'] = int(eachRange['Max'])
                print '->'
                print int(eachRange['ID'])

            print '----------'

        rangesData['Max'] = rangesData['Max'].map(lambda x: ('{:,.0f}').format(x))
        rangesData['Min'] = rangesData['Min'].map(lambda x: ('{:,.0f}').format(x))
        print rangesData.sort_index()
        rangesData.sort_index().to_html('reports/Bands&Zones.html')

    def drawGradeRange(self):
        self.drawGradeGraph(show=False)
        for gradeNum, eachGrade in self.userData['GradesandRangesCode']['range'].iteritems():
            if len(eachGrade) == 0:
                continue
            for rangeNum, eachRange in eachGrade.iterrows():
                self.drawRangesLine(eachRange['JE Point'], eachRange['Min'], eachRange['Max'])

        plt.show()

    def drawRangesLine(self, je, min, max):
        plt.plot([je, je, je], [min, (min + max) / 2, max], 'k.-')

    def calcRegLines(self):
        self.regLine = {}
        self.regLine['Base'] = np.poly1d(np.polyfit(self.finalData['JEpoint'], self.finalData['metric'], 1))
        self.regLine['Policy1'] = np.poly1d(np.polyfit(self.finalData['JEpoint'], self.finalData['Policy1'], 1))
        self.regLine['Policy2'] = np.poly1d(np.polyfit(self.finalData['JEpoint'], self.finalData['Policy2'], 1))

    def polyfit(x, y, degree):
        import numpy
        results = {}

        coeffs = numpy.polyfit(x, y, degree)

        # Polynomial Coefficients
        results['polynomial'] = coeffs.tolist()

        # r-squared
        p = numpy.poly1d(coeffs)
        # fit values, and mean
        yhat = p(x)  # or [p(z) for z in x]
        ybar = numpy.sum(y) / len(y)  # or sum(y)/len(y)
        ssreg = numpy.sum((yhat - ybar) ** 2)  # or sum([ (yihat - ybar)**2 for yihat in yhat])
        sstot = numpy.sum((y - ybar) ** 2)  # or sum([ (yi - ybar)**2 for yi in y])
        results['determination'] = ssreg / sstot

        return results

    def drawRegressionLine(self, show=True):
        plt.close('all')
        plt.figure(figsize=(15,10))
        self.regLine = {}
        self.regLine['Base'],self.r2 = self.drawLine(self.finalData['JEpoint'], self.finalData['metric'])
        legend = ['Jobs', 'Base Regression Line\n'+'y = '+str(self.regLine['Base'])+'\nR-Squared : '+str(self.r2)]
        colors = ['g--', 'b:']
        for index, row in self.userData['PolicyLinesCode'].iterrows():
            if row['Display'] == True:
                self.regLine[row['Name']] = self.drawLine(self.finalData['JEpoint'], self.finalData[row['Name']], True, colors[index])
                legend.append(row['Name'])

        #plt.text(10,-20,'y = '+str(self.regLine['Base']))
        plt.legend(legend,loc="best")
        plt.xlabel('JE points')
        plt.ylabel('$ (based on ' + self.userData['CompensationMetricCode'].get_value(0, 'CompensationMetric') + ')')
        plt.title('Regression Line')
        if show:
            plt.show()

        # newBigXValue = 300
        
        # slope =  ([self.finalData['metric'].values[len(self.finalData['metric'].values) - 1]] - self.finalData['metric'].values[:len(self.finalData['metric'].values) - 1])/([self.finalData['JEpoint'].values[len(self.finalData['JEpoint'].values) - 1]] - self.finalData['JEpoint'].values[:len(self.finalData['JEpoint'].values) - 1])
        # xCoords = list(self.finalData['JEpoint'].values[:len(self.finalData['JEpoint'].values) - 1]) + list([self.finalData['JEpoint'].values[len(self.finalData['JEpoint'].values) - 1] + newBigXValue])
        # extraY = slope * (xCoords[len(xCoords)- 1] - newBigXValue)
        # yCoords = list(self.finalData['metric'].values[:len(self.finalData['metric'].values) - 1]) + list([self.finalData['metric'].values[len(self.finalData['metric'].values) - 1] + extraY])
        # self.regLine['Base'] = self.drawLine(xCoords, yCoords)
        # legend = ['Jobs', 'Base Regression Line']
        # colors = ['g--', 'b:']
        # for index, row in self.userData['PolicyLinesCode'].iterrows():
            # if row['Display'] == True:
                # slope =  ([self.finalData[row['Name']].values[len(self.finalData[row['Name']].values) - 1]] - self.finalData['metric'].values[:len(self.finalData[row['Name']].values) - 1])/([self.finalData['JEpoint'].values[len(self.finalData['JEpoint'].values) - 1]] - self.finalData['JEpoint'].values[:len(self.finalData['JEpoint'].values) - 1])
                # extraY = slope * (xCoords[len(xCoords)- 1] - newBigXValue)
                # yCoords = list(self.finalData[row['Name']].values[:len(self.finalData[row['Name']].values) - 1]) + list([self.finalData[row['Name']].values[len(self.finalData[row['Name']].values) - 1] + extraY])
                # self.regLine[row['Name']] = self.drawLine(xCoords, self.finalData[row['Name']].values, True, colors[index])
                # legend.append(row['Name'])

    def drawLine(self, X, Y, policy=False, color='r'):
        if not policy:
            plt.plot(X, Y, 'o' + color)
        line = np.poly1d(np.polyfit(X, Y, 1))
        X = X.append(pd.Series(X.min() - (X.max() - X.min()) * 0.25))
        X = X.append(pd.Series(X.max() + (X.max() - X.min()) * 0.25))
        plt.plot(X, line(X), color)
        from sklearn.metrics import r2_score
        coefficient_of_dermination = r2_score(Y, line(X[:-2]))
        return line,coefficient_of_dermination

    def drawGradeGraph(self, show=True):
        self.drawRegressionLine(False)
        for index, row in self.userData['GradesandRangesCode']['grade'].iterrows():
            line = self.regLine[row['policy']]
            geMid = (row['GEmin'] + row['GEmax']) / 2
            jeYMin = geMid * (1 - row['range'] / 100)
            jeYMax = geMid * (1 + row['range'] / 100)
            try:
                self.drawRectangle(row['GEmin'], row['GEmax'], jeYMin, jeYMax, line)
            except:
                print("bug")
                self.drawRectangle(row['GEmin'], row['GEmax'], jeYMin, jeYMax, line[0])

        plt.title('Grades Graph')
        if show:
            plt.show()

    def drawRectangle(self, jeMin, jeMax, jeYMin, jeYMax, line):
        Ymax = line(jeYMax)
        Ymin = line(jeYMin)
        X = [jeMin, jeMax, jeMax, jeMin, jeMin]
        Y = [Ymin, Ymin, Ymax, Ymax, Ymin]
        plt.plot(X, Y, '-c', linewidth=2.0)
# okay decompiling visualizationManager.pyc

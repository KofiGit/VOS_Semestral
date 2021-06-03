import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ExcelWorker import Excel
import pyqtgraph as pg
import xlrd


class Canvas(FigureCanvas):

    def __init__(self, parent, excelPath, realData=False):
        fig, self.ax = plt.subplots(figsize=(5, 4), dpi=200)
        super().__init__(fig)
        self.setParent(parent)
        self.ExcelPath = excelPath

        if (realData):
            self.Excel()
        else:
            self.ShowCase()

    def Excel(self):
        # Get Excel on given Path
        excel = Excel(self.ExcelPath)
        # Get first sheet
        sheet = excel.readData()
        # Convert to list of floats and ignore first line as it should be header
        yValues = [float(item) for item in sheet.col_values(1)[3:]]
        yName = sheet.col_values(1)[2]
        npyArray = np.array(yValues)
        npxArray = [float(item) for item in sheet.col_values(0)[3:]]

        xLabel = sheet.col_values(0)[1]
        yLabel = sheet.col_values(1)[1]
        graphName = sheet.col_values(0)[0]

        self.ax.plot(npyArray, npxArray)  # add them to plot to show them

        self.ax.set(xlabel=xLabel, ylabel=yLabel,
                    title=graphName)  # create naming
        self.ax.grid()  # show grid

        plt.tight_layout()

    def ShowCase(self):

        x = np.arange(0.0, 2.0, 0.01)
        y = 1 + np.sin(2 * np.pi * x)

        self.ax.plot(x, y)

        self.ax.set(xlabel='x', ylabel='Y',
                    title='Show Case')
        self.ax.grid()

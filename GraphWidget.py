import pyqtgraph as pg

from ExcelWorker import Excel
import numpy as np


class GraphWidget:

    def __init__(self, parent, excelPath, realData=False):
        #self.setParent(parent)
        self.ExcelPath = excelPath


    def RealData(self):

        # Get Excel on given Path
        excel = Excel(self.ExcelPath)
        # Get first sheet
        sheet = excel.readData()

        npxArray = [float(item) for item in sheet.col_values(0)[3:]]

        xLabel = sheet.col_values(0)[1]
        yLabel = sheet.col_values(1)[1]
        graphName = sheet.col_values(0)[0]

        self.graphWidget = pg.PlotWidget()

        # Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle(graphName, color="b", size="30pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", yLabel, **styles)
        self.graphWidget.setLabel("bottom", xLabel, **styles)
        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        # Set Range
        self.graphWidget.setXRange(min(npxArray), max(npxArray), padding=0)

        minY = 0
        maxY = 1000000
        for column in range(sheet.ncols - 1):
            yName = sheet.col_values(column + 1)[2]
            yValues = [float(item) for item in sheet.col_values(column + 1)[3:]]
            if min(yValues) < minY:
                minY = min(yValues)
            if max(yValues) < maxY:
                maxY = max(yValues)
            self.plot(npxArray, yValues, yName, 'r')

        self.graphWidget.setYRange(minY, maxY, padding=0)

        return self.graphWidget

    def ShowCase(self):

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

        self.graphWidget = pg.PlotWidget()

        # Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)
        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        # Set Range
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        self.plot(hour, temperature_1, "Sensor1", 'r')
        self.plot(hour, temperature_2, "Sensor2", 'b')

        return self.graphWidget

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))
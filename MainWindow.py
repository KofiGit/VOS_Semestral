import sys
from os import path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QFileDialog, QLabel
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Canvas import Canvas
from GraphWidget import GraphWidget
from SubWindow import showHelp, showMessage


class Window(QMainWindow):
    def __init__(self, parent=None):
        # Call inherited class init method
        super(Window, self).__init__(parent)

        self.setGeometry(300, 300, 1200, 700)  # How big Window Should be (X,Y,Widht, Height)
        self.setWindowTitle("Graphs programming")  # Window Title
        self.chosenFilePath = "Not yet choosen"
        self.fileLabel = QLabel(f"Choosen Excel File: {self.chosenFilePath} ")
        self.fileLabel.setStyleSheet("font-weight: bold; color: black; font: 15px")
        self.initUI()  # init method

    def chooseFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            None,
            "Choose Excel File",
            "",
            "Excel Files (*.xls *.xlsx)",
            options=options)
        if fileName:
            self.chosenFilePath = fileName
            self.fileLabel.setText(f"Choosen Excel File: {self.chosenFilePath} ")

    def initUI(self):
        # Creating menu tool bar
        mainMenu = self.menuBar()
        mainMenu.setNativeMenuBar(False)
        fileMenu = mainMenu.addMenu('File')
        graphMenu = mainMenu.addMenu('Graph')
        helpMenu = mainMenu.addMenu('Help')
        self.addMainMenuItems(fileMenu=fileMenu, graphMenu=graphMenu, helpMenu=helpMenu)
        self.createCentralWidget()

    def createCentralWidget(self, typeGraph=0, realData=False):
        # Get Canvas with graph
        try:
            if not self.chosenFilePath and realData:
                showMessage(self, "No excel choosen.")
                return

            if not path.exists(self.chosenFilePath) and realData:
                showMessage(self, "Saved file not exists.")
                return

            self.centerLayout = QtWidgets.QVBoxLayout()  # QVBox lines up widgets vertically, has to be here to render it always
            self.centerLayout.addWidget(self.fileLabel, 2)

            if typeGraph == 1:  # ChartWidget
                self.createChartTypeWidget(realData)
            else:
                self.createCanvasTypeWidget(realData)

        except:
            ex = sys.exc_info()[0]
            showMessage(self, str(ex))

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()  # Qwidget is base class of all user interface objects
        widget.setLayout(self.centerLayout)
        self.setCentralWidget(widget)  # Provides main app window - so we adding widget to main window

    def createCanvasTypeWidget(self, realData=False):
        # Get Chart
        chart = Canvas(self, self.chosenFilePath, realData)
        # Prepare control toolbar for canvas
        toolbar = NavigationToolbar(chart, self)

        self.centerLayout.addWidget(toolbar)
        self.centerLayout.addWidget(chart)

    def createChartTypeWidget(self, realData=False):

        chartWidget = GraphWidget(self, self.chosenFilePath)
        if realData:
            widgetChart = chartWidget.RealData()
        else:
            widgetChart = chartWidget.ShowCase()

        self.centerLayout.addWidget(widgetChart)

    def addMainMenuItems(self, **kvargs):
        # Adding File menu buttons
        chooseExcelFile = QAction('Choose Excel', self)
        chooseExcelFile.setShortcut('Ctrl+L')
        chooseExcelFile.setStatusTip('Choose excel with data for graph')
        chooseExcelFile.triggered.connect(self.chooseFile)
        kvargs.get('fileMenu').addAction(chooseExcelFile)

        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        kvargs.get('fileMenu').addAction(exitButton)

        # Adding Help menu button
        aboutButton = QAction('About', self)
        aboutButton.setShortcut('Ctrl+A')
        aboutButton.setStatusTip('About this program')
        aboutButton.triggered.connect(showHelp)
        kvargs.get('helpMenu').addAction(aboutButton)

        # Adding graph menu button
        showCaseButton = QAction('Canvas graph from excel data', self)
        showCaseButton.setStatusTip('Show example graph on central widget')
        showCaseButton.triggered.connect(lambda: self.createCentralWidget(0, True))
        kvargs.get('graphMenu').addAction(showCaseButton)

        showCaseButton = QAction('Chart Widget from excel data', self)
        showCaseButton.setStatusTip('Show example graph widget')
        showCaseButton.triggered.connect(lambda: self.createCentralWidget(1, True))
        kvargs.get('graphMenu').addAction(showCaseButton)

        kvargs.get('graphMenu').addSeparator()

        showCaseButton = QAction('Show Case Canvas graph', self)
        showCaseButton.setStatusTip('Show example graph on central widget')
        showCaseButton.triggered.connect(lambda: self.createCentralWidget(0))
        kvargs.get('graphMenu').addAction(showCaseButton)

        showCaseButton = QAction('Show Case Chart Widget', self)
        showCaseButton.setStatusTip('Show example graph widget')
        showCaseButton.triggered.connect(lambda: self.createCentralWidget(1))
        kvargs.get('graphMenu').addAction(showCaseButton)

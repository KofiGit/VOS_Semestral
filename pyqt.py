# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PYQT.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NavigationToolbar = QtWidgets.QWidget(self.centralwidget)
        self.NavigationToolbar.setGeometry(QtCore.QRect(0, 0, 791, 101))
        self.NavigationToolbar.setObjectName("NavigationToolbar")
        self.Canvas = QtWidgets.QWidget(self.centralwidget)
        self.Canvas.setGeometry(QtCore.QRect(-1, 99, 791, 451))
        self.Canvas.setObjectName("Canvas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen_Data_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_Data_File.setObjectName("actionOpen_Data_File")
        self.actionSave_Graph = QtWidgets.QAction(MainWindow)
        self.actionSave_Graph.setObjectName("actionSave_Graph")
        self.actionOpen_Graph = QtWidgets.QAction(MainWindow)
        self.actionOpen_Graph.setObjectName("actionOpen_Graph")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuMenu.addAction(self.actionOpen_Data_File)
        self.menuMenu.addAction(self.actionSave_Graph)
        self.menuMenu.addAction(self.actionOpen_Graph)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionClose)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen_Data_File.setText(_translate("MainWindow", "Open Data File"))
        self.actionSave_Graph.setText(_translate("MainWindow", "Save Graph"))
        self.actionOpen_Graph.setText(_translate("MainWindow", "Open Graph"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import Window

if __name__ == '__main__':
    app = QApplication(sys.argv)        #Get app from QWidgets

    main = Window()                     #Initialize Main Window
    main.show()                         #Show main Window

    sys.exit(app.exec_())
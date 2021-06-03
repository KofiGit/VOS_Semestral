from PyQt5.QtWidgets import QDialog, QPushButton, QMessageBox, QVBoxLayout, QLabel


def showHelp(self):
    d = QDialog()
    d.setMinimumHeight(200)
    d.setMinimumWidth(200)
    d.setWindowTitle("About")

    layout = QVBoxLayout()
    label = QLabel("Program created by: Petr Koukolicek")
    layout.addWidget(label)

    b1 = QPushButton("Close", d)
    b1.clicked.connect(d.close)
    layout.addWidget(b1)

    d.setLayout(layout)
    d.exec_()

def showMessage(self, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Information")
    msg.setText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
# Python
import sys
import logging
import traceback
logger = logging.getLogger()

# PyQt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot

# Ui
from mainwindow import Ui_MainWindow


class Mainwindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Das Signal manuell verbinden
        # self.pushButton_4.clicked.connect(self.clicked)

        # Signal manuell auslösen
        # self.pushButton_4.click()

        # Wert manuell setzen
        # self.dial.setValue(90)

    def clicked(self):
        print("Button 4 was clicked")

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print("Button 1 clicked")
        self.dial.setValue(25)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        print("Button 2 clicked")
        self.dial.setValue(50)


    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        print("Button 3 clicked")
        self.dial.setValue(75)

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        print("Button 4 clicked")
        self.dial.setValue(99)
        self.changedValue.emit()

    @pyqtSlot(int)
    def on_dial_valueChanged(self, value):
        print("Value", value)


if __name__ == "__main__":

    def excepthook(*args, **kwargs):
        logger.exception("Fatal {} {}".format(args, kwargs))
        traceback.print_tb(args[2])

    app = QApplication(sys.argv)

    window = Mainwindow()
    window.show()

    # Eigener Exceptionhandler für debugging
    sys.excepthook = excepthook

    sys.exit(app.exec_())


def test798798("")


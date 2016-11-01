import sys

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

form = uic.loadUiType("Mkalendar.ui")[0]
class Mkalendar(QMainWindow, form) :


    def __init__(self):
        super().__init__()
        self.setUi()
        self.setEvent()

        # calendarWidget = QCalendarWidget()
        self.calMain.clicked[QtCore.QDate].connect(self.slotClicked)

    def setUi(self):
        self.setupUi(self)

    def setEvent(self):
        self.pushButton.clicked.connect(self.test)
        # self.cal

    def slotClicked(self, date):
        QtWidgets.QMessageBox.information(self, "QCalendarWidget Date Selected", date.toString())

    def test(self):
        print("A")

    # def clickDate(self):



def main() :
    app = QApplication(sys.argv)
    w = Mkalendar()
    w.show()
    app.exec_()

if __name__ == '__main__' :
    main()

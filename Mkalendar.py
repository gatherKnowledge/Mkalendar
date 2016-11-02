import sys
import XmlMaker

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

form = uic.loadUiType("Mkalendar.ui")[0]
class Mkalendar(QMainWindow, form) :
    chDate = QDate
    def __init__(self):
        super().__init__()
        self.setUi()
        self.setEvent()

    def setUi(self):
        self.setupUi(self)
        # self.addItems()
        # self.initStyle()

    # def initStyle(self):
        # self.optionList.hide()

    def setEvent(self):
        # self.pushButton.clicked.connect(self.test)
        self.calMain.clicked[QtCore.QDate].connect(self.dateClicked)
        self.btnNewWork.clicked.connect(self.makeWork)
        self.btnClose.clicked.connect(self.closeEvent)
    # def defaultItems(self):
    #     self.optionList.addItem("추가")
    def makeWork(self):
        self.addItems()

    def addItems(self):
        self.listWorkList.addItem("새 일정")
        self.listWorkList.setCurrentRow(1)
        print("현재 목록 수 : %s"%self.listWorkList.count())

    def dateClicked(self, date):
        # self.optionList.show()
        # QtWidgets.QMessageBox.information(self, "QCalendarWidget Date Selected", date.toString())
        sDate = date.toString("yyyy년 MM월 dd일 (ddd)요일")
        self.chDate = date.toString("yyyy-MM-dd")
        # sDate = str(date.year())+ str(date.day())+ str(date.month())
        # type(sDate
        # self.lbDate.setText(self._translate("MainWindow", "XXXX년 XX월 XX일"))
        self.lbDate.setText(sDate)

    # x btn click event name
    def closeEvent(self, event):
        qApp.exit()
    """TODO
    def closeEvent(self, event):

        reply = QMessageBox.question(self, "종료 알림"
                             ,"정말 종료 하시겠습니까?" ,QMessageBox.Yes | QMessageBox.No )
        t = type(event)
        # x mark로 들어오는 값이랑 버튼을 눌렀을 때 들어오는 값이 달라서 달리 보내야 함
        if t == bool :
            if reply == QMessageBox.Yes  :
                qApp.exit()
            else :
                pass
        else :
            if reply == QMessageBox.Yes  :
                event.accept()
            else :
                event.ignore()
    """





    def test(self):
        print("A")


def main() :
    app = QApplication(sys.argv)
    w = Mkalendar()
    w.show()
    app.exec_()

if __name__ == '__main__' :
    main()

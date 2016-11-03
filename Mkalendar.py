import sys
import XmlMaker
import FileIo
from PyQt5.QtGui import QPainter
from Task import Task

from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
form = uic.loadUiType("Mkalendar.ui")[0]


class Mkalendar(QMainWindow, form):


    def __init__(self):
        super().__init__()
        self.setUi()
        self.setData()
        self.setEvent()

    def setUi(self):
        self.setupUi(self)
        # self.addItems()
        # self.initStyle()
        # def initStyle(self):
        # self.optionList.hide()

    def setData(self):
        self.workStack = []
        self.chDate=self.calMain.selectedDate()
        self.dateClicked(self.chDate)

    def setEvent(self):
        self.calMain.clicked[QtCore.QDate].connect(self.dateClicked)
        self.btnNewWork.clicked.connect(self.makeNewWork)
        self.btnClose.clicked.connect(self.closeEvent)


    def makeNewWork(self):
        self.addItems(Task)

    def editItems(self):
        pass

    def addItems(self, Task):
        # 날짜 누르기 전
        # if type(self.chDate) != str:
        #     QtWidgets.QMessageBox.information(self, "Warning", "날짜가 선택되지 않았습니다.")
        #     return

        # 새로운 객체 생성 할 때
        if Task :
            self.listWorkList.addItem("새 일정")
            Task.title = "새일정"
            self.workStack.append(Task)

        #기존 것 추가해주는 이벤트 일 때
        else:
            # 기존 것에서 받고 list에 넣고
            self.listWorkList.addItem(Task.title)
            self.workStack.append(Task)


        #현재 stack
        print("현재 목록 수 : %s" % self.listWorkList.count())
        print("현재 stack 목록 수 : %s" % len(self.workStack))




    def emptyList(self):
        while True:
            self.listWorkList.takeItem(0)
            if self.listWorkList.count() == 0:
                break ;

    def dateClicked(self, date):
        # paint = QtWidgets.QPainter
        # paint.setBackground("RED")
        # self.calMain.paintCell(paint,date)
        # 이미지 파일
        # self.optionList.show()
        # QtWidgets.QMessageBox.information(self, "QCalendarWidget Date Selected", date.toString())
        sDate = date.toString("yyyy년 MM월 dd일 (ddd)요일")
        self.chDate = date.toString("yyyyMMdd")
        # sDate = str(date.year())+ str(date.day())+ str(date.month())
        # type(sDate
        # self.lbDate.setText(self._translate("MainWindow", "XXXX년 XX월 XX일"))
        self.lbDate.setText(sDate)
        # 아이템 삭제
        self.emptyList()
        self.workStack.clear()




        # 파일 내용
        saveData = FileIo.isAnyFile()
        if saveData :
            #있다
            # Task.date=
            # Task.title=''
            # Task.content=''
            # Task.index=''
            # 정렬 할 수있으면 하는것이 좋을듯 index를 기준으로
            # return list
            # list = FileIo.findTask(Task)
            list = FileIo.getTasks(self.chDate)
            for t in list:
                self.addItems(t)

        else :
            #없다
            FileIo.newFile()


    # ele을 파라미터로 받는 adder
    def adderList(self, list):
        if len(list) > 0:
            for elem in list:
                fTask = XmlMaker.parserXml(elem)
                self.addItems(fTask)
        else:pass

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


def main():
    app = QApplication(sys.argv)
    w = Mkalendar()
    w.show()
    app.exec_()

if __name__ == '__main__':
    main()

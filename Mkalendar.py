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


    # 초기화
    def __init__(self):
        super().__init__()
        self.setUi()

        #Data setting
        self.workStack = []
        self.chDate=self.calMain.selectedDate()
        self.dateClicked(self.chDate)
        self.currIndex = -1

        self.setEvent()

    # UI 세팅
    def setUi(self):
        self.setupUi(self)

    # 이벤트 세팅
    def setEvent(self):
        self.calMain.clicked[QtCore.QDate].connect(self.dateClicked)
        self.btnNewWork.clicked.connect(self.makeNewWork)
        self.btnClose.clicked.connect(self.closeEvent)
        self.btnSave.clicked.connect(self.saveEvent)
        self.listWorkList.clicked.connect(self.listItemClickEvent)

        # TODO List
        """
        # 저장 버튼 이벤트
        # 달력 해당 셀 색깔 변화 이벤트

        """



    def makeNewWork(self):
        Task.index = 0
        self.addItems(Task)

    def editItems(self):
        pass

    def listItemClickEvent(self):
        self.emptyText()
        row = self.listWorkList.currentRow()
        self.currIndex = row
        title = self.workStack[row].title
        content = self.workStack[row].content

        if title :
            self.editTitle(title)
        if content :
            self.editContent(content)

    def emptyText(self):
        self.content.clear()
        self.title.clear()

    # 제목 수정
    def editTitle(self, title):
        self.title.setText(title)

    # 내용 수정
    def editContent(self, content):
        self.content.setText(content)


    def addBefore(self, Task):
        self.listWorkList.addItem(Task.title)
        self.workStack.append(Task)

    def addNew(self, Task):
        # index확인
        if self.currIndex is not -1:
            row = self.currIndex
            bTask = self.workStack[row]
            bTask.title = self.title.text()
            bTask.content = self.content.toPlainText()
            print(self.workStack)
            print(row)
            self.workStack.insert(row, bTask)
        self.listWorkList.addItem("새 일정")
        pTask = Task("", self.chDate, "새일정", "")
        self.workStack.append(pTask)

    def addItems(self, Task):
        # 새로운 객체 생성 할 때
        if Task.index == 0:
            self.addNew(Task)
        #기존 것 추가해주는 이벤트 일 때
        else:
            # 기존 것에서 받고 list에 넣고
            self.addBefore(Task)
        #현재 stack
        print("현재 목록 수 : %s" % self.listWorkList.count())
        print("현재 stack 목록 수 : %s" % len(self.workStack))




    def emptyList(self):
        while True:
            self.listWorkList.takeItem(0)
            if self.listWorkList.count() == 0:
                break ;

    def dateClicked(self, date):
        self.emptyText()
        # paint = QtWidgets.QPainter
        # paint.setBackground("RED")
        # self.calMain.paintCell(paint,date)
        # 이미지 파일
        sDate = date.toString("yyyy년 MM월 dd일 (ddd)요일")
        self.chDate = date.toString("yyyyMMdd")
        self.lbDate.setText(sDate)
        # 아이템 삭제
        self.emptyList()
        self.workStack.clear()

        # 파일 내용
        saveData = FileIo.isAnyFile(self.chDate)
        if saveData :
            #있다
            # 정렬 할 수있으면 하는것이 좋을듯 index를 기준으로
            # return list
            # list = FileIo.findTask(Task)
            list = FileIo.getTasks(self.chDate)
            print(list)
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

    def saveEvent(self):
        # self.tClick()
        # TODO
        xml = XmlMaker.mkXmlTotal(self.workStack)
        FileIo.newXml(xml, self.chDate)



    def tClick(self):
        QMessageBox.information(self, "CLICK", "CLICK")

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
                passaddItemses  :
                event.accept()
            else :
                event.ignore()
    """

def main():
    app = QApplication(sys.argv)
    w = Mkalendar()
    w.show()
    app.exec_()

if __name__ == '__main__':
    main()

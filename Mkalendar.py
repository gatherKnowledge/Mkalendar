import sys
import XmlMaker
import FileIo
import Util
import  WorkStack

from Task import Task
from PyQt5.QtGui import QBrush
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

form = uic.loadUiType("Mkalendar.ui")[0]
"""
    추가 할 내용
    1.정규표현식 이용.. content 부분에 알람 기능 넣기
    2.일정 내용의 타이틀 부분에서 바뀌면 동시 일정 목록에 있는 내용도 동시에 바뀌기
    3.path 기본 잡아주고 내가 정할 수 있게 바꿔주기
    4.디자인 꾸미기

"""

class Mkalendar(QMainWindow, form):
    # 초기화
    def __init__(self):
        super().__init__()
        #ui
        self.setUi()

        #style
        self.colorCal()

        #Data setting
        self.chDate=self.calMain.selectedDate()
        self.workStack = WorkStack.WorkStack()
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
        self.btnDelWork.clicked.connect(self.delEvent)
        self.btnTest.clicked.connect(self.testEvent)
        self.btnReturn.clicked.connect(self.comebackEvent)

    def makeNewWork(self):
        Task.index = 0
        self.addItems(Task)

    def setListView(self):
        self.listWorkList.setCurrentRow(self.listWorkList.count()-1)
        self.listItemClickEvent()
        self.currIndex = -1

    def listItemClickEvent(self):
        row = self.currIndex
        if row is not -1:
            bTask = self.workStack.list[row]
            print(type(bTask))
            try:
                if self.content.toPlainText():
                    bTask.content = self.content.toPlainText()
            except:
                bTask.content = ""
            try:
                if self.title.text():
                    bTask.title = self.title.text()
            except:
                bTask.title = ""
            self.workStack.list[row] = bTask
        self.emptyText()
        row = self.listWorkList.currentRow()
        self.currIndex = row
        try:
            title = self.workStack.list[row].title
            content = self.workStack.list[row].content
            if title :
                self.editTitle(title)
            if content :
                self.editContent(content)
        except :
            print("title or content 명이 비었음")
        finally:
            print("finally 구문")
    def emptyText(self):
        self.content.clear()
        self.title.clear()

    # 제목 수정
    def editTitle(self, title):
        self.title.setText(title)

    # 내용 수정
    def editContent(self, content):
        self.content.setText(content)

    def delEvent(self):
        row = self.listWorkList.currentRow()
        self.workStack.list[row:row+1] = []
        self.workStack.workStackView()
        self.listWorkList.takeItem(row)

        self.setListView()

    def addBefore(self, Task):
        self.listWorkList.addItem(Task.title)
        self.workStack.list.append(Task)

    def saveEditData(self):
        row = self.listWorkList.currentRow()
        if row is not -1:
            bTask = self.workStack.list[row]
            print(type(bTask))
            try:
                if self.content.toPlainText():
                    bTask.content = self.content.toPlainText()
            except:
                bTask.content = ""
            try:
                if self.title.text():
                    bTask.title = self.title.text()
            except:
                bTask.title = ""
            self.workStack.list[row] = bTask

    def addNew(self, Task):
        self.saveEditData()
        # index확인
        self.listWorkList.addItem("새일정")
        pTask = Task("", self.chDate, "새일정", "")
        self.workStack.list.append(pTask)

        # 공통 : 새일정 하나 늘리고 마지막 리스트 클릭 돼있는 상태 유지
        self.emptyText()
        self.editTitle("새일정")

        self.setListView()

    def addItems(self, Task):
        # 새로운 객체 생성 할 때
        if Task.index == 0:
            self.addNew(Task)
        #기존 것 추가해주는 이벤트 일 때
        else:

            # 기존 것에서 받고 list에 넣고
            self.addBefore(Task)
        #현재 stack
        itemMent = "|현재 목록 수 : %s" % self.listWorkList.count()
        stackMent = "|현재 stack 목록 수 : %s" % len(self.workStack.list)
        mentlist = [itemMent, stackMent]
        Util.printBox(mentlist)
        self.workStack.workStackView()

    def testEvent(self):
        self.clickTest()

    def emptyList(self):
        while True:
            self.listWorkList.takeItem(0)
            if self.listWorkList.count() == 0:
                break

    def dateClicked(self, date):
        self.currIndex = -1
        self.emptyText()
        sDate = date.toString("yyyy년 MM월 dd일 (ddd)요일")
        self.chDate = date.toString("yyyyMMdd")
        self.lbDate.setText(sDate)
        # 아이템 삭제
        self.emptyList()
        self.workStack.list.clear()


        """
        있던 없던 상관X
        """
        # 파일 내용
        saveData = FileIo.isAnyFile(self.chDate)
        if saveData :
            # 정렬 할 수있으면 하는것이 좋을듯 index를 기준으로
            list = FileIo.getTasks(self.chDate)
            for t in list:
                self.addItems(t)

        self.setListView()

    # ele을 파라미터로 받는 adder
    def adderList(self, list):
        if len(list) > 0:
            for elem in list:
                fTask = XmlMaker.parserXml(elem)
                self.addItems(fTask)
        else:pass

    def saveEvent(self):
        if not self.workStack.list :
            FileIo.delFile(self.chDate)
            self.colorCal("2")
        else :
            bTask =  self.workStack.list.pop()
            bTask.title = self.title.text()
            bTask.content = self.content.toPlainText()
            self.workStack.list.append(bTask)
            xml = XmlMaker.mkXmlTotal(self.workStack.list)
            FileIo.newXml(xml, self.chDate)
            self.colorCal()
        saveData = FileIo.isAnyFile(self.chDate)
        if saveData:
            self.emptyList()
            self.workStack.list.clear()
            # 정렬 할 수있으면 하는것이 좋을듯 index를 기준으로
            list = FileIo.getTasks(self.chDate)
            for t in list:
                self.addItems(t)

    def comebackEvent(self):
        self.calMain.showToday()

    def divDate(self, date):
        year = date[0:4]
        month = date[4:6]
        day = date[6:8]
        if int(month) < 10:
            month = date[5:6]
        if int(day) < 10:
            day = date[7:8]
        year = int(year)
        month = int(month)
        day = int(day)
        list = [year, month, day]
        return list

    def colorOneCell(self, pdate):
        brush = QBrush()
        qtColor = Qt.white
        brush.setColor(qtColor)
        dlist = self.divDate(pdate)
        date = QDate(dlist[0],dlist[1],dlist[2])
        cf = self.calMain.dateTextFormat(date)
        cf.setBackground(brush)
        self.calMain.setDateTextFormat(date, cf)

    def colorManyCell(self):
        list = FileIo.getDateList()
        qtColor = Qt.darkCyan
        brush = QBrush()
        brush.setColor(qtColor)
        for file in list:
            # date = QDate(2016, 11, 09)
            dlist = self.divDate(file)
            date = QDate(dlist[0], dlist[1], dlist[2])
            cf = self.calMain.dateTextFormat(date)
            cf.setBackground(brush)
            self.calMain.setDateTextFormat(date, cf)
    def colorCal(self, color = "1"):
        if color is "1":
            self.colorManyCell()
        elif color is "2":
            self.colorOneCell(self.chDate)

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
                qApp.exit()
            else :
                event.ignore()


def main():
    app = QApplication(sys.argv)
    w = Mkalendar()
    w.show()
    app.exec_()

if __name__ == '__main__':
    main()

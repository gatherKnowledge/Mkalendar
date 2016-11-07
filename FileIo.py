from Task import Task
import os
from xml.etree.ElementTree import dump
from xml.etree.ElementTree import ElementTree as elemt
from xml.etree import ElementTree

path = "C:\\Users\\Company_SH\\Desktop\\test\\"
pFileName = "tasks"


def isAnyFile(date):
    if os.path.isfile(path+pFileName+date+".xml"):
        return True
    else:
        return False

def isAnyXmlFile(Task):
    if os.path.isfile(path + pFileName + Task.date +".xml"):
        print("파일 O")
        return True
    else:
        print("파일 X")
        return False

def newXml(xml, date):
    et = elemt(xml)
    et.write(path+pFileName+date+".xml", encoding="utf-8", xml_declaration=True)

def newFile():
    # r : read , a : append, w : write
    f = open(path+pFileName, 'w')
    f.write("<?xml version=\"1.0\"?>\n")
    f.write("<Tasks>\n</Tasks>")
    # f.write("</xml>")
#write 기능, Task
def modiFile(Task):
    f = open (path+pFileName, 'w')
    f.write()

def getMaxIdx(date):
    list = getTasks(date)
    idxList = []
    for i in list:
        idxList.append(i.index)
    idxList.sort(reverse=True)
    return idxList.index(0)

def getElemRoot(date):
    tree = ElementTree.parse(path +pFileName+date +".xml")
    root = tree.getroot()
    return root

# 날짜 입력 받으면 해당 날짜의 Tasks를 받아옴
# 현재는 잘 몰라서 --> 바로 불러오고싶은대 xml로 불러옴
def getTasks(date):
    root = getElemRoot(date)
    list = []
    for fTask in root.findall('Task'):
        if fTask.find('date').text == date:
            nIndex = fTask.find('index').text
            nDate = fTask.find('date').text
            nTitle = fTask.find('title').text
            nContent = fTask.find('content').text
            if not nIndex :
                nIndex = ''
            if not nDate :
                nDate = ''
            if not nTitle :
                nTitle = ''
            if not nContent :
                nContent = ''
            pTask= Task(nIndex, nDate, nTitle, nContent)
            list.append(pTask)

        else:
            pass
    print("리턴 되기 전")
    print(list)
    return list

# return type --> element
def findTask(Task):
    root = getElemRoot()
    print("file s","*"*50)
    dump(root)
    print("file e","*"*50)
    #return List
    list = []
    print("count 갯수 : %s" % Task.getCount(Task))
    if Task.getCount(Task) == 1:
        for fTask in root.findall('Task'):
            if fTask.find('date').text == Task.date :
                list.append(fTask)
            else :
                pass
        return list
    else :
        for fTask in root.findall('Task'):
            if fTask.find('index').text == Task.index :
                if fTask.find('date').text == Task.date :
                    return fTask
                else : pass
            else : pass



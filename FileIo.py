from Task import Task
import os
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import dump
from xml.etree import ElementTree

path = "C:\\Users\\Company_SH\\Desktop\\"
pFileName = "tasks.xml"


def isAnyFile():
    if os.path.isfile(path+pFileName):
        print("파일 O")
        return True
    else:
        print("파일 X")
        return False

"""
if os.path.isdir("000"):
    print
    "디렉토리 있습니다"
else:
    print
    "그런 이름의 디렉토리는 없습니다"
"""

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
    print("*"*50)
    print(list[0].title, list[1].title)
    print("*"*50)
    idxList = []
    for i in list:
        print(i.title)
        idxList.append(i.index)
        print(i.index)
    print(idxList)
    print(idxList.sort(reverse=True))
    print(idxList.index(0))
    return idxList.index(0)



def getElemRoot():
    # f = open(path + pFileName,encoding="utf8")
    # str = ""
    # while True:
    #     line = f.readline()
    #     if not line:
    #         break
    #     str += line
    # f.close()
    # print(str)
    # childs = str.getiterator()
    tree = ElementTree.parse(path + pFileName)
    root = tree.getroot()
    return root

# 날짜 입력 받으면 해당 날짜의 Tasks를 받아옴
# 현재는 잘 몰라서 --> 바로 불러오고싶은대 xml로 불러옴
def getTasks(date):
    root = getElemRoot()
    list = []
    i = 0
    for fTask in root.findall('Task'):
        if fTask.find('date').text == date:
            # Task(fTask.find('index').text, fTask.find('date').text,fTask.find('title').text,fTask.find('content').text)
            Task(fTask.find('index').text, fTask.find('date').text, fTask.find('title').text, fTask.find('content').text)
            # Task()
            list.append(Task)
            # print(Task.index)
            # print(Task.title)
            i = i+1
            print("cnt", i)
            print("index : ", Task.index)
            print("index : ", Task.date)
            print("index : ", Task.title)
            print("index : ", Task.content)
        else:
            pass
    # print("GetTasks에서 list")
    # print(list)
    # print("*"*50)
    return list

# return type --> element
def findTask(Task):
    root = getElemRoot()
    #
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
            # for child in root:
            #     sign = False
            #     for cofc in child:
            #         # print(cofc.tag, cofc.text)
            #         print("현재 값 : ", cofc.tag, cofc.text)
            #         if cofc.tag == "index" :
            #             if cofc.text == Task.index :
            #                 sign = True
            #         pass
            #
            #         if cofc.tag == "date":
            #             if cofc.text == Task.date and sign == True:
            #                 return child
            #             else :
            #                 pass
            #         else :
            #             pass

def __main__():
    mTask = Task
    mTask.index = "1"
    mTask.date = ""
    mTask.title = ""
    mTask.content=""

    # print("print 값", mTask.getCount(mTask))
    # print(type(findTask(Task)))
    getMaxIdx("20161102")
if __name__ == '__main__':
    __main__()



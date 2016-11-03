from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import dump

from Task import Task

def mkXml(Task):
    xTask = Element("Task")
    SubElement(xTask, "index").text =Task.index
    SubElement(xTask, "date").text = Task.date
    SubElement(xTask, "title").text = Task.title
    SubElement(xTask, "content").text = Task.content
    indent(xTask)
    return xTask

def indent(elem, level=0):
    i = "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text= i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail= i
        for elem in elem :
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else :
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i + "   "


def parserXml(elem):
    Task.index = SubElement(elem, "index").text
    Task.date = SubElement(elem, "date").text
    Task.title = SubElement(elem, "title").text
    Task.content = SubElement(elem, "content").text
    return Task

"""
Task.content = "내용"
Task.title = "제목"
Task.date = "20161102"
Task.index = "1"
dump(mkXml(Task))
"""
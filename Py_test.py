from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import dump
from xml.etree import ElementTree
import XmlMaker


path = "C:\\Users\\Company_SH\\Desktop\\"
pFileName = "tasks"

e= Element("task")
xml = XmlMaker.mkXml(list)
FileIo.newXml(xml, "20161102")
ElementTree.write(path + "aa.xml", encoding="utf-8", xml_declaration=True)
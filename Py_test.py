

class obj:
    def __init__(self, a):
        self.a = a
class obj2 :
    def __init__(self, a):
        self.a = a

pList = [obj(1),obj(2),obj(3),obj(4),obj(5)]
list = []

for i in pList:
    obj2.a = i.a
    list.append(obj2)


for i in list :
    print(i.a)
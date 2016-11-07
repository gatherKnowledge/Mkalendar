
class WorkStack(list):
    def __init__(self):
        self.list = []

    def append(self, obj):
        self.list.append(obj)
        self.workStackView()

    def remove(self, value):
        self.list.remove(value)
        self.workStackView()

    def clear(self):
        self.list.clear()

    def workStackView(self):
        fullSize = 40
        mark = ''
        for i in range(0, fullSize):
            if i % 3 == 0:
                mark += '*'
            else:
                mark += '--'
        mark += "\n|"
        tmark = ""
        for i in range(0, len(self.list)):
            tmark += "XXXX|"
            if i == len(self.list) - 1:
                while True:
                    if (len(tmark) < len(mark) - 4):
                        tmark += " "
                    else:
                        break
                tmark += "|"
        mark += tmark
        mark += "\n"
        for i in range(0, fullSize):
            if i % 3 == 0:
                mark += '*'
            else:
                mark += '--'
        print("* self.list 개 수: %s" % len(self.list))
        print(mark)

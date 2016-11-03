class Task:
    def __init__(self, index, date, title, content):
        self.index = index
        self.date = date
        self.title = title
        self.content = content

    def getCount(self):
        self.count = 0
        if self.index != '' :
            self.count =self.count + 1
        if self.date != '' :
            self.count = self.count + 1
        if self.title != '' :
            self.count = self.count + 1
        if self.content != '' :
            self.count = self.count + 1

        print("최종 개수 %s" % self.count)
        return self.count


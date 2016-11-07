def workStackView(list):
    fullSize = 40
    mark = ''
    for i in range(0, fullSize):
        if i % 3 == 0:
            mark += '*'
        else:
            mark += '--'
    mark += "\n|"
    tmark = ""
    for i in range(0, len(list)):
        tmark += "XXXX|"
        if i == len(list)-1 :
            while True :
                if(len(tmark) < len(mark)-4 ):
                    tmark +=" "
                else :
                    break
            tmark += "|"
    mark += tmark
    mark += "\n"
    for i in range(0, fullSize):
        if i % 3 == 0:
            mark += '*'
        else:
            mark += '--'
    print("* list 개 수: %s"%len(list))
    print(mark)

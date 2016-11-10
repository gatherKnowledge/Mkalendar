import Task
# 문자열 list input -->>
# output -->
# * ---------------------------------- *
# |현재 목록 수 : 3                     |
# |현재 stack 목록 수 : 3               |
# * ---------------------------------- *
def printBox(plist):
    # print(type(list))
    print("\n"*10)
    if type(plist) is Task.Task:
        tmpList = [plist]
        plist = tmpList
    print("*", "-" * 34, "*")
    for p in range(0, len(plist)):
        while True:
            if len(plist[p]) < 32:
                plist[p] += " "
            else:
                print(plist[p], "|")
                break
    print("*", "-" * 34, "*")
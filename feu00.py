import sys
import time

def createLine(L):
    if L == -1:
        return "o"
    s = "o"
    for _ in range(L):
        s += "-"
    s += "o"
    return s

def createEmptyLine(L):
    if L == -1:
        return "|"
    s = "|"
    for _ in range(L):
        s += " "
    s += "|"
    return s

def createString(L,l):
    if L == 0 or l == 0:
        return ""
    if l == 1:
        return createLine(L-2)
    s = createLine(L-2)
    for _ in range(l-2):
        s += "\n" + createEmptyLine(L-2)
    s += "\n" + createLine(L-2)
    return s

if len(sys.argv) != 3 or not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("error")
    exit()
else:
    print(createString(int(sys.argv[1]),int(sys.argv[2])))
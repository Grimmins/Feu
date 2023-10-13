import sys

def dispTab(tab):
    sh = ""
    for i in range(len(tab)):
        for j in range (len(tab[0])):
            sh += tab[i][j]
        sh += '\n'
    print(sh)

def list_of_lines(filename):
    result = []
    try:
        file = open(filename, 'r')
        for line in file:
            line_list = list(line.rstrip('\n'))
            result.append(line_list)
    except FileNotFoundError:
        print(f"Le fichier {filename} n'a pas été trouvé !", file=sys.stderr)
        return None
    ch = ""
    for i in result[0]:
        if i.isdigit():
            ch += i
    result[0][0] = ch
    for i in range(len(ch) - 1):
        result[0].pop(1 + i)
    return result


def file_to_tab(filename):
    result = []
    list_lines = list_of_lines(filename)
    for i in range(len(list_lines)):
        result.append([])
        for j in range(len(list_lines[i])):
            if list_lines[i][j] == '.':
                result[i].append(-1)
            else:
                result[i].append(int(list_lines[i][j]))
    return result

def listObstOfLines(fileLines, cObst):
    result = []
    for i in range(len(fileLines)):
        for j in range(len(fileLines[0])):
            if fileLines[i][j] == cObst:
                result.append([i,j])
    return result

def surface(fileLines, taille):
    result = []
    for i in range(len(fileLines)):
        for j in range(len(fileLines[0])):
            if isSurfaceClean(fileLines,i,j,taille):
                result.append([i,j])
    return result

def isSurfaceClean(fileLines,i,j,taille):
    for k in range(i,i+taille+1):
        for l in range(j,j+taille+1):
            if [k,l] in listObst or l > len(fileLines[0])-1 or k > maxHeight-1:
                return False
    return True

def changeTab(fileLines,taille,origin,cSqua):
    x,y = origin[0],origin[1]
    for i in range(x,x+taille+1):
        for j in range(y,y+taille+1):
            fileLines[i][j] = cSqua
    return fileLines

def check_if_file_correct(filename):
    fileLines = list_of_lines(filename)
    if fileLines == None:
        return
    #vérifier les paramètres
    if (len(fileLines[0]) != 4 or not fileLines[0][0].isdigit() or fileLines[0][1] == fileLines[0][2] or fileLines[0][1] == fileLines[0][3] or fileLines[0][2] == fileLines[0][3] or len(fileLines[0][1]) != 1 or len(fileLines[0][2]) != 1 or len(fileLines[0][3]) != 1):
        return False

    #vérifier la bonne taille
    if int(fileLines[0][0]) != len(fileLines)-1:
        return False

    #vérifier bon caractères
    for i in range(1,len(fileLines)):
        for j in range(len(fileLines[1])):
            if fileLines[i][j] != fileLines[0][2] and fileLines[i][j] != fileLines[0][1]:
                return False

    return True

if len(sys.argv) != 2:
    print("erreur d'argument on souhaite le nom d'un seul fichier .txt en argument")
elif not check_if_file_correct(sys.argv[1]):
    print("erreur de format du fichier texte ou fichier introuvable")
else:
    fileTest = sys.argv[1]
    fileLines = list_of_lines(fileTest)
    maxHeight = int(fileLines[0][0])
    cFree = fileLines[0][1]
    cObst = fileLines[0][2]
    cSqua = fileLines[0][3]
    fileLines.pop(0)
    listObst = listObstOfLines(fileLines, cObst)
    result = surface(fileLines, 0)
    taille = 0
    for i in range(1,maxHeight):
        result1 = surface(fileLines, i)
        if len(result1) != 0:
            taille += 1
            result = result1
    finalBoard = changeTab(fileLines,taille,result[0],cSqua)
    dispTab(finalBoard)
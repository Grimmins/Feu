import sys

def check_if_file_correct(filename):
    result= list_of_lines(filename)
    if len(result) != 9:
        return False
    else:
        for i in range(len(result)):
            if len(result[i]) != 9:
                return False
        return True


def list_of_lines(filename):
    result = []
    with open(filename, "r") as file:
        for line in file:
            line_list = list(line.rstrip('\n'))
            result.append(line_list)
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

def display(tab):
    ch = ""
    for i in range(len(tab)):
        if i%3 == 0 and i != 0:
            ch+= "----+-----+----\n"
        for j in range(len(tab[i])):
            if j%3 == 0 and j!= 0:
                if tab[i][j] == -1:
                    ch += " | _"
                else:
                    ch += " | " + str(tab[i][j])
            else:
                if tab[i][j] == -1:
                    ch += "_"
                else:
                    ch += str(tab[i][j])
        ch += "\n"
    return ch

def valid(tab, num, pos):

    #check line
    for j in range(len(tab[0])):
        if tab[pos[0]][j] == num:
            return False

    #check column
    for i in range(len(tab)):
        if tab[i][pos[1]] == num:
            return False

    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if tab[i][j] == num and [i,j] != pos:
                return False

    return True

def solve(tab):
    find = find_empty(tab)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(tab, i, (row, col)):
            tab[row][col] = i

            if solve(tab):
                return True

            tab[row][col] = -1

    return False

def find_empty(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == -1:
                return (i, j)  # row, col
    return None

global tab

if len(sys.argv) != 2:
    print("erreur d'argument on souhaite le nom d'un seul fichier .txt en argument")
elif not check_if_file_correct(sys.argv[1]):
    print("erreur de format du fichier texte")
else:
    tab = file_to_tab(sys.argv[1])
    print(display(tab))
    solve(tab)
    print(display(tab))

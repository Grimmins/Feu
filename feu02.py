import sys

def read_file_to_list(filename):
    result = []
    with open(filename, "r") as file:
        for line in file:
            line_list = list(line.rstrip('\n'))
            result.append(line_list)
    return result

def toComplete(board, to_find, origin):
    maxX = -sys.maxsize - 1
    for i in range(len(board)):
        maxX = max(maxX, len(board[i]))
    maxY = len(board)
    ch = ""
    NBx = originToTabCoordonates(to_find, origin)
    for i in range(maxY):
        for j in range(maxX):
            if [i,j] in NBx and to_find[i-origin[0]][j-origin[1]] != ' ':
                ch += to_find[i-origin[0]][j-origin[1]]
            else:
                ch += "-"
        ch += '\n'
    return ch

def originToTabCoordonates(to_find, origin):
    NBx = []
    for i in range(len(to_find)):
        for j in range(len(to_find[i])):
            NBx.append([origin[0]+i,origin[1]+j])
    return NBx


def final_test(board, to_find):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == to_find[0][0]:
                test_board = []
                for k in range(len(to_find)):
                    for l in range(len(to_find[k])):
                        if i+k < len(board) and j+l < len(board[i]):
                            test_board.append([i+k,j+l])
                        else:
                            return False
                if check_if_equals(test_board, to_find):
                    global origin
                    origin = test_board[0]
                    return True
    return False

def check_if_equals(test_board, to_find):
    k = 0
    for i in range(len(to_find)):
        for j in range(len(to_find[i])):
            if board[test_board[k][0]][test_board[k][1]] != to_find[i][j] and to_find[i][j] != ' ':
                return False
            k += 1
    return True

board = read_file_to_list(sys.argv[1])
to_find = read_file_to_list(sys.argv[2])
if final_test(board, to_find):
    print("Trouvé !")
    print("Coordonnées : " + str(origin[1]) + ", " + str(origin[0]))
    print(toComplete(board, to_find, origin))
else:
    print("Introuvable !")

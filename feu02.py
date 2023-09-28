import sys

def read_file_to_list(filename):
    result = []
    with open(filename, "r") as file:
        for line in file:
            line_list = list(line.rstrip('\n'))
            result.append(line_list)
    return result

def toComplete(filename, origin):
    result = read_file_to_list(filename)
    print(result)
    maxX = -sys.maxsize - 1
    print(maxX)
    for i in range(len(result)):
        maxX = max(maxX, len(result[i]))
    maxY = len(result)
    ch = ""
    for i in range(maxY):
        for j in range(maxX):
            if i == origin[0] and j == origin[1]:
                ch +=


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
print(final_test(board, to_find), origin)
print(toComplete(sys.argv[1]))

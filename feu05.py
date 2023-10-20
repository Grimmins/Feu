import sys
import copy

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
    return result

def getParam(tab):
    L = tab[0]
    param = []
    ch = ""
    for i in range(len(L)):
        if not L[i].isdigit():
            param.append(ch)
            break
        else:
            ch += L[i]
    for i in range(len(ch)):
        L.pop(0)
    param.append(L[0])
    L.pop(0)
    ch = ""
    for i in range(len(L)):
        if not L[i].isdigit():
            param.append(ch)
            break
        else:
            ch += L[i]
    for i in range(len(ch)):
        L.pop(0)
    for i in L:
        param.append(i)
    return param

def dispMaze(maze_with_path):
    for row in maze_with_path:
        print("".join(row))

def findStartExit(maze, exitChar):
    entry = (0, 0)
    out = (0, 0)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == startChar:
                entry = (row, col)

            elif maze[row][col] == exitChar:
                out = (row, col)
    return (entry, out)

def create_graph_from_maze(maze, freeChar, startChar, exitChar):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])

    for row in range(rows):
        for col in range(cols):
            if maze[row][col] in [freeChar, startChar, exitChar]:
                node = (row, col)
                graph[node] = []

                neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for neighbor in neighbors:
                    n_row, n_col = neighbor
                    if 0 <= n_row < rows and 0 <= n_col < cols and maze[n_row][n_col] in [freeChar, startChar, exitChar]:
                        graph[node].append(neighbor)
    return graph

def manhattan_distance(current_node, goal_node):
    current_node_x = current_node[0]
    current_node_y = current_node[1]
    goal_node_x = goal_node[0]
    goal_node_y = goal_node[1]
    diff_x = abs(current_node_x - goal_node_x)
    diff_y = abs(current_node_y - goal_node_y)
    manhattan_distance = diff_x + diff_y
    return manhattan_distance


def find_lowest_f_cost_node(open_set, f_costs):
    lowest_f_cost = float('inf')
    lowest_f_cost_node = None
    for node in open_set:
        if f_costs[node] < lowest_f_cost:
            lowest_f_cost = f_costs[node]
            lowest_f_cost_node = node
    return lowest_f_cost_node

def reconstruct_path(parents, current_node):
    path = []
    while current_node is not None:
        path.insert(0, current_node)
        current_node = parents[current_node]
    return path

def a_star_algorithm(graph, start_node, goal_node, heuristic_func):
    open_set = {start_node}
    closed_set = set()

    g_costs = {node: float('inf') for node in graph}
    g_costs[start_node] = 0

    f_costs = {node: float('inf') for node in graph}
    f_costs[start_node] = heuristic_func(start_node, goal_node)

    parents = {node: None for node in graph}

    while open_set:
        current_node = find_lowest_f_cost_node(open_set, f_costs)

        if current_node == goal_node:
            path = reconstruct_path(parents, goal_node)
            return path

        open_set.remove(current_node)
        closed_set.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor in closed_set:
                continue

            tentative_g_cost = g_costs[current_node] + 1

            if neighbor not in open_set:
                open_set.add(neighbor)

            if tentative_g_cost < g_costs[neighbor]:
                parents[neighbor] = current_node
                g_costs[neighbor] = tentative_g_cost
                f_costs[neighbor] = g_costs[neighbor] + heuristic_func(neighbor, goal_node)

    return []

def trace_path_in_maze(maze, path, pathChar):
    maze_copy = copy.deepcopy(maze)
    for i in range(1, len(path) - 1):
        row, col = path[i]
        maze_copy[row][col] = pathChar
    return maze_copy

# affiche le nombre de pas pour trouver la sortie
def number_attempts(maze_with_path, pathChar):
    count_o = 0
    for row in range(len(maze_with_path)):
        for col in range(len(maze_with_path[0])):
            if maze_with_path[row][col] == pathChar:
                count_o += 1
    print(f'Sortie en {count_o} pas !')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("error")
        sys.exit()

    mazeWithParameters = list_of_lines(filename)
    maze = mazeWithParameters[1:]
    param = getParam(mazeWithParameters)
    obstChar = param[3]
    freeChar = param[4]
    pathChar = param[5]
    startChar = param[6]
    exitChar = param[7]

    start, exit = findStartExit(maze, exitChar)
    graph = create_graph_from_maze(maze, freeChar, startChar, exitChar)
    print(graph)
    shortest_path = a_star_algorithm(graph, start, exit, manhattan_distance)
    print(shortest_path)
    maze_with_path = trace_path_in_maze(maze, shortest_path, pathChar)
    dispMaze(maze_with_path)
    number_attempts(maze_with_path, pathChar)
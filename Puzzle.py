# Name: Peter Orndoff
# Description: CS 325 A8
# Date: March 4th 2023

def solve_puzzle(puzzle, start, end):


    if puzzle[start[0]][start[1]] == '#':
        return None

    num_rows = len(puzzle)
    num_colum = len(puzzle[0])

    new_puzzle = puzzle_converter(puzzle, num_rows, num_colum)
    graph = puzzle_graph_converter(new_puzzle, num_rows, num_colum)
    start = start[0] * num_colum + start[1]
    int_end = end[0] * num_colum + end[1]

    if new_puzzle[end[0]][end[1]] is None:
        return None

    if len(graph[int_end]) == 0 or len(graph[start]) == 0:
        return None

    else:
        bfs_path = BFS(graph, start, int_end)
        path = path_get(new_puzzle, bfs_path, num_rows, num_colum)
        directional_path = get_directions(path)

    return path, directional_path


def path_get(puzzle, bfs_path, num_rows, num_columns, i=None, j=None, path=None, bfs_index=None, increment=None):

    if i is None:
        increment = 0
        i = 0
        j = 0
        bfs_index = 0
        path = []

    if bfs_path is None:
        return None

    if increment == len(bfs_path):
        return path

    if puzzle[i][j] == bfs_path[increment]:
        path.append((i, j))
        i = 0
        j = 0
        increment += 1
        return path_get(puzzle, bfs_path, num_rows, num_columns, i, j, path, bfs_index, increment)

    if j == num_columns - 1:
        j = 0
        i += 1
        return path_get(puzzle, bfs_path, num_rows, num_columns, i, j, path, bfs_index, increment)

    else:
        j += 1
        return path_get(puzzle, bfs_path, num_rows, num_columns, i, j, path, bfs_index, increment)


def puzzle_converter(puzzle, num_rows, num_columns, i=None, j=None, integer=None, num_graph=None):

    if i is None:
        i = 0
        j = 0
        integer = 0
        num_graph = [[0 for i in range(num_columns)] for i in range(num_rows)]

    if integer == num_rows * num_columns:
        return num_graph

    if j == num_columns:
        j = 0
        i += 1
        return puzzle_converter(puzzle, num_rows, num_columns, i, j, integer, num_graph)

    if puzzle[i][j] == '#':
        num_graph[i][j] = None

        if j == num_columns - 1:
            i += 1
            j = 0
            integer += 1
            return puzzle_converter(puzzle, num_rows, num_columns, i, j, integer, num_graph)

        else:
            j += 1
            integer += 1
            return puzzle_converter(puzzle, num_rows, num_columns, i, j, integer, num_graph)

    num_graph[i][j] = integer
    integer += 1
    j += 1

    return puzzle_converter(puzzle, num_rows, num_columns, i, j, integer, num_graph)


def puzzle_graph_converter(puzzle, num_rows, num_colum, graph=None, increment=None, j=None, i=None):

    if graph is None:
        graph = {}
        increment = 0
        i = 0
        j = 0

    while increment < num_colum * num_rows:
        value = puzzle[i][j]

        if value is not None:
            graph[value] = adjacent(puzzle, num_rows, num_colum, i, j)

        if j == num_colum - 1:
            j = 0
            i += 1
        else:
            j += 1

        increment += 1

    return graph


def adjacent(puzzle, num_rows, num_colum, i, j, adj=None):

    if adj is None:
        adj = []

    if 0 <= i < num_rows:
        if i == num_rows - 1:

            top_row = puzzle[i - 1][j]

            if top_row is None:
                pass
            else:
                adj.append(top_row)

        elif i != 0:

            bottom_row = puzzle[i + 1][j]
            top_row = puzzle[i - 1][j]

            if bottom_row and top_row is not None:
                adj.append(top_row)
                adj.append(bottom_row)
            elif top_row is None and bottom_row is not None:
                adj.append(bottom_row)
            elif bottom_row is None and top_row is not None:
                adj.append(top_row)

        else:
            bottom_row = puzzle[i + 1][j]

            if bottom_row == None:
                pass
            else:
                adj.append(bottom_row)

    if 0 <= j < num_colum:
        if j == num_colum - 1:
            left_column = puzzle[i][j - 1]

            if left_column is None:
                pass
            else:
                adj.append(left_column)

        elif j != 0:

            right_column = puzzle[i][j + 1]
            left_column = puzzle[i][j - 1]

            if right_column and left_column is not None:
                adj.append(right_column)
                adj.append(left_column)

            elif right_column is None and left_column is not None:
                adj.append(left_column)

            elif left_column is None and right_column is not None:
                adj.append(right_column)

        else:
            right_column = puzzle[i][j + 1]

            if right_column is None:
                pass
            else:
                adj.append(right_column)

    return adj



def BFS(graph, start, goal):

    explored = []

    # Queue for  BFS
    queue = [[start]]

    if start == goal:
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path

            explored.append(node)

def get_directions(tuples):

    cardinal = ''

    past_vector = tuples[0]
    current_vector = tuples[0]

    vectors = [[0, 0], [1, 0], [0, 1], [1, 1]]

    for k in range(len(tuples)):


        if current_vector[0] != past_vector[0]:
            cardinal += 'R'

        if current_vector[1] != past_vector[1]:

            if current_vector[1] > past_vector[1]:
                cardinal += 'D'
            else:
                cardinal += 'U'

        if k+1 == len(tuples):
            return cardinal

        else:
            past_vector = tuples[k]
            current_vector = tuples[k+1]

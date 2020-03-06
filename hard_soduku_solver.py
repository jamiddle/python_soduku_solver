"""puzzle must be a list of lists to replicate 8x8 grid"""

puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8],
          [0, 8, 0, 0, 9, 0, 0, 3, 0],
          [2, 0, 0, 0, 0, 5, 4, 0, 0],
          [4, 0, 0, 0, 0, 1, 8, 0, 0],
          [0, 3, 0, 0, 7, 0, 0, 4, 0],
          [0, 0, 7, 9, 0, 0, 0, 0, 3],
          [0, 0, 8, 4, 0, 0, 0, 0, 6],
          [0, 2, 0, 0, 5, 0, 0, 8, 0],
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]

solution = [[3, 4, 6, 1, 2, 7, 9, 5, 8],
            [7, 8, 5, 6, 9, 4, 1, 3, 2],
            [2, 1, 9, 3, 8, 5, 4, 6, 7],
            [4, 6, 2, 5, 3, 1, 8, 7, 9],
            [9, 3, 1, 2, 7, 8, 6, 4, 5],
            [8, 5, 7, 9, 4, 6, 2, 1, 3],
            [5, 9, 8, 4, 1, 3, 7, 2, 6],
            [6, 2, 4, 7, 5, 9, 3, 8, 1],
            [1, 7, 3, 8, 6, 2, 5, 9, 4]]


def sudoku_solver(puzzle):
    rows = {}
    columns = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
    """grid (row_possibles, column_possibles): nums_in_grid"""
    grids = {((0, 1, 2), (0, 1, 2)): [], ((0, 1, 2), (3, 4, 5)): [], ((0, 1, 2), (6, 7, 8)): [],
             ((3, 4, 5), (0, 1, 2)): [], ((3, 4, 5), (3, 4, 5)): [], ((3, 4, 5), (6, 7, 8)): [],
             ((6, 7, 8), (0, 1, 2)): [], ((6, 7, 8), (3, 4, 5)): [], ((6, 7, 8), (6, 7, 8)): []}
    remaining_values = {}
    possible_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row_counter = 0
    for list in puzzle:
        rows[row_counter] = list
        row_counter += 1

    for list in puzzle:
        column_counter = 0
        for char in list:
            if column_counter <= 8:
                columns[column_counter].append(char)
                column_counter += 1

    for key in grids.keys():
        for i in range(9):
            for j in range(9):
                if i in key[0] and j in key[1]:
                    grids[key].append(rows[i][j])

    for i in range(9):
        for j in range(9):
            """rows[i][j] refers to each individual number in grid"""
            remaining_values[(i, j)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while True:

        for key in grids.keys():
            for i in range(9):
                for j in range(9):
                    if i in key[0] and j in key[1]:
                        this_grid = grids[key]
                        for num in possible_nums:
                            if num in rows[i] or num in columns[j] or num in this_grid:
                                if num in remaining_values[(i, j)]:
                                    remaining_values[(i, j)].remove(num)
                            if len(remaining_values[(i, j)]) == 1:
                                rows[i][j] = remaining_values[(i, j)][0]

        done = [v for v in remaining_values.values() if len(v) == 1]
        two_possibilities = [v for v in remaining_values.values() if len(v) == 2]

        if len(two_possibilities) > 0:
            for k, v in remaining_values.items():
                """if [2, 5] == [2, 5]"""
                if two_possibilities[0] == v:
                    print(k[0])
                    print(k[1])
                    print(two_possibilities[0][0])
                    rows[[k[0]][k[1]]] = two_possibilities[0][0]
                    print(rows[[k[0]][k[1]]])
        else:
            print("DONE")
            break

        for i in range(9):
            for j in range(9):
                print(remaining_values[(i, j)])

    #     for i in two_possibilities:
    #         for k, v in remaining_values.items():
    #             if i == v:
    #                 print(k)
    #                 print(i)
    #     print(two_possibilities)

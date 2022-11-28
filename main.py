def empty_finder(sudoku):
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == -1:
                return r,c


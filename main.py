def empty_finder(sudoku):
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == -1:
                return r,c

    return None,None

def validity(sudoku,sol,r,c):
    rval = sudoku[r]
    if sol in rval:
        return False
    cval =[]
    for i in range(9):
        cval.append(sudoku[i][c])
    if sol in cval:
        return False

    r_i=(r//3)*3
    c_i=(c//3)*3
    for i in range(r_i,r_i +3):
        for j in range(c_i,c_i+3):
            if sudoku[i][j]==sol:
                return False

    return True

def solve_sudoku(sudoku):
    r,c = empty_finder(sudoku)
    if r is None:
        return True
    for sol in range(1,10):
        if validity(sudoku,sol,r,c):
            sudoku[r][c]=sol
            if solve_sudoku(sudoku):
                return True

        sudoku[r][c]= -1
    return False





def find_next_empty(puzzle):
    # fint the next row,col on the puzzle that is not empty
    # and what location
    # and what index
    # also if the sudoku is completed
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c


    return None, None # there are no spaces left in pzzle 
    
def is_valid(puzzle, guess, row,col):
    # figures out weather the guess at the row/col is valid or not
    # retrun True if valid else false
    # starting with row

    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = []
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # now the square
    # find the starting index of the row of that matrix and find the starting index of the col of that matrix
    # and iterate over the 3 values in the row/col
    row_start = (row//3) * 3 # 1//3 = 0 , 5 // 3 = 1
    col_start = (col//3) * 3 # same as above

    for r in range(row_start, row_start + 3): # because we iterate for 3 rows
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # if we get here then checks pass
    return True 


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    # if there is nowhere left then we're done
    if row is None:
        return True
    
    # if there is place to put our guess then we need to make a guess from 1->9
    for guess in range(1, 10):
        # check if the guess is valid
        if is_valid(puzzle, guess, row,col):
            # step if this is valid, then place then palce this value on the puzzle
            puzzle[row][col] = guess
            # now call our function recursively
            if solve_sudoku(puzzle):
                return True

        # if our guess is not valid then remove our value and redo
        # backtrack
        puzzle[row][col] = -1 #reset

    # if no numbers are pussible then this is unsolvable
    return False









if __name__ == '__main__':
    # example_board = [
    #     [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
    #     [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
    #     [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

    #     [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
    #     [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
    #     [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

    #     [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
    #     [6, 7, -1,   1, -1, 5,   -1, 4, -1],
    #     [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    # ]
        example_board = [
        [6, 7, 2,   -1, -1, 3,   -1, -1, 4],
        [-1, 3, 1,   -1, -1, -1,   2, 5, -1],
        [-1, 4, -1,   -1, -1, -1,   -1, 1, 3],

        [1, -1, 7,   -1, 4, -1,   -1, -1, -1],
        [3, 9, -1,   -1, -1, -1,   -1, 4, 5],
        [2, -1, -1,   -1, 7, 5,   1, -1, 6],

        [-1, -1, 5,   -1, 9, 6,   3, 7, 8],
        [-1, 6, -1,   5, -1, 8,   -1, -1, 9],
        [9, -1, -1,   -1, -1, 7,   5, -1, 1]
    ]

if solve_sudoku(example_board):
    for row in range(9):
        print(example_board[row])
else:
     print('Not Solvable')

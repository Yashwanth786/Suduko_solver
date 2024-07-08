import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

solutions = []

def possible(row, column, number):
    global grid
    # Is the number appearing in the given row?
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # Is the number appearing in the given column?
    for i in range(0, 9):
        if grid[i][column] == number:
            return False

    # Is the number appearing in the given square?
    x_0 = (column // 3) * 3
    y_0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y_0 + i][x_0 + j] == number:
                return False

    return True

def solve():
    global grid, solutions
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return

    solutions.append(np.matrix(grid))

solve()

if solutions:
    for solution in solutions:
        print(solution)
        input('Press enter once again for one more possible solution')
    print("No other solutions.")
else:
    print("No solution exists.")

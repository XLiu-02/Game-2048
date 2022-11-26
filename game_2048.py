import random
import numpy as np


def start_game():
    # declaring an empty list then appending 4 list each with four elements 0
    grid = np.zeros((4, 4))

    # printing controls for user
    print("Commands are as follows : ")
    print("'w' : Move Up")
    print("'s' : Move Down")
    print("'a' : Move Left")
    print("'d' : Move Right")

    # calling the function to add a new random 2 in grid after every step
    get_new_2(grid)
    return grid


# function to add a new random 2 in grid at any empty cell
def get_new_2(grid):
    # choosing a random index for row and column.
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    # random cell chosen need to be empty
    while grid[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    # place a 2 at that empty random cell
    grid[r][c] = 2


# matrix manipulation functions

# all the functions defined below are for left swap initially.

# compress grid before merge
def compress(grid):
    # bool variable to determine any change happened or not
    changed = False
    # empty grid with all cells empty
    new_grid = np.zeros((4, 4))
    # shift entries of each cell to extreme left row by row
    # loop to traverse rows
    for i in range(4):
        pos = 0
        # loop to traverse each column in respective row
        for j in range(4):
            # if cell is non-empty then we will shift the number to
            # previous empty cell in that row,denoted by pos variable
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                if j != pos:  # not the same position
                    changed = True
                pos += 1
    # returning new compressed matrix and the flag variable.
    return new_grid, changed


# function to merge the cells in grid after compressing
def merge(grid):
    changed = False

    for i in range(4):
        for j in range(3):
            # if current cell has same value as next cell in the row and they are non empty then
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                # double current cell value and empty the next cell
                grid[i][j] *= 2
                grid[i][j + 1] = 0
                # bool variable to indicate the new grid after merging is different
                changed = True

    return grid, changed


# function to reverse the matrix means reversing the content of each row (= )
def reverse(grid):
    new_grid = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[i][3 - j]
    return new_grid


# function to get the transpose of matrix means interchanging rows and column
def transpose(grid):
    new_grid = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            new_grid[i][j] = grid[j][i]
    return new_grid


# function to update the matrix if we move / swipe left
def move_left(grid):
    # first compress the grid
    new_grid, changed1 = compress(grid)

    # then merge the cells.
    new_grid, changed2 = merge(new_grid)

    changed = changed1 or changed2

    # again compress after merging.
    new_grid, temp = compress(new_grid)

    # return new matrix and bool changed telling whether the grid is same or different
    return new_grid, changed


# function to update the matrix if we move / swipe right
def move_right(grid):
    # to move right we just reverse the matrix
    new_grid = reverse(grid)

    # then move left
    new_grid, changed = move_left(new_grid)

    # then again reverse matrix will give us desired result
    new_grid = reverse(new_grid)
    return new_grid, changed


# function to update the matrix if we move / swipe up
def move_up(grid):
    # to move up we just take transpose of matrix
    new_grid = transpose(grid)

    # then move left then
    new_grid, changed = move_left(new_grid)

    # again take transpose will give desired results
    new_grid = transpose(new_grid)

    return new_grid, changed


# function to update the matrix if we move / swipe down
def move_down(grid):
    # to move down we take transpose
    new_grid = transpose(grid)

    # move right and then again
    new_grid, changed = move_right(new_grid)

    # again take transpose will give desired results.
    new_grid = transpose(new_grid)

    return new_grid, changed


# function to get the state of game
def get_state(grid):
    # if any cell contains 2048: win the game
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return 'You win!'

    # if we are still left with at least one empty cell，game continues
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return 'Game Continue'

    # or if no cell is empty now, but if after any move left, right, up or down, if any two cells
    # get merged and create an empty cell then you can continue the game

    for i in range(3):
        for j in range(3):
            if grid[i][j] == grid[i + 1][j] or grid[i][j] == grid[i][j + 1]:
                return 'Game Continue'

    # else you lost the game
    return 'Lost. Game Over!'

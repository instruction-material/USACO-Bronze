###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# http://www.usaco.org/index.php?page=viewproblem2&cpid=689


def read_input():
    f = open("cowtip.in")
    text = f.readlines()
    f.close()

    grid = []
    for i in range(1, len(text)):
        grid_row = []
        for num in text[i].strip():
            grid_row.append(int(num))
        grid.append(grid_row)

    return grid


# flipGrid(grid, maxI, maxJ) flips the grid inside of the (maxI,maxJ) coordinate
def flip_grid(grid, max_i, max_j):
    for i in range(0, max_i + 1):
        for j in range(0, max_j + 1):
            if grid[i][j] == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid


# isDone(grid) checks whether all the cows are upright (i.e. all 0s)
def is_done(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == 1:
                return False
    return True


# minFlips(grid) calculates the minimum number of flips to upright the cows,
# using the following algorithm:
# 1. start tipping from the bottom right corner.
# 2. keep searching to the left.
# 3. when an entire row is searched, move up to the next row.


def min_flips(grid):
    # edge case: all cows are already upright
    if is_done(grid):
        return 0

    num_flips = 0
    while True:
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid) - 1, -1, -1):
                if grid[i][j] == 1:
                    grid = flip_grid(grid, i, j)
                    num_flips += 1

                    if is_done(grid):
                        return num_flips


def write_output(num_flips):
    f = open("cowtip.out", "w")
    f.write(str(num_flips) + "\n")
    f.close()


grid = read_input()
num_flips = min_flips(grid)
write_output(num_flips)

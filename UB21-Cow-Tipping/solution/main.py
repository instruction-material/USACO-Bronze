# http://www.usaco.org/index.php?page=viewproblem2&cpid=689

def readInput():
    f = open("cowtip.in")
    text = f.readlines()
    f.close()

    grid = []
    for i in range(1,len(text)):
        gridRow = []
        for num in text[i].strip():
            gridRow.append(int(num))
        grid.append(gridRow)

    return grid

# flipGrid(grid, maxI, maxJ) flips the grid inside of the (maxI,maxJ) coordinate
def flipGrid(grid, maxI, maxJ):
    for i in range(0,maxI+1):
        for j in range(0,maxJ+1):
            if grid[i][j] == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid

# isDone(grid) checks whether all the cows are upright (i.e. all 0s)
def isDone(grid):
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if grid[i][j] == 1:
                return False
    return True

# minFlips(grid) calculates the minimum number of flips to upright the cows, 
# using the following algorithm:
# 1. start tipping from the bottom right corner.
# 2. keep searching to the left.
# 3. when an entire row is searched, move up to the next row.

def minFlips(grid):
    # edge case: all cows are already upright
    if isDone(grid):
        return 0
    
    numFlips = 0
    while True:
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid)-1, -1, -1):
                if grid[i][j] == 1:
                    grid = flipGrid(grid,i,j)
                    numFlips += 1
                    
                    if isDone(grid):
                        return numFlips

def writeOutput(numFlips):
    f = open("cowtip.out","w")
    f.write(str(numFlips) + "\n")
    f.close()

grid = readInput()
numFlips = minFlips(grid)
writeOutput(numFlips)

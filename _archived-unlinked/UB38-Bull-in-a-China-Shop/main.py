# http://usaco.org/index.php?page=viewproblem2&cpid=640

def readInput():
    f = open('bcs.in')
    data = f.readlines()
    n, k = data[0].split()
    n, k = int(n), int(k)
    goal = processGrid(data[1:n+1])
    grids = []
    for i in range(n+1, len(data), n):
        grids.append(processGrid(data[i:i+n]))
    return n, k, goal, grids

def processGrid(grid):
    out = []
    for line in grid:
        out.append([char for char in line.strip()])
    return out

def main(n, k, goal, grids):
    for i in range(k):
        for j in range(i+1, k):
            for idx in range(-n+1, n):
                for idy in range(-n+1, n):
                    for jdx in range(-n+1, n):
                        for jdy in range(-n+1, n):
                            good = True
                            x = 0
                            while good and x < n:
                                y = 0
                                while good and y < n:
                                    iLoc = getPosition(grids[i], idx + x, idy + y)
                                    jLoc = getPosition(grids[j], jdx + x, jdy + y)
                                    if iLoc and jLoc:
                                        good = False
                                    if (goal[x][y] == "#") != (iLoc or jLoc):
                                        good = False
                                    y += 1
                                x += 1
                            if good:
                                return i + 1, j + 1
    assert False

def getPosition(grid, x, y):
    return x >=0 and x < len(grid) and y >= 0 and y < len(grid[x]) and grid[x][y] == "#"

def writeOut(x, y):
    fout = open("bcs.out", "w")
    fout.write(str(x) + " " + str(y) + "\n")
    fout.close()

n, k, goal, grids = readInput()
x, y = main(n, k, goal, grids)
writeOut(x,y)

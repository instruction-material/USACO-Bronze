# http://www.usaco.org/index.php?page=viewproblem2&cpid=617

def readInput():
    fin = open("balancing.in")
    data = fin.readlines()
    fin.close()

    coordinates = []
    for i in range(1,len(data)):
        coord = data[i].split()
        x = int(coord[0])
        y = int(coord[1])
        coordinates.append([x,y])
    return coordinates

# calculates the maximum number of cows in a region given a and b
def calcMaxCowsInRegion(a,b, coordinates):
    # numCows[0] stores number of cows where x>a and y>b, etc.
    numCows = [0, 0, 0, 0]
    
    for coord in coordinates:
        x = coord[0]
        y = coord[1]

        if x > a and y > b:
            numCows[0] += 1
        elif x > a and y < b:
            numCows[1] += 1
        elif x < a and y > b:
            numCows[2] += 1
        else:
            numCows[3] += 1

    return max(numCows)

# calculates the minimum number of cows in a region, checking all values for
# a that are to the right of a cow, and all values of b that are above a cow
# (this limits the search space so the program can run within time bounds)
def calcMinCows(coordinates):
    minCows = len(coordinates)
    xCoords = set()
    yCoords = set()

    for coord in coordinates:
        xCoords.add(coord[0])
        yCoords.add(coord[1])

    for x in xCoords:
        for y in yCoords:
            numCows = calcMaxCowsInRegion(x+1,y+1,coordinates)
            minCows = min(minCows, numCows)

    return minCows

def writeOutput(minCows):
    fout = open("balancing.out", "w")
    fout.write(str(minCows) + "\n")
    fout.close()

coordinates = readInput()
minCows = calcMinCows(coordinates)
writeOutput(minCows)

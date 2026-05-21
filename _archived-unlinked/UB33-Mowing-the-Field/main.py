# http://www.usaco.org/index.php?page=viewproblem2&cpid=593

# returns list of direction-step pairs
def readInput():
    fin = open("mowing.in")
    data = fin.readlines()
    fin.close()

    directions = []
    for i in range(1,len(data)):
        direction = data[i].split()[0]
        numSteps = int(data[i].split()[1])
        directions.append([direction, numSteps])
    return directions

def calcMaxTime(directions):
    # use dictionary where keys are coords and values are the last time this coord was visited
    coords = {}
    x = 0
    y = 0
    t = 0
    maxTime = 10 * 100

    for line in directions:
        direction = line[0]
        numSteps = line[1]

        if (direction == "N"):
            for i in range(numSteps):
                coord = str(x) + "," + str(y)
                if coord in coords:
                    prevTime = coords[coord]
                    if t-prevTime < maxTime:
                        maxTime = t-prevTime
                coords[coord] = t
                t += 1
                y += 1
        elif (direction == "S"):
            for i in range(numSteps):
                coord = str(x) + "," + str(y)
                if coord in coords:
                    prevTime = coords[coord]
                    if t-prevTime < maxTime:
                        maxTime = t-prevTime
                coords[coord] = t
                t += 1
                y -= 1
        elif (direction == "W"):
            for i in range(numSteps):
                coord = str(x) + "," + str(y)
                if coord in coords:
                    prevTime = coords[coord]
                    if t-prevTime < maxTime:
                        maxTime = t-prevTime
                coords[coord] = t
                t += 1
                x -= 1
        elif (direction == "E"):
            for i in range(numSteps):
                coord = str(x) + "," + str(y)
                if coord in coords:
                    prevTime = coords[coord]
                    if t-prevTime < maxTime:
                        maxTime = t-prevTime
                coords[coord] = t
                t += 1
                x += 1

    if maxTime == 10 * 100:
        maxTime = -1

    return maxTime

# writes output
def writeOutput(maxTime):
    fout = open("mowing.out", "w")
    fout.write(str(maxTime) + "\n")
    fout.close()

directions = readInput()
maxTime = calcMaxTime(directions)
writeOutput(maxTime)

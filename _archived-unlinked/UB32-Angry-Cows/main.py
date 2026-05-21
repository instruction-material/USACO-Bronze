# http://www.usaco.org/index.php?page=viewproblem2&cpid=592

# returns list of hay bale locations
def readInput():
    fin = open("angry.in")
    data = fin.readlines()
    fin.close()

    locations = []
    for i in range(1,len(data)):
        locations.append(int(data[i]))

    return sorted(locations)

# calculate the number of explosions a cow launched at start will cause
def calcExplosions(start, locations):

    # calculate the furthest left the explosion can propagate
    blastRadius = 1
    currentPos = start
    while True:
        continueExplosion = False
        newPos = currentPos
        for i in range(currentPos-1, currentPos-blastRadius-1, -1):
            if i in locations:
                continueExplosion = True
                newPos = i
        if not continueExplosion:
            break
        else:
            currentPos = newPos
            blastRadius += 1
    leftBound = currentPos

    # calculate the furthest right the explosion can propagate
    blastRadius = 1
    currentPos = start
    while True:
        continueExplosion = False
        newPos = currentPos
        for i in range(currentPos+1, currentPos+blastRadius+1):
            if i in locations:
                continueExplosion = True
                newPos = i
        if not continueExplosion:
            break
        else:
            currentPos = newPos
            blastRadius += 1
    rightBound = currentPos

    # calculate the number of cows between leftBound and rightBound
    numExplosions = 0
    for i in range(leftBound, rightBound+1):
        if i in locations:
            numExplosions += 1  

    return numExplosions

# check each hay bale for how many explosions a cow launched onto it will cause
def calcMaxExplosions(locations):
    maxExplosions = 0
    for i in locations:
        numExplosions = calcExplosions(i, locations)
        if numExplosions > maxExplosions:
            maxExplosions = numExplosions
    return maxExplosions

# writes output
def writeOutput(maxExplosions):
    fout = open("angry.out", "w")
    fout.write(str(maxExplosions) + "\n")
    fout.close()

locations = readInput()
maxExplosions = calcMaxExplosions(locations)
writeOutput(maxExplosions)

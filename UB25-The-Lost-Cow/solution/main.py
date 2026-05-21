# http://www.usaco.org/index.php?page=viewproblem2&cpid=735

def readInput():
    f = open("lostcow.in")
    text = f.readlines()
    f.close()

    startingPos = int(text[0].split()[0])
    bessiePos = int(text[0].split()[1])

    return startingPos, bessiePos

def main(startingPos, bessiePos):
    # continue the zig-zag search strategy until Farmer John reaches or passes Bessie
    distanceFromX = 1
    distTraveled = 0
    currPos = startingPos
    while True:
        newPos = startingPos + distanceFromX
        distTraveled += abs(newPos-currPos)
        currPos = newPos
        distanceFromX *= -2

        # make sure we update distTraveled properly if Farmer John overshot Bessie
        if currPos == bessiePos:
            break
        elif currPos < bessiePos and startingPos > bessiePos:
            distTraveled -= abs(currPos-bessiePos)
            break
        elif currPos > bessiePos and startingPos < bessiePos:
            distTraveled -= abs(currPos-bessiePos)
            break
    return distTraveled

def writeOutput(distTraveled):
    f = open("lostcow.out","w")
    f.write(str(distTraveled) + "\n")
    f.close()

startingPos, bessiePos = readInput()
distTraveled = main(startingPos, bessiePos)
writeOutput(distTraveled)

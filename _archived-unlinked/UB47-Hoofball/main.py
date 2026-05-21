# http://usaco.org/index.php?page=viewproblem2&cpid=808

def readInput():
    fin = open("hoofball.in")
    data = fin.readlines()
    fin.close()

    cows = data[1].split()
    cows = [int(x) for x in cows]

    return sorted(cows)

# returns the index of the nearest cow to cowIndex
def getNearestCow(cowIndex, cows):
    if cowIndex == 0:
        return 1
    elif cowIndex == len(cows)-1:
        return len(cows)-2
    else:
        leftDist = cows[cowIndex]-cows[cowIndex-1]
        rightDist = cows[cowIndex+1]-cows[cowIndex]

        # in case of ties, the cow throws left
        if rightDist < leftDist:
            return cowIndex+1
        else:
            return cowIndex-1

def main(cows):
    # create a dictionary where the key is the cowIndex and the value is the
    # index of the nearest cow to cowIndex
    nearest = {}
    for i in range(0,len(cows)):
        nearest[i] = getNearestCow(i, cows)
    
    # check whether each cow is isolated (i.e. would not receive a ball),
    # in which case it would need a ball passed to it to start
    numBalls = 0
    for cowIndex in nearest:
        receivesPass = False
        # check whether cow to the left will pass to it
        if cowIndex > 0:
            if nearest[cowIndex-1] == cowIndex:
                receivesPass = True
        # check whether cow to the right will pass to it
        if cowIndex < len(cows)-1:
            if nearest[cowIndex+1] == cowIndex:
                receivesPass = True
        if not receivesPass:
            numBalls += 1

    # also check for pairs of cows that only pass to each other and
    # do not receive passes from anyone else (need a ball to be passed
    # to each of these pairs)
    for cowIndex in nearest:
        if nearest[cowIndex] == cowIndex+1 and nearest[cowIndex+1] == cowIndex:
            receivesPass = False
            # check if left cow in pair receives pass from left
            if cowIndex > 0 and nearest[cowIndex-1] == cowIndex:
                receivesPass = True
            # check if right cow in pair receives pass from right
            if cowIndex < len(cows)-2 and nearest[cowIndex+2] == cowIndex+1:
                receivesPass = True
            if not receivesPass:
                numBalls += 1
    
    return numBalls

def writeOutput(numBalls):
    fout = open("hoofball.out", "w")
    fout.write(str(numBalls) + "\n")
    fout.close()

cows = readInput()
numBalls = main(cows)
writeOutput(numBalls)
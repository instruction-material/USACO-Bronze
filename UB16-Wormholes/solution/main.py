"""
ID: your_id_here
LANG: PYTHON3
TASK: wormhole
"""

def readInput():
    f = open("wormhole.in")
    data = f.readlines()
    f.close()

    # read in x and y coordinates
    x = []
    y = []

    for i in range(1,len(data)):
        wormhole = data[i].split()
        x.append(int(wormhole[0]))
        y.append(int(wormhole[1]))

    return x,y

# create list where each element is the partner of wormhole i
# if unpaired, the partner is -1
def generatePartners(x,y):
    partners = []
    for i in range(len(x)):
        partners.append(-1)
    return partners

# create list where each element is the next wormhole to the right of i
def generateNextOnRight(x,y):
    nextOnRight = []
    for i in range(0,len(partners)):
        nextOnRight.append(-1)
    for i in range(0,len(partners)):
        # loop through each wormhole
        for j in range(0,len(partners)):
            # update nextOnRight if wormhole is the closest to the right
            if x[j] > x[i] and y[i] == y[j]:
                if nextOnRight[i] == -1:
                    nextOnRight[i] = j
                elif x[j] - x[i] < x[nextOnRight[i]]-x[i]:
                   nextOnRight[i] = j

    return nextOnRight

# checks whether a given pairing of wormholes results in a cycle
def cycleExists(partners, nextOnRight):
    # try starting at each wormhole and looking for a cycle
    for i in range(0,len(partners)):
        pos = i
        
        # at most, try taking N steps (where each step is a teleport + moving to the right)
        for j in range(0,len(partners)):
            # teleport to the partner wormhole
            pos = partners[pos]
            # jump to the next wormhole on the right
            pos = nextOnRight[pos]
            # stop if there's no wormhole to the right
            if pos == -1:
                break

        # if you're still at a wormhole, then there is a cycle
        if pos != -1:
            return True
        
    return False

# recursively generate all pairings of wormholes and check if each pairing results in a cycle
def main(partners, nextOnRight):
    totalSolutions = 0
    
    # find the first unpaired wormhole
    unpairedWormholeIndex = 0
    foundUnpairedWormhole = False
    for i in range(0,len(partners)):
        if partners[i] == -1:
            unpairedWormholeIndex = i
            foundUnpairedWormhole = True
            break

    # if all wormholes are already paired, check if this pairing is valid
    if not foundUnpairedWormhole:
        if cycleExists(partners, nextOnRight):
            return 1
        else:
            return 0

    # try pairing this wormhole with all other possible wormholes
    for j in range(i+1,len(partners)):
        if partners[j] == -1:
            partners[i] = j
            partners[j] = i
            totalSolutions += main(partners, nextOnRight)
            partners[i] = -1
            partners[j] = -1

    return totalSolutions

def writeOutput(totalSolutions):
    f = open("wormhole.out", "w")
    f.write(str(totalSolutions) + "\n")
    f.close()

x,y = readInput()
partners = generatePartners(x,y)
nextOnRight = generateNextOnRight(x,y)
totalSolutions = main(partners, nextOnRight)
writeOutput(totalSolutions)

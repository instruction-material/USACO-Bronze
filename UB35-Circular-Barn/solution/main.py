
# http://www.usaco.org/index.php?page=viewproblem2&cpid=616

def readInput():
    fin = open("cbarn.in")
    data = fin.readlines()
    fin.close()

    doors = []
    for i in range(1,len(data)):
        doors.append(int(data[i]))
    return doors

# calculates the amount of distance the cows travel if openDoorNum is opened
def calcDistance(openDoorNum, doors):
    distance = 0
    for i in range(0, len(doors)):
        finalDoor = i
        numCows = doors[i]
        
        # cows travel clockwise, so special case if the cow needs to go around
        if finalDoor >= openDoorNum:
            distance += (finalDoor-openDoorNum) * numCows
        else:
            distance += (len(doors)-openDoorNum + finalDoor) * numCows
    return distance

def calcMinDistance(doors):
    minDistance = 100 * len(doors) * 1000 # max num rooms * max num cows * max perimeter
    for i in range(0,len(doors)):
        distance = calcDistance(i, doors)
        minDistance = min(minDistance, distance)
    return minDistance

def writeOutput(minDistance):
    fout = open("cbarn.out", "w")
    fout.write(str(minDistance) + "\n")
    fout.close()

doors = readInput()
minDistance = calcMinDistance(doors)
writeOutput(minDistance)

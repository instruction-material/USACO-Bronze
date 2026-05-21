# http://www.usaco.org/index.php?page=viewproblem2&cpid=807

def readInput():
    f = open("teleport.in")
    data = f.readlines()
    f.close()

    data = data[0].split()
    start = int(data[0])
    end = int(data[1])
    teleport1 = int(data[2])
    teleport2 = int(data[3])

    return start, end, teleport1, teleport2

def main(start, end, teleport1, teleport2):
    # case 1: haul manure directly from start to end
    minDist = abs(end-start)

    # case 2: haul manure to teleport1, then from teleport2 to end
    newDist = abs(start-teleport1) + abs(end-teleport2)
    minDist = min(minDist, newDist)
    
    # case 3: haul manure to teleport2, then from teleport 1 to end
    newDist = abs(start-teleport2) + abs(end-teleport1)
    minDist = min(minDist, newDist)

    return minDist

def writeOutput(answer):
    f = open("teleport.out", "w+")
    f.write(str(answer) + "\n")
    f.close()

start, end, teleport1, teleport2 = readInput()
minDist = main(start, end, teleport1, teleport2)
writeOutput(minDist)

http://www.usaco.org/index.php?page=viewproblem2&cpid=759
def readInput():
    f = open("billboard.in")
    data = f.readlines()
    f.close()

    billboard1 = data[0].split()
    billboard1 = [int(x) for x in billboard1]
    billboard2 = data[1].split()
    billboard2 = [int(x) for x in billboard2]
    truck = data[2].split()
    truck = [int(x) for x in truck]

    return billboard1, billboard2, truck

def calcVisibleArea(billboard, truck):
    # get the coordinates of the blocked area of the billboard
    minX = max(billboard[0], truck[0])
    minY = max(billboard[1], truck[1])
    maxX = min(billboard[2], truck[2])
    maxY = min(billboard[3], truck[3])

    blockedArea = (maxX-minX) * (maxY-minY)

    # handle edge case where truck is entirely outside the billboard
    if truck[0] > billboard[2] or truck[2] < billboard[0] or truck[1] > billboard[3] or truck[3] < billboard[1]:
        blockedArea = 0
 
    totalArea = (billboard[2]-billboard[0]) * (billboard[3]-billboard[1])

    return totalArea-blockedArea

def writeOutput(answer):
    f = open("billboard.out", "w+")
    f.write(str(answer) + "\n")
    f.close()
    
billboard1, billboard2, truck = readInput()
visibleArea = calcVisibleArea(billboard1, truck) + calcVisibleArea(billboard2, truck)
writeOutput(visibleArea)

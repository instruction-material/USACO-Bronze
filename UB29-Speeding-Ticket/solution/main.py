# http://www.usaco.org/index.php?page=viewproblem2&cpid=568

def readInput():
    f = open("speeding.in")
    text = f.readlines()
    f.close()
    
    n = int(text[0].split()[0])
    speedLimits = generateSpeedDict(text[1:n+1])
    bessieSpeeds = generateSpeedDict(text[n+1:])

    return speedLimits, bessieSpeeds

# create a dictionary where each key is a road segment index
# and each value is the speed or speed limit at that segment
def generateSpeedDict(data):
    speedDict = {}
    roadSegment = 1

    for i in range(len(data)):
        segmentLength = int(data[i].split()[0])
        speedLimit = int(data[i].split()[1])

        for j in range(segmentLength):
            speedDict[roadSegment] = speedLimit
            roadSegment += 1

    return speedDict

def main(speedLimits, bessieSpeeds):
    # iterate through the dictionaries and calculate the max amount
    # by which Bessie exceeded the speed limit

    maxExceeds = 0
    for key in bessieSpeeds:
        speedDiff = bessieSpeeds[key] - speedLimits[key]
        maxExceeds = max(maxExceeds, speedDiff)
        
    return maxExceeds

def writeOutput(maxExceeds):
    f = open("speeding.out","w")
    f.write(str(maxExceeds) + "\n")
    f.close()

speedLimits, bessieSpeeds = readInput()
maxExceeds = main(speedLimits, bessieSpeeds)
writeOutput(maxExceeds)

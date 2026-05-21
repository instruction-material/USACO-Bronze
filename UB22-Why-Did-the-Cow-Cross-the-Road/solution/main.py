# http://usaco.org/index.php?page=viewproblem2&cpid=711

def readInput():
    f = open("crossroad.in")
    text = f.readlines()
    f.close()

    inputData = []
    for i in range(1,len(text)):
        line = text[i].split()
        line = [int(x) for x in line]
        inputData.append(line)
    return inputData

def main(inputData):
    # create two dictionaries where the keys are the cow IDs
    # lastPosition: tracks the last position (0 or 1) of each cow
    # numCrossings: tracks the number of crossings of each cow

    lastPosition = {}
    numCrossings = {}

    for line in inputData:
        cowId = line[0]
        if cowId not in lastPosition:
            lastPosition[cowId] = ''
            numCrossings[cowId] = 0

    # run through the input and update lastPosition and numCrossings
    for line in inputData:
        cowId = line[0]
        position = line[1]

        # handle case if this is the first position for this cow
        if lastPosition[cowId] == '':
            lastPosition[cowId] = position
        elif position != lastPosition[cowId]:
            lastPosition[cowId] = position
            numCrossings[cowId] += 1

    # sum total number of crossings
    totalCrossings = 0
    for key in numCrossings:
        totalCrossings += numCrossings[key]

    return totalCrossings

def writeOutput(totalCrossings):
    f = open("crossroad.out","w")
    f.write(str(totalCrossings) + "\n")
    f.close()

inputData = readInput()
totalCrossings = main(inputData)
writeOutput(totalCrossings)

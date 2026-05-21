# http://usaco.org/index.php?page=viewproblem2&cpid=713

def readInput():
    f = open("cowqueue.in")
    inputData = f.readlines()
    f.close()

    return inputData

def main(inputData):
    # create dictionary where the keys are arrival time and values are
    # total questioning times

    times = {}
    for i in range(1,len(inputData)):
        line = inputData[i].split()
        arrivalTime = int(inputData[i].split()[0])
        questioningTime = int(inputData[i].split()[1])
        if arrivalTime in times:
            times[arrivalTime] += (questioningTime)
        else:
            times[arrivalTime] = questioningTime

    latestTime = 0
    for arrivalTime in sorted(times):
        questioningTimes = times[arrivalTime]

        # if the cows cannot get questionined immediately, add questioningTimes
        # to latestTime, otherwise just update latestTime to the time it would take
        # to question these cows

        if arrivalTime < latestTime:
            latestTime += questioningTimes
        else:
            latestTime = arrivalTime + questioningTimes

    return latestTime

def writeOutput(latestTime):
    f = open("cowqueue.out","w")
    f.write(str(latestTime) + "\n")
    f.close()

inputData = readInput()
latestTime = main(inputData)
writeOutput(latestTime)

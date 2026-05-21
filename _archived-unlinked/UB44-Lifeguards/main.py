# http://www.usaco.org/index.php?page=viewproblem2&cpid=784

def readInput():
    f = open("lifeguards.in")
    data = f.readlines()
    f.close()

    # store shift times in list of pairs
    times = []
    for i in range(1,len(data)):
        line = data[i].split()
        line = [int(x) for x in line]
        times.append(line)

    # find minTime and maxTime
    minTime = 1000
    maxTime = 0
    for shift in times:
        minTime = min(shift[0], minTime)
        maxTime = max(shift[1], maxTime)

    # create dictionary of covered times, where
    # key is timepoint and value is number of lifeguards covering it
    coveredTimes = {}
    for i in range(minTime, maxTime):
        coveredTimes[i] = 0
    for shift in times:
        for time in range(shift[0], shift[1]):
            coveredTimes[time] += 1

    return times, coveredTimes

# returns amount of time covered when a given shift is removed
def checkCoveredTime(coveredTimes, startTime, endTime):
    times = coveredTimes.copy()

    # reduce number of lifeguards during this shift by 1
    for i in range(startTime, endTime):
        times[i] -= 1

    # sum up covered times
    coveredTime = 0
    for time in times:
        if times[time] > 0:
            coveredTime += 1

    return coveredTime

def main(times, coveredTimes):
    maxCoveredTime = 0

    # check how much time is covered when each shift is removed
    for shift in times:
        time = checkCoveredTime(coveredTimes, shift[0], shift[1])
        maxCoveredTime = max(maxCoveredTime, time)

    return maxCoveredTime

def writeOutput(answer):
    f = open("lifeguards.out", "w+")
    f.write(str(answer) + "\n")
    f.close()

times, coveredTimes = readInput()
maxCoveredTime = main(times, coveredTimes)
writeOutput(maxCoveredTime)

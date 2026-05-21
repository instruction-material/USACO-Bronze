"""
ID: your_id_here
LANG: PYTHON3
TASK: milk2
"""

# Returns a list of lists of start and end milking times
def readInput():
    with open("milk2.in") as fin:
        data = fin.readlines()
    times = []
    for i in range(1, len(data)):
        times.append([int(data[i].split()[0]), int(data[i].split()[1])])
    return times

# Returns an array of times when milking was active
def createArray(times):
    # Find earliest and latest time
    earliestTime = min(time[0] for time in times)
    latestTime = max(time[1] for time in times)

    # Create an array to track milking times
    milkTimes = [False] * (latestTime - earliestTime)

    # Fill the array based on when milking was active
    for time in times:
        startTime = time[0] - earliestTime
        endTime = time[1] - earliestTime
        for i in range(startTime, endTime):
            milkTimes[i] = True

    return milkTimes, earliestTime, latestTime

# Returns longest consecutive milking and non-milking times
def calcTimes(milkTimes):
    longestMilkTime = 0
    currentMilkTime = 0
    longestNoMilkTime = 0
    currentNoMilkTime = 0

    for isMilking in milkTimes:
        if isMilking:
            currentMilkTime += 1
            longestMilkTime = max(longestMilkTime, currentMilkTime)
            currentNoMilkTime = 0
        else:
            currentNoMilkTime += 1
            longestNoMilkTime = max(longestNoMilkTime, currentNoMilkTime)
            currentMilkTime = 0

    return longestMilkTime, longestNoMilkTime

# Write output
def writeOutput(longestMilkTime, longestNoMilkTime):
	fout = open("milk2.out","w")
	fout.write(str(longestMilkTime) + " " + str(longestNoMilkTime) + "\n")
	fout.close()

times = readInput()
milkTimes, earliestTime, latestTime = createArray(times)
longestMilkTime, longestNoMilkTime = calcTimes(milkTimes)
writeOutput(longestMilkTime, longestNoMilkTime)

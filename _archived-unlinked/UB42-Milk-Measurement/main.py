# http://www.usaco.org/index.php?page=viewproblem2&cpid=761

def readInput():
    f = open("measurement.in")
    data = f.readlines()
    f.close()

    # create dict where keys are the day and values are [cowName, change]
    # note that problem says he can only make one measurement on a given day
    milkLog = {}
    for i in range(1,len(data)):
        line = data[i].split()
        day = int(line[0])
        cowName = line[1]
        change = int(line[2])
        milkLog[day] = [cowName, change]

    return milkLog

def main(milkLog):
    numChanges = 0
    cows = {}
    cows["Mildred"] = 0
    cows["Elsie"] = 0
    cows["Bessie"] = 0

    topMilkers = set()
    for cow in cows:
        topMilkers.add(cow)
    
    # iterate through dict in sorted order, keeping track of top milker
    for key in sorted(milkLog):
        cowName = milkLog[key][0]
        change = milkLog[key][1]
        cows[cowName] += change

        # check if there was a change in the leader(s)
        maxMilk = 0
        for cow in cows:
            if cows[cow] > maxMilk:
                maxMilk = cows[cow]
        newLeaders = set()
        for cow in cows:
            if cows[cow] == maxMilk:
                newLeaders.add(cow)

        if newLeaders != topMilkers:
            numChanges += 1

        topMilkers = newLeaders

    return numChanges

def writeOutput(answer):
    f = open("measurement.out", "w+")
    f.write(str(answer) + "\n")
    f.close()
    
milkLog = readInput()
numChanges = main(milkLog)
writeOutput(numChanges)

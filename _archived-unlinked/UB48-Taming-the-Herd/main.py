# http://usaco.org/index.php?page=viewproblem2&cpid=809

def readInput():
    fin = open("taming.in")
    data = fin.readlines()
    fin.close()

    log = data[1].split()
    log = [int(x) for x in log]

    return log

def main(log):
    # edge case: the first entry in the log is > 0, since we know there was
    # a breakout on day 1
    if log[0] > 0:
        return -1
    
    # try to reconstruct the log with the given information
    newLog = []
    for i in range(0,len(log)):
        newLog.append(-1)

    # there was definitely a breakout on day 1
    newLog[0] = 0

    # go through the log backwards. every time we see a non-negative number,
    # try to trace back the number of breakouts
    for i in range(len(log)-1, -1, -1):
        if log[i] >= 0:
            numBreakouts = log[i]
            for j in range(i, -1, -1):
                # check for consistency
                if newLog[j] != -1 and newLog[j] != numBreakouts:
                    return -1
                else:
                    newLog[j] = numBreakouts

                numBreakouts -= 1
                if numBreakouts < 0:
                    break

    # check if log and newLog are consistent
    for i in range(0,len(log)):
        if log[i] != newLog[i] and log[i] != -1:
            return -1

    return newLog

def calcMinMax(log):
    # for the minimum number of breakouts, then only the days marked 0 had
    # a breakout (none of the -1 were breakouts)
    minBreakouts = 0
    for num in log:
        if num == 0:
            minBreakouts += 1

    # for the maximum number of breakouts, then every day marked -1 was also
    # a breakout
    maxBreakouts = minBreakouts
    for num in log:
        if num == -1:
            maxBreakouts += 1

    return minBreakouts, maxBreakouts

def writeOutput(minBreakouts, maxBreakouts):
    f = open("taming.out", "w")
    f.write(str(minBreakouts) + " " + str(maxBreakouts) + "\n")
    f.close()

def writeInconsistentOutput():
    f = open("taming.out", "w")
    f.write("-1\n")
    f.close()

log = readInput()
result = main(log)
if result == -1:
    writeInconsistentOutput()
else:
    minBreakouts, maxBreakouts = calcMinMax(result)
    writeOutput(minBreakouts, maxBreakouts)

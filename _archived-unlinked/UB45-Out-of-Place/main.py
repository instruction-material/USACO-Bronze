# http://www.usaco.org/index.php?page=viewproblem2&cpid=785
def readInput():
    f = open("outofplace.in")
    data = f.readlines()
    f.close()

    lineup = []
    for i in range(1,len(data)):
        lineup.append(int(data[i]))
    return lineup

def findNumSwaps(lineup):
    # sort the lineup and compare how many cows are out of order
    # if there are N cows out of order, it will take N-1 swaps to fix them
    sortedLineup = sorted(lineup)
    numSwaps = 0
    
    for i in range(0,len(lineup)):
        if lineup[i] != sortedLineup[i]:
            numSwaps += 1

    return numSwaps-1

def writeOutput(answer):
    f = open("outofplace.out", "w+")
    f.write(str(answer) + "\n")
    f.close()

lineup = readInput()
numSwaps = findNumSwaps(lineup)
writeOutput(numSwaps)

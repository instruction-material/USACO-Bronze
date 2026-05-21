# http://www.usaco.org/index.php?page=viewproblem2&cpid=687

def readInput():
    f = open("notlast.in")
    text = f.readlines()
    f.close()

    # create dictionary of milk amounts of each cow
    # note that cows need to be predefined in case a cow is not in the input

    cows = {
        "Bessie": 0,
        "Elsie": 0,
        "Daisy": 0,
        "Gertie": 0,
        "Annabelle": 0,
        "Maggie": 0,
        "Henrietta": 0,
    }

    for i in range(1,len(text)):
        cow = text[i].split()[0]
        milk = text[i].split()[1]
        cows[cow] += int(milk)

    return cows

# returns the second lowest amount of milk (-1 if all cows tie for the lowest amount)
def findSecondLowest(cows):
    milkAmts = []
    for cow in cows:
        milkAmts.append(cows[cow])

    milkAmts = sorted(milkAmts)
    lowest = milkAmts[0]
    secondLowest = -1
    for i in milkAmts:
        if i > lowest:
            secondLowest = i
            break

    return secondLowest

# find cow(s) associated with the second lowest amount of milk
def main(cows, secondLowest):
    numCowsFound = 0
    cowName = ''
    if secondLowest != -1:
        for cow in cows:
            if cows[cow] == secondLowest:
                numCowsFound += 1
                cowName = cow

    return cowName, numCowsFound

def writeOutput(cowName, secondLowest, numCowsFound):
    f = open("notlast.out","w")
    if secondLowest == -1:
        f.write("Tie\n")
    elif numCowsFound > 1:
       f.write("Tie\n")
    else:
        f.write(cowName + "\n")
    f.close()

cows = readInput()
secondLowest = findSecondLowest(cows)
cowName, numCowsFound = main(cows, secondLowest)
writeOutput(cowName, secondLowest, numCowsFound)

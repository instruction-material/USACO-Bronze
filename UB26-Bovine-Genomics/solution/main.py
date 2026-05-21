# http://www.usaco.org/index.php?page=viewproblem2&cpid=736

def readInput():
    f = open("cownomics.in")
    text = f.readlines()
    f.close()

    numCows = int(text[0].split()[0])
    numPositions = int(text[0].split()[1])
    spottyCows = []
    plainCows = []

    for i in range(1,numCows+1):
        spottyCows.append(text[i].strip())

    for i in range(numCows+1,len(text)):
        plainCows.append(text[i].strip())

    return spottyCows, plainCows, numPositions

def main(spottyCows, plainCows, numPositions):
    # for each position, store the plain cow genes in a set.
    # check if all the spotty cows have a different letter.
    # if they do, increase numPossibleGenes by 1.

    numPossibleGenes = 0
    for i in range(0,numPositions):
        plainCowGenes = set()
        for plainCow in plainCows:
            plainCowGenes.add(plainCow[i])

        spottyCowsHaveOtherLetters = True
        for spottyCow in spottyCows:
            if spottyCow[i] in plainCowGenes:
                spottyCowsHaveOtherLetters = False

        if spottyCowsHaveOtherLetters:
            numPossibleGenes += 1

    return numPossibleGenes

def writeOutput(numPossibleGenes):
    f = open("cownomics.out","w")
    f.write(str(numPossibleGenes) + "\n")
    f.close()

spottyCows, plainCows, numPositions = readInput()
numPossibleGenes = main(spottyCows, plainCows, numPositions)
writeOutput(numPossibleGenes)

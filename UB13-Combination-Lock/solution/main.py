"""
ID: roobeel1
LANG: PYTHON3
TASK: combo
"""

def readInput():
    f = open("combo.in")
    text = f.readlines()
    f.close()

    # read in maxNum and the two codes
    maxNum = int(text[0])
    farmerCombo = text[1].split()
    masterCombo = text[2].split()
    for i in range(3):
        farmerCombo[i] = int(farmerCombo[i])
        masterCombo[i] = int(masterCombo[i])

    return maxNum, farmerCombo, masterCombo

# function that takes in a number and generates a list of the 2 numbers above and below
def generateNumPossibilities(num, maxNum):
    nums = []

    # handle special case where maxNum <= 5
    if maxNum <= 5:
        for i in range(1,maxNum+1):
            nums.append(i)
        return nums
    
    for i in range(-2,3):
        codeNum = num + i
        if codeNum < 1:
            codeNum = maxNum + codeNum
        elif codeNum > maxNum:
            codeNum = codeNum - maxNum
        nums.append(codeNum)
    return nums

# function that generates a set of the possible combos, given a code
def generateCombos(code, maxNum):
    combos = set()
    numPossibilities = []

    for i in range(3):
        numPossibilities.append(generateNumPossibilities(code[i], maxNum))

    for i in numPossibilities[0]:
        for j in numPossibilities[1]:
            for k in numPossibilities[2]:
                combo = str(i) + '-' + str(j) + '-' + str(k)
                combos.add(combo)

    return combos

def main(maxNum, farmerCombo, masterCombo):
    # generate the possible combos for both codes
    farmerCombos = generateCombos(farmerCombo, maxNum)
    masterCombos = generateCombos(masterCombo, maxNum)

    # find the size of the union of the possible combos
    numPossibleCombos = len(farmerCombos.union(masterCombos))

    return numPossibleCombos

def writeOutput(numPossibleCombos):
    f = open("combo.out", "w")
    f.write(str(numPossibleCombos) + "\n")
    f.close()

maxNum, farmerCombo, masterCombo = readInput()
numPossibleCombos = main(maxNum, farmerCombo, masterCombo)
writeOutput(numPossibleCombos)

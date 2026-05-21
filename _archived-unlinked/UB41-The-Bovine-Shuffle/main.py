# http://www.usaco.org/index.php?page=viewproblem2&cpid=760

def readInput():
    f = open("shuffle.in")
    data = f.readlines()
    f.close()

    shuffle = data[1].split()
    shuffle = [int(x) for x in shuffle]

    finalOrder = data[2].split()
    finalOrder = [int(x) for x in finalOrder]

    return shuffle, finalOrder

# takes in the shuffle and the result of the shuffle,
# and returns the starting order
def reverseShuffle(shuffle, finalOrder):
    startingOrder = []
    for i in range(0,len(finalOrder)):
        startingOrder.append(0)

    for i in range(0,len(shuffle)):
        startingOrder[i] = finalOrder[shuffle[i]-1] # -1 because of indexing

    return startingOrder

def main(shuffle, finalOrder):
    shuffle1 = reverseShuffle(shuffle, finalOrder)
    shuffle2 = reverseShuffle(shuffle, shuffle1)
    shuffle3 = reverseShuffle(shuffle, shuffle2)

    return shuffle3

def writeOutput(finalOrder):
    f = open("shuffle.out", "w+")
    for num in finalOrder:
        f.write(str(num) + "\n")
    f.close()

shuffle, finalOrder = readInput()
startingOrder = main(shuffle, finalOrder)
writeOutput(startingOrder)

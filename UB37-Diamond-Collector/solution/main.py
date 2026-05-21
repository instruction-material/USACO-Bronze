# http://usaco.org/index.php?page=viewproblem2&cpid=639

def readInput():
    fin = open("diamond.in")
    data = fin.readlines()
    fin.close()

    k = int(data[0].split()[1])
    sizes = []
    for i in range(1,len(data)):
        sizes.append(int(data[i]))
    return sizes, k

# given the smallest diamond in a display case, find the number of diamonds
# that can be displayed alongside it
def calcNumDiamonds(minSize, sizes, k):
    numDiamonds = 0
    for diamond in sizes:
        if diamond >= minSize and diamond <= minSize + k:
            numDiamonds += 1
    return numDiamonds

def calcMaxDiamonds(sizes, k):
    # test each diamond for how many can be displayed alongside it
    maxDiamonds = 0
    for diamond in sizes:
        numDiamonds = calcNumDiamonds(diamond, sizes, k)
        maxDiamonds = max(maxDiamonds, numDiamonds)
    return maxDiamonds

def writeOutput(maxDiamonds):
    fout = open("diamond.out", "w")
    fout.write(str(maxDiamonds) + "\n")
    fout.close()

sizes, k = readInput()
maxDiamonds = calcMaxDiamonds(sizes, k)
writeOutput(maxDiamonds)

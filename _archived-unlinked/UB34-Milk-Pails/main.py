# http://www.usaco.org/index.php?page=viewproblem2&cpid=615

def readInput():
    fin = open("pails.in")
    data = fin.readlines()
    fin.close()
    
    data = data[0].split()
    x = int(data[0])
    y = int(data[1])
    m = int(data[2])
    return x, y, m

def calcMaxMilk(x, y, m):
    # try every combination of the small and medium pails
    # at most, the total number of pails has to be less than m/x
    maxMilk = 0
    maxPails = int(m/x)
    for i in range(maxPails+1):
        for j in range(maxPails-i+1):
            totalMilk = x*i + y*j
            if totalMilk <= m and totalMilk > maxMilk:
                maxMilk = totalMilk
    return maxMilk

def writeOutput(maxMilk):
    fout = open("pails.out", "w")
    fout.write(str(maxMilk) + "\n")
    fout.close()

x, y, m = readInput()
maxMilk = calcMaxMilk(x,y,m)
writeOutput(maxMilk)

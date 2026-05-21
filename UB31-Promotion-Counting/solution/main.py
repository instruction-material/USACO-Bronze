# http://www.usaco.org/index.php?page=viewproblem2&cpid=591

def readInput():
    fin = open("promote.in")
    data = fin.readlines()
    fin.close()

    participants = []
    for line in data:
        numBefore = int(line.split()[0])
        numAfter = int(line.split()[1])
        participants.append([numBefore, numAfter])
    return participants

def calcPromotions(participants):
    # promoted from G to P = num P after - num P before
    numGtoP = participants[3][1] - participants[3][0]

    # promoted from S to G = num in G or P after - num in G or P before 
    numStoG = (participants[2][1] + participants[3][1]) - (participants[2][0] + participants[3][0])

    # promoted from B to S = num in S or G or P after - num in S or G or P before
    numBtoS = (participants[1][1] + participants[2][1] + participants[3][1]) - (participants[1][0] + participants[2][0] + participants[3][0])

    return numGtoP, numStoG, numBtoS

def writeOutput(numGtoP, numStoG, numBtoS):
    fout = open("promote.out", "w")
    fout.write(str(numBtoS) + "\n")
    fout.write(str(numStoG) + "\n")
    fout.write(str(numGtoP) + "\n")
    fout.close()

participants = readInput()
numGtoP, numStoG, numBtoS = calcPromotions(participants)
writeOutput(numGtoP, numStoG, numBtoS)

def readInput():
    fin = open("reduce.in")
    data = fin.readlines()
    fin.close()

    cows = []
    for i in range(1,len(data)):
        cows.append([int(x) for x in data[i].split()])

    return cows

def main(cow):
    # we only need to keep track of 8 numbers:
    # - smallest (x1) and second smallest (x2) x coord
    # - largest (x3) and second largest (x4) x coord
    # - smallest (y1) and second smallest (y2) y coord
    # - largest (y3) and second largest (y4) coord

    x1 = 40000
    x2 = 40000
    x3 = 0
    x4 = 0
    y1 = 40000
    y2 = 40000
    y3 = 0
    y4 = 0

    for cow in cows:
        x = cow[0]
        y = cow[1]
        if x < x1:
            x2 = x1
            x1 = x
        elif x < x2:
            x2 = x
            
        if x > x3:
            x4 = x3
            x3 = x
        elif x > x4:
            x4 = x
        
        if y < y1:
            y2 = y1
            y1 = y
        elif y < y2:
            y2 = y
            
        if y > y3:
            y4 = y3
            y3 = y
        elif y > y4:
            y4 = y

    minArea = (x3-x1)*(y3-y1)

    # now, check each point and see if it is on the current fence border
    # if it is, then pretend to remove it and update to the second smallest/largest accordingly

    for cow in cows:
        x = cow[0]
        y = cow[1]

        minX = x1
        maxX = x3
        minY = y1
        maxY = y3

        if x == x1:
            minX = x2
        if x == x3:
            maxX = x4
        if y == y1:
            minY = y2
        if y == y3:
            maxY = y4

        minArea = min(minArea, (maxX-minX)*(maxY-minY))

    return minArea

def writeOutput(minArea):
    f = open("reduce.out", "w")
    f.write(str(minArea) + "\n")
    f.close()

cows = readInput()
minArea = main(cows)
writeOutput(minArea)

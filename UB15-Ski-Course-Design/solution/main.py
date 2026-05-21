"""
ID: your_id_here
LANG: PYTHON3
TASK: skidesign
"""

def readInput():
    f = open("skidesign.in")
    data = f.readlines()
    f.close()

    heights = []
    for i in range(1,len(data)):
        heights.append(int(data[i]))
    heights = sorted(heights)

    return heights

def main(heights):
    # calculate the total cost for each possible interval, starting from
    # (minHeight, lowestHeight + 17) up to (minHeight - 17, maxHeight)

    minCost = 1000 * 100**2 # make sure minCost is set reasonably
    minHeight = heights[0]
    maxHeight = minHeight + 17

    while minHeight <= heights[-1]-17:
        cost = 0
        for height in heights:
            if height < minHeight:
                cost += (height-minHeight)**2
            elif height > maxHeight:
                cost += (height-maxHeight)**2
        if cost < minCost:
            minCost = cost
        minHeight += 1
        maxHeight += 1

    return minCost

def writeOutput(minCost):
    f = open("skidesign.out", "w+")
    f.write(str(minCost) + "\n")
    f.close()

heights = readInput()
minCost = main(heights)
writeOutput(minCost)


def readInput():
    f = open("billboard.in")
    data = f.readlines()
    f.close()

    backBoard = data[0].split()
    backBoard = [int(x) for x in backBoard]
    frontBoard = data[1].split()
    frontBoard = [int(x) for x in frontBoard]

    return backBoard, frontBoard

def calcTarpArea(backBoard, frontBoard):
    backX1 = backBoard[0]
    backY1 = backBoard[1]
    backX2 = backBoard[2]
    backY2 = backBoard[3]

    frontX1 = frontBoard[0]
    frontY1 = frontBoard[1]
    frontX2 = frontBoard[2]
    frontY2 = frontBoard[3]

    numCornersCovered = 0
    if isCovered(backX1, backY1, frontX1, frontY1, frontX2, frontY2):
        numCornersCovered += 1
    if isCovered(backX1, backY2, frontX1, frontY1, frontX2, frontY2):
        numCornersCovered += 1
    if isCovered(backX2, backY1, frontX1, frontY1, frontX2, frontY2):
        numCornersCovered += 1
    if isCovered(backX2, backY2, frontX1, frontY1, frontX2, frontY2):
        numCornersCovered += 1

    # if all 4 corners are covered, then 0 area needs to be covered
    if numCornersCovered == 4:
        return 0

    backBoardWidth = backBoard[2]-backBoard[0]
    backBoardHeight = backBoard[3]-backBoard[1]
    backBoardArea = backBoardWidth * backBoardHeight

    # if 0 or 1 corners are covered, then the whole backBoard needs to be covered
    if numCornersCovered < 2:
        return backBoardArea

    # otherwise find the portion of the backBoard that needs to be covered
    else:
        xL = max(backX1, frontX1)
        xR = min(backX2, frontX2)
        yL = max(backY1, frontY1)
        yR = min(backY2, frontY2)
        return backBoardArea - (xR-xL)*(yR-yL)
    
# returns true if (x,y) is covered by the rectangle bounded by (x1,y1) and (x2,y2)
def isCovered(x, y, x1, y1, x2, y2):
    return x >= x1 and x <= x2 and y >= y1 and y <= y2

def writeOutput(answer):
    f = open("billboard.out", "w+")
    f.write(str(answer) + "\n")
    f.close()

backBoard, frontBoard = readInput()
area = calcTarpArea(backBoard, frontBoard)
writeOutput(area)

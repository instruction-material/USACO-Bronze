# http://www.usaco.org/index.php?page=viewproblem2&cpid=737

def readInput():
    f = open("art.in")
    text = f.readlines()
    f.close()

    canvas = []
    for i in range(1,len(text)):
        canvas.append(text[i].strip())

    return canvas

# checks if a given color is in the canvas
def isInCanvas(color):
    for i in range(0,len(canvas)):
        for j in range(0,len(canvas[0])):
            if color == canvas[i][j]:
                return True
    return False

# returns whether color1 is found inside the rectangle of color2
def colorInRect(color1, color2):
    # find boundaries of color2
    minRow = len(canvas)
    maxRow = 0
    minCol = len(canvas[0])
    maxCol = 0
    for i in range(0,len(canvas)):
        for j in range(0,len(canvas[0])):
            if canvas[i][j] == color2:
                if i < minRow:
                    minRow = i
                if i > maxRow:
                    maxRow = i
                if j < minCol:
                    minCol = j
                if j > maxCol:
                    maxCol = j

    # check if color1 is found inside color2
    for i in range(minRow, maxRow + 1):
        for j in range(minCol, maxCol + 1):
            if color1 == canvas[i][j]:
                return True
    return False
    
def main(canvas):
    # check each color and see if it is on top of any other rectangles.
    # if it is, then it cannot have been drawn first.

    numPossible = 0
    for color in range(1,10):
        color = str(color)
        if isInCanvas(color):
            couldBeFirst = True
            for color2 in range(1,10):
                color2 = str(color2)
                if color2 != color:
                    if colorInRect(color, color2):
                        couldBeFirst = False
            if couldBeFirst:
                numPossible += 1
    return numPossible

def writeOutput(numPossible):
    f = open("art.out","w")
    f.write(str(numPossible) + "\n")
    f.close()

canvas = readInput()
numPossible = main(canvas)
writeOutput(numPossible)

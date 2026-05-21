# http://usaco.org/index.php?page=viewproblem2&cpid=712

import string

def readInput():
    f = open("circlecross.in")
    text = f.readlines()
    f.close()

    circle = text[0].strip()
    return circle

def main(circle):
    # count the number of times a single letter appears between two letters
    # for each letter, only consider the letters that come after it to avoid
    # double-counting

    numCrossings = 0

    letters = string.ascii_uppercase
    for letter in letters:
        currentPos = circle.find(letter)
        uniqueLetters = [] # holds unique letters
        while True:
            currentPos += 1
            # handle case where circle wraps around
            if currentPos >= len(circle):
                currentPos = 0
            # break when we find the same letter again
            if circle[currentPos] == letter:
                break

            currentLetter = circle[currentPos]
            if ord(currentLetter) > ord(letter):
                # remove currentLetter from uniqueLetters if it appears twice
                if currentLetter not in uniqueLetters:
                    uniqueLetters.append(currentLetter)
                else:
                    uniqueLetters.remove(currentLetter)

        numCrossings += len(uniqueLetters)
    return numCrossings
    
def writeOutput(numCrossings):
    f = open("circlecross.out","w")
    f.write(str(numCrossings) + "\n")
    f.close()

circle = readInput()
numCrossings = main(circle)
writeOutput(numCrossings)

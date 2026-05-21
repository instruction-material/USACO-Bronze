# http://www.usaco.org/index.php?page=viewproblem2&cpid=664

from string import ascii_lowercase

def readInput():
    f = open("blocks.in")
    text = f.readlines()
    f.close()

    # save word pairings in list of lists
    words = []
    for i in range(1,len(text)):
        words.append(text[i].split())
    return words

# generates dictionary where key is letter and value is number of times
# the letter appears in the word
def countLettersInWord(word):
    letterCount = {}
    for letter in word:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    return letterCount

def main(words):
    # for each letter, save the number of times it appears most frequently
    # on either side of the block
    masterDict = {}
    for wordPair in words:
        wordOneDict = countLettersInWord(wordPair[0])
        wordTwoDict = countLettersInWord(wordPair[1])

        # iterate through all letters contained in at least one of the two words
        for letter in set(wordOneDict.keys()).union(wordTwoDict.keys()):
            
            # if the letter is in both words, add the larger count to masterDict
            if letter in wordOneDict and letter in wordTwoDict:
                maxCount = wordOneDict[letter]
                if wordTwoDict[letter] > maxCount:
                    maxCount = wordTwoDict[letter]
                
                if letter in masterDict:
                    masterDict[letter] += maxCount
                else:
                    masterDict[letter] = maxCount

            # else, just add the count from one of the words to masterDict
            else:
                maxCount = 0
                if letter in wordOneDict:
                    maxCount = wordOneDict[letter]
                else:
                    maxCount = wordTwoDict[letter]
                
                if letter in masterDict:
                    masterDict[letter] += maxCount
                else:
                    masterDict[letter] = maxCount

    return masterDict

def writeOutput(masterDict):
    f = open("blocks.out", "w")
    for letter in ascii_lowercase:
        if letter in masterDict:
            f.write(str(masterDict[letter]) + "\n")
        else:
            f.write(str(0) + "\n")
    f.close()

words = readInput()
masterDict = main(words)
writeOutput(masterDict)

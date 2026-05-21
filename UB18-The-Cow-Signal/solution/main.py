# http://www.usaco.org/index.php?page=viewproblem2&cpid=665


def readInput():
    f = open("cowsignal.in")
    text = f.readlines()
    f.close()

    factor = int(text[0].split()[2])

    signal = []
    for i in range(1,len(text)):
        signal.append(text[i].strip())

    return signal, factor

def main(signal, factor):
    # for each line, append that character n times
    # then append that line n times to newSignal
    newSignal = []
    for line in signal:
        newLine = ''
        for letter in line:
            for i in range(factor):
                newLine += letter
        for i in range(factor):
            newSignal.append(newLine)

    return newSignal

def writeOutput(newSignal):
    f = open("cowsignal.out","w")
    for line in newSignal:
        f.write(line + "\n")
    f.close()

signal, factor = readInput()
newSignal = main(signal, factor)
writeOutput(newSignal)

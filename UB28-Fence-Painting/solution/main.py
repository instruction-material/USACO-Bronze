# http://www.usaco.org/index.php?page=viewproblem2&cpid=567

def readInput():
    f = open("paint.in")
    text = f.readlines()
    f.close()

    a = int(text[0].split()[0])
    b = int(text[0].split()[1])
    c = int(text[1].split()[0])
    d = int(text[1].split()[1])

    return a,b,c,d

def main(a,b,c,d):
    # if c < a < b < d, then the length is d-c
    # if c < d < a < b, then the length is (b-a) + (d-c)
    # if c < a < d < b, then the length is (b-a) + (a-c)
    # if a < b < c < d, then the length is (b-a) + (d-c)
    # if a < c < b < d, then the length is (b-a) + (d-b)
    # if a < c < d < b, then the length ia b-a

    length = 0
    if c < a:
        if d > b:
            length = d-c
        elif a > d:
            length = (b-a) + (d-c)
        else:
            length = (b-a) + (a-c)
    else:
        if c > b:
            length = (b-a) + (d-c)
        elif b > d:
            length = b-a
        else:
            length = (b-a) + (d-b)

    return length

def writeOutput(length):
    f = open("paint.out","w")
    f.write(str(length) + "\n")
    f.close()

a,b,c,d = readInput()
length = main(a,b,c,d)
writeOutput(length)

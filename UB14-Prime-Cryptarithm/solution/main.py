"""
ID: your_id_here
LANG: PYTHON3
TASK: crypt1
"""

def readInput():
    f = open("crypt1.in")
    data = f.readlines()
    f.close()
    
    nums = data[1].strip().split()
    return nums

# generate all possible options for the two numbers that will be multipled together
def generateOptions(nums):
    numOneOptions = []
    numTwoOptions = []

    for i in nums:
        for j in nums:
            for k in nums:
                numOneOptions.append(i+j+k)

    for i in nums:
        for j in nums:
            numTwoOptions.append(i+j)

    return numOneOptions, numTwoOptions

def main(numOneOptions, numTwoOptions):
    # generate the three numbers involved in the multiplication
    # check combination for its validity
    counter = 0
    for i in numOneOptions:
        for j in numTwoOptions:
            num1 = i
            num2 = j

            row1 = int(num1) * int(num2[1])
            row2 = int(num1) * int(num2[0])
            product = int(num1) * int(num2)

            isValid = True

            # make sure that each number is the correct number of digits
            if row1 > 999 or row2 > 999 or product > 9999:
                isValid = False

            row1 = str(row1)
            row2 = str(row2)
            product = str(product)

            # check that each number only contains valid digits
            for k in row1:
                if k not in nums:
                    isValid = False

            for k in row2:
                if k not in nums:
                    isValid = False

            for k in product:
                if k not in nums:
                    isValid = False

            if isValid:
                counter += 1

    return counter

def writeOutput(answer):
    f = open("crypt1.out", "w+")
    f.write(str(answer) + "\n")
    f.close()

nums = readInput()
numOneOptions, numTwoOptions = generateOptions(nums)
answer = main(numOneOptions, numTwoOptions)
writeOutput(answer)

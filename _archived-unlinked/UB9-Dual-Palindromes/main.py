"""
ID: your_id_here
LANG: PYTHON3
TASK: dualpal
"""

def readInput():
	fin = open('dualpal.in')
	text = fin.readlines()
	fin.close()

	numNumbers = int(text[0].split()[0])
	minNumber = int(text[0].split()[1])
	return numNumbers, minNumber

# converts num in base 10 to new base
def convertBase(num, newBase):
	letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J'}
	remainingNum = num
	result = ''
	while remainingNum != 0:
		quotient = int(remainingNum/newBase)

		if quotient == 0:
			remainder = remainingNum
		else:
			remainder = remainingNum % newBase

		if remainder > 9:
			remainder = letters[remainder]

		result = str(remainder) + result
		remainingNum = quotient
		
	return result

def writeOutput(numNumbers, minNumber):
	fout = open('dualpal.out', 'w')

	currentNum = minNumber + 1
	numCounter = 0
	while numCounter < numNumbers:
		palindromeCounter = 0
		
		for base in range(2,11):
			num = convertBase(currentNum, base)
			if num == num[::-1]:
				palindromeCounter += 1

		if palindromeCounter >= 2:
			fout.write(str(currentNum) + '\n')
			numCounter += 1

		currentNum += 1

	fout.close()

numNumbers, minNumber = readInput()
writeOutput(numNumbers, minNumber)

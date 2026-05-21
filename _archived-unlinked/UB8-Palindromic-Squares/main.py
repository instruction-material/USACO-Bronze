"""
ID: your_id_here
LANG: PYTHON3
TASK: palsquare
"""

# read in base
def readInput():
	fin = open('palsquare.in')
	data = fin.readlines()
	fin.close()
	base = int(data[0].strip())
	return base

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

def writeOutput(base):
	fout = open('palsquare.out', 'w+')
	for i in range(1,301):
		num = convertBase(i, base)
		square = convertBase(i*i, base)

		if square == square[::-1]:
			fout.write(str(num) + ' ' + square + '\n')
	fout.close()

base = readInput()
writeOutput(base)

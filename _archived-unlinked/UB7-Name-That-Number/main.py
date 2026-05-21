"""
ID: your_id_here
LANG: PYTHON3
TASK: namenum
"""

def readInput():
	fin = open('dict.txt')
	names = fin.readlines()
	fin.close()

	fin = open('namenum.in')
	data = fin.readlines()
	fin.close()
	brandNum = data[0].strip()
	
	return names, brandNum

# writes valid names to the output file
def translateNames(names, brandNum):
	fout = open('namenum.out', 'w')
	foundValidName = False

	for name in names:
		name = name.strip()
		nameNum = ''
		for letter in name:
			num = 0
			# special case for after Q
			if ord(letter) > ord('Q'):
				num = int((ord(letter)-66)/3) + 2
			else:
				num = int((ord(letter)-65)/3) + 2
			nameNum += str(num)

		if nameNum == brandNum:
			fout.write(name + '\n')
			foundValidName = True

	if not foundValidName:
		fout.write('NONE\n')

	fout.close()

names, brandNum = readInput()
translateNames(names, brandNum)
"""
ID: your_id_here
LANG: PYTHON3
TASK: transform
"""

def readInput():
	fin = open('transform.in')
	data = fin.readlines()
	fin.close()
	
	# read in size of square from input
	size = int(data[0].strip())

	# read in original pattern from input
	originalPattern = []
	for i in range(1,size+1):
		row = []
		for j in range(0,size):
			row.append(data[i][j])
		originalPattern.append(row)

	# read in new pattern from input
	newPattern = []
	for i in range(size+1,len(data)):
		row = []
		for j in range(0,size):
			row.append(data[i][j])
		newPattern.append(row)

	return originalPattern, newPattern

def rotate90(pattern):
	newPattern = []
	size = len(pattern)

	# fill newPattern with appropriate dimensions
	for i in range(0,size):
		row = []
		for j in range(0,size):
			row.append('')
		newPattern.append(row)

	# create newPattern
	for i in range(0,size):
		for j in range(0,size):
			newPattern[j][size-i-1] = pattern[i][j]

	return newPattern

def reflect(pattern):
	newPattern = []
	size = len(pattern)

	# fill newPattern with appropriate dimensions
	for i in range(0,size):
		row = []
		for j in range(0,size):
			row.append('')
		newPattern.append(row)

	# create newPattern
	for i in range(0,size):
		for j in range(0,size):
			newPattern[i][size-j-1] = pattern[i][j]

	return newPattern

def main(originalPattern, newPattern):
	# check and write which transformation was applied
	fout = open('transform.out', 'w')

	rotate90pattern = rotate90(originalPattern)
	rotate180pattern = rotate90(rotate90(originalPattern))
	rotate270pattern = rotate90(rotate90(rotate90(originalPattern)))
	reflectPattern = reflect(originalPattern)

	if newPattern == rotate90pattern:
		fout.write("1\n")
	elif newPattern == rotate180pattern:
		fout.write("2\n")
	elif newPattern == rotate270pattern:
		fout.write("3\n")
	elif newPattern == reflectPattern:
		fout.write("4\n")
	elif newPattern == rotate90(reflectPattern):
		fout.write("5\n")
	elif newPattern == rotate90(rotate90(reflectPattern)):
		fout.write("5\n")
	elif newPattern == rotate90(rotate90(rotate90(reflectPattern))):
		fout.write("5\n")
	elif newPattern == originalPattern:
		fout.write("6\n")
	else:
		fout.write("7\n")
		
	fout.close()

originalPattern, newPattern = readInput()
main(originalPattern, newPattern)
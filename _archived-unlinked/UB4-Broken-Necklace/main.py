"""
ID: your_id_here
LANG: PYTHON3
TASK: beads
"""

def beads(beadsString):
	maxBeads = 0
	for i in range(0,len(beadsString)):
		numBeads = 0
		counter = i

		# check how long two adjacent segments can be
		for j in range(0,2):
			firstBead = beadsString[counter]
			while True:
				# continue incrementing as long as beads are white
				# update the bead color once you hit a non-white bead
				if firstBead == 'w':
					numBeads += 1
					firstBead = beadsString[counter]
					counter += 1
				elif firstBead == beadsString[counter] or beadsString[counter] == 'w':
					numBeads += 1
					counter += 1
				else:
					break

				# properly increment the counter
				if counter == len(beadsString):
					counter = 0

				# edge case: numBeads cannot be greater than the length of the necklace
				if numBeads == len(beadsString):
					return numBeads

		if numBeads > maxBeads:
			maxBeads = numBeads

	return maxBeads

# read input
fin = open('beads.in')
data = fin.readlines()
fin.close()

result = beads(data[1].strip())

# write output
fout = open('beads.out', 'w')
fout.write(str(result) + '\n')
fout.close()
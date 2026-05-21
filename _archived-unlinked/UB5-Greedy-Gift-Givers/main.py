"""
ID: your_id_here
LANG: PYTHON3
TASK: gift1
"""

def readInput():
	fin = open('gift1.in','r')
	data = fin.readlines()
	fin.close()
	return data

def calcBalance(data):
	# set everyone's balance in the bank dict to 0
	bank = {}
	numPeople = int(data[0])
	
	for i in range(1,numPeople+1):
		bank[data[i].strip()] = 0

	# iterate though the data and update balances accordingly
	lineCounter = numPeople+1

	while True:
		person = data[lineCounter].strip()
		money = int(data[lineCounter+1].split()[0])
		numGiftees = int(data[lineCounter+1].split()[1])
		if numGiftees == 0:
			amountPerGift = 0
			remainder = money
		else:
			amountPerGift = int(money/numGiftees)

		# remove the gifted money from the person's bank
		bank[person] -= numGiftees * amountPerGift

		# add the gifted money to the giftees
		for i in range(lineCounter+2, lineCounter+2+numGiftees):
			giftee = data[i].strip()
			bank[giftee] += amountPerGift

		# update lineCounter appropriately
		lineCounter += 2 + numGiftees

		if lineCounter == len(data):
			break

	return bank

def writeOutput(data, bank):
	numPeople = int(data[0])
	fout = open('gift1.out','w')
	
	for i in range(1,numPeople+1):
		person = data[i].strip()
		fout.write(person + ' ' + str(bank[person]) + '\n')

	fout.close()

data = readInput()
bank = calcBalance(data)
writeOutput(data, bank)

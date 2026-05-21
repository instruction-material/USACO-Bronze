"""
ID: your_id_here
LANG: PYTHON3
TASK: milk
"""

def readInput():
	f = open("milk.in")
	text = f.readlines()
	f.close()

	numUnits = int(text[0].split()[0])

	# create dictionary where keys are prices and values are lists of numUnits
	farmers = {}
	for i in range(1,len(text)):
		price = int(text[i].split()[0])
		units = int(text[i].split()[1])

		if price in farmers:
			farmers[price].append(units)
		else:
			farmers[price] = [units]

	return farmers, numUnits

def calcTotalPrice(farmers, numUnits):
	# loop through sorted dictionary until numUnits is reached
	totalUnits = 0
	totalPrice = 0

	for price in sorted(farmers.keys()):
		# calculate number of units offered at this price
		units = 0
		for i in farmers[price]:
			units += i
		
		# check if units remaining is less than units this farmer offers
		# if so, only buy as many units as needed, otherwise buy all
		remainingUnits = numUnits - totalUnits
		if remainingUnits < units:
			totalPrice += remainingUnits * price
			break
		else:
			totalUnits += units
			totalPrice += units*price

	return totalPrice

def writeOutput(totalPrice):
	f = open("milk.out","w+")
	f.write(str(totalPrice) + "\n")
	f.close()

farmers, numUnits = readInput()
totalPrice = calcTotalPrice(farmers, numUnits)
writeOutput(totalPrice)
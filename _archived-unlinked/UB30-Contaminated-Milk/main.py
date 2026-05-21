# http://www.usaco.org/index.php?page=viewproblem2&cpid=569

def readInput():
	f = open("badmilk.in")
	text = f.readlines()
	f.close()

	# create a dictionary where each key is a person number and
	# each value is the time they got sick

	sickPeople = {}
	numDrinks = int(text[0].split()[2])

	for i in range(numDrinks+1, len(text)):
		personNum = int(text[i].split()[0])
		timeSick = int(text[i].split()[1])
		sickPeople[personNum] = timeSick

	# create a dictionary where each key is a milk number and
	# each value is a list of tuples, where each tuple is: (person, time)

	drinks = {}

	for i in range(1, numDrinks+1):
		personNum = int(text[i].split()[0])
		milkNum = int(text[i].split()[1])
		time = int(text[i].split()[2])

		if milkNum in drinks:
			drinks[milkNum].append((personNum, time))
		else:
			drinks[milkNum] = [(personNum, time)]

	return sickPeople, drinks

def main(sickPeople, drinks):

	# for each milk number, check if all of the people who drank the milk
	# got sick after they drank it. also check if everyone who got sick
	# drank the milk. if both are true, add this milk to possibleBadMilks

	possibleBadMilks = []

	for milkNum in drinks:
		isBadMilk = True

		# check if all the people who drank the milk got sick after they drank it
		for data in drinks[milkNum]:
			personNum = data[0]
			timeConsumed = data[1]
			if personNum in sickPeople:
				sickTime = sickPeople[personNum]
				if sickTime <= timeConsumed:
					isBadMilk = False

		# check if everyone who got sick drank the milk
		peopleNums = []
		for data in drinks[milkNum]:
			peopleNums.append(data[0])
		for peopleNum in sickPeople:
			if peopleNum not in peopleNums:
				isBadMilk = False

		if isBadMilk:
		   possibleBadMilks.append(milkNum)

	# find the number of people who drank each badMilk and take the maximum of these numbers to find the maximum doses of medicine list
	maxDoses = 0
	for milkNum in possibleBadMilks:
		peopleDrankBadMilk = set()
		for data in drinks[milkNum]:
			peopleDrankBadMilk.add(data[0])
		maxDoses = max(maxDoses, len(peopleDrankBadMilk))

	return maxDoses

def writeOutput(maxDoes):
	f = open("badmilk.out","w")
	f.write(str(maxDoes) + "\n")
	f.close()

sickPeople, drinks = readInput()
maxDoses = main(sickPeople, drinks)
writeOutput(maxDoses)

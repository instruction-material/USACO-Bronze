"""
ID: your_id_here
LANG: PYTHON3
TASK: ride
"""

# read input
f = open("ride.in")
data = f.readlines()
f.close()

group = data[0].strip()
comet = data[1].strip()

# calculate products
groupProduct = 1
for letter in group:
  groupProduct *= ord(letter)-64

cometProduct = 1
for letter in comet:
  cometProduct *= ord(letter)-64

# write output
f = open('ride.out', 'w')

if groupProduct % 47 == cometProduct % 47:
  f.write('GO\n')
else:
  f.write('STAY\n')

f.close()

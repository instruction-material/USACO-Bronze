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
group_product = 1
for letter in group:
  group_product *= ord(letter)-64

comet_product = 1
for letter in comet:
  comet_product *= ord(letter)-64

# write output
f = open('ride.out', 'w')

if group_product % 47 == comet_product % 47:
  f.write('GO\n')
else:
  f.write('STAY\n')

f.close()

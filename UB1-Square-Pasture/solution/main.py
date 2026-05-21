f = open("square.in")
data = f.readlines()
f.close()
coords = []

for line in data:
  line = [int(x) for x in line.split()]
  coords.append(line)

minX = min(coords[0][0], coords[1][0])
maxX = max(coords[0][2], coords[1][2])
minY = min(coords[0][1], coords[1][1])
maxY = max(coords[0][3], coords[1][3])

side1 = maxX - minX
side2 = maxY - minY
area = max(side1, side2) ** 2

f = open("square.out","w")
f.write(str(area))
f.close()
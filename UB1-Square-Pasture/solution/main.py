f = open("square.in")
data = f.readlines()
f.close()
coords = []

for line in data:
    line = [int(x) for x in line.split()]
    coords.append(line)

min_x = min(coords[0][0], coords[1][0])
max_x = max(coords[0][2], coords[1][2])
min_y = min(coords[0][1], coords[1][1])
max_y = max(coords[0][3], coords[1][3])

side1 = max_x - min_x
side2 = max_y - min_y
area = max(side1, side2) ** 2

f = open("square.out", "w")
f.write(str(area))
f.close()

"""
ID: your_id_here
LANG: PYTHON3
TASK: skidesign
"""

def read_input():
    f = open("skidesign.in")
    data = f.readlines()
    f.close()

    heights = []
    for i in range(1,len(data)):
        heights.append(int(data[i]))
    heights = sorted(heights)

    return heights

def main(heights):
    # calculate the total cost for each possible interval, starting from
    # (minHeight, lowestHeight + 17) up to (minHeight - 17, maxHeight)

    min_cost = 1000 * 100**2 # make sure minCost is set reasonably
    min_height = heights[0]
    max_height = min_height + 17

    while min_height <= heights[-1]-17:
        cost = 0
        for height in heights:
            if height < min_height:
                cost += (height-min_height)**2
            elif height > max_height:
                cost += (height-max_height)**2
        if cost < min_cost:
            min_cost = cost
        min_height += 1
        max_height += 1

    return min_cost

def write_output(min_cost):
    f = open("skidesign.out", "w+")
    f.write(str(min_cost) + "\n")
    f.close()

heights = read_input()
min_cost = main(heights)
write_output(min_cost)

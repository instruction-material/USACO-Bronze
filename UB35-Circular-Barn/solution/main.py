###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# http://www.usaco.org/index.php?page=viewproblem2&cpid=616


def read_input():
    fin = open("cbarn.in")
    data = fin.readlines()
    fin.close()

    doors = []
    for i in range(1, len(data)):
        doors.append(int(data[i]))
    return doors


# calculates the amount of distance the cows travel if openDoorNum is opened
def calc_distance(open_door_num, doors):
    distance = 0
    for i in range(0, len(doors)):
        final_door = i
        num_cows = doors[i]

        # cows travel clockwise, so special case if the cow needs to go around
        if final_door >= open_door_num:
            distance += (final_door - open_door_num) * num_cows
        else:
            distance += (len(doors) - open_door_num + final_door) * num_cows
    return distance


def calc_min_distance(doors):
    min_distance = (
        100 * len(doors) * 1000
    )  # max num rooms * max num cows * max perimeter
    for i in range(0, len(doors)):
        distance = calc_distance(i, doors)
        min_distance = min(min_distance, distance)
    return min_distance


def write_output(min_distance):
    fout = open("cbarn.out", "w")
    fout.write(str(min_distance) + "\n")
    fout.close()


doors = read_input()
min_distance = calc_min_distance(doors)
write_output(min_distance)

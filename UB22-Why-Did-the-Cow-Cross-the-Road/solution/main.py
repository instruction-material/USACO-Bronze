# http://usaco.org/index.php?page=viewproblem2&cpid=711


def read_input():
    f = open("crossroad.in")
    text = f.readlines()
    f.close()

    input_data = []
    for i in range(1, len(text)):
        line = text[i].split()
        line = [int(x) for x in line]
        input_data.append(line)
    return input_data


def main(input_data):
    # create two dictionaries where the keys are the cow IDs
    # lastPosition: tracks the last position (0 or 1) of each cow
    # numCrossings: tracks the number of crossings of each cow

    last_position = {}
    num_crossings = {}

    for line in input_data:
        cow_id = line[0]
        if cow_id not in last_position:
            last_position[cow_id] = ""
            num_crossings[cow_id] = 0

    # run through the input and update lastPosition and numCrossings
    for line in input_data:
        cow_id = line[0]
        position = line[1]

        # handle case if this is the first position for this cow
        if last_position[cow_id] == "":
            last_position[cow_id] = position
        elif position != last_position[cow_id]:
            last_position[cow_id] = position
            num_crossings[cow_id] += 1

    # sum total number of crossings
    total_crossings = 0
    for key in num_crossings:
        total_crossings += num_crossings[key]

    return total_crossings


def write_output(total_crossings):
    f = open("crossroad.out", "w")
    f.write(str(total_crossings) + "\n")
    f.close()


input_data = read_input()
total_crossings = main(input_data)
write_output(total_crossings)

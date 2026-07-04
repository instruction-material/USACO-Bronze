###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# http://www.usaco.org/index.php?page=viewproblem2&cpid=568


def read_input():
    f = open("speeding.in")
    text = f.readlines()
    f.close()

    n = int(text[0].split()[0])
    speed_limits = generate_speed_dict(text[1 : n + 1])
    bessie_speeds = generate_speed_dict(text[n + 1 :])

    return speed_limits, bessie_speeds


# create a dictionary where each key is a road segment index
# and each value is the speed or speed limit at that segment
def generate_speed_dict(data):
    speed_dict = {}
    road_segment = 1

    for i in range(len(data)):
        segment_length = int(data[i].split()[0])
        speed_limit = int(data[i].split()[1])

        for j in range(segment_length):
            speed_dict[road_segment] = speed_limit
            road_segment += 1

    return speed_dict


def main(speed_limits, bessie_speeds):
    # iterate through the dictionaries and calculate the max amount
    # by which Bessie exceeded the speed limit

    max_exceeds = 0
    for key in bessie_speeds:
        speed_diff = bessie_speeds[key] - speed_limits[key]
        max_exceeds = max(max_exceeds, speed_diff)

    return max_exceeds


def write_output(max_exceeds):
    f = open("speeding.out", "w")
    f.write(str(max_exceeds) + "\n")
    f.close()


speed_limits, bessie_speeds = read_input()
max_exceeds = main(speed_limits, bessie_speeds)
write_output(max_exceeds)

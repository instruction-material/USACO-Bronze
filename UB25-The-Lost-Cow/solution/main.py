###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# http://www.usaco.org/index.php?page=viewproblem2&cpid=735


def read_input():
    f = open("lostcow.in")
    text = f.readlines()
    f.close()

    starting_pos = int(text[0].split()[0])
    bessie_pos = int(text[0].split()[1])

    return starting_pos, bessie_pos


def main(starting_pos, bessie_pos):
    # continue the zig-zag search strategy until Farmer John reaches or passes Bessie
    distance_from_x = 1
    dist_traveled = 0
    curr_pos = starting_pos
    while True:
        new_pos = starting_pos + distance_from_x
        dist_traveled += abs(new_pos - curr_pos)
        curr_pos = new_pos
        distance_from_x *= -2

        # make sure we update distTraveled properly if Farmer John overshot Bessie
        if curr_pos == bessie_pos:
            break
        elif curr_pos < bessie_pos and starting_pos > bessie_pos:
            dist_traveled -= abs(curr_pos - bessie_pos)
            break
        elif curr_pos > bessie_pos and starting_pos < bessie_pos:
            dist_traveled -= abs(curr_pos - bessie_pos)
            break
    return dist_traveled


def write_output(dist_traveled):
    f = open("lostcow.out", "w")
    f.write(str(dist_traveled) + "\n")
    f.close()


starting_pos, bessie_pos = read_input()
dist_traveled = main(starting_pos, bessie_pos)
write_output(dist_traveled)

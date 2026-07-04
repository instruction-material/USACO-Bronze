"""
ID: your_id_here
LANG: PYTHON3
TASK: wormhole
"""


def read_input():
    f = open("wormhole.in")
    data = f.readlines()
    f.close()

    # read in x and y coordinates
    x = []
    y = []

    for i in range(1, len(data)):
        wormhole = data[i].split()
        x.append(int(wormhole[0]))
        y.append(int(wormhole[1]))

    return x, y


# create list where each element is the partner of wormhole i
# if unpaired, the partner is -1
def generate_partners(x, y):
    partners = []
    for i in range(len(x)):
        partners.append(-1)
    return partners


# create list where each element is the next wormhole to the right of i
def generate_next_on_right(x, y):
    next_on_right = []
    for i in range(0, len(partners)):
        next_on_right.append(-1)
    for i in range(0, len(partners)):
        # loop through each wormhole
        for j in range(0, len(partners)):
            # update nextOnRight if wormhole is the closest to the right
            if x[j] > x[i] and y[i] == y[j]:
                if next_on_right[i] == -1:
                    next_on_right[i] = j
                elif x[j] - x[i] < x[next_on_right[i]] - x[i]:
                    next_on_right[i] = j

    return next_on_right


# checks whether a given pairing of wormholes results in a cycle
def cycle_exists(partners, next_on_right):
    # try starting at each wormhole and looking for a cycle
    for i in range(0, len(partners)):
        pos = i

        # at most, try taking N steps (where each step is a teleport + moving to the right)
        for j in range(0, len(partners)):
            # teleport to the partner wormhole
            pos = partners[pos]
            # jump to the next wormhole on the right
            pos = next_on_right[pos]
            # stop if there's no wormhole to the right
            if pos == -1:
                break

        # if you're still at a wormhole, then there is a cycle
        if pos != -1:
            return True

    return False


# recursively generate all pairings of wormholes and check if each pairing results in a cycle
def main(partners, next_on_right):
    total_solutions = 0

    # find the first unpaired wormhole
    unpaired_wormhole_index = 0
    found_unpaired_wormhole = False
    for i in range(0, len(partners)):
        if partners[i] == -1:
            unpaired_wormhole_index = i
            found_unpaired_wormhole = True
            break

    # if all wormholes are already paired, check if this pairing is valid
    if not found_unpaired_wormhole:
        if cycle_exists(partners, next_on_right):
            return 1
        else:
            return 0

    # try pairing this wormhole with all other possible wormholes
    for j in range(i + 1, len(partners)):
        if partners[j] == -1:
            partners[i] = j
            partners[j] = i
            total_solutions += main(partners, next_on_right)
            partners[i] = -1
            partners[j] = -1

    return total_solutions


def write_output(total_solutions):
    f = open("wormhole.out", "w")
    f.write(str(total_solutions) + "\n")
    f.close()


x, y = read_input()
partners = generate_partners(x, y)
next_on_right = generate_next_on_right(x, y)
total_solutions = main(partners, next_on_right)
write_output(total_solutions)

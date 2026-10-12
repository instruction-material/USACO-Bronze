# ADDED: Distinct Wormholes learner; complete only the named tasks.
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
    # CHANGED: learner task generate_next_on_right; retain the supplied driver.
    raise NotImplementedError("TASK: generate_next_on_right")  # CHANGED


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
    # CHANGED: learner task main; retain the supplied driver.
    raise NotImplementedError("TASK: main")  # CHANGED


def write_output(total_solutions):
    f = open("wormhole.out", "w")
    f.write(str(total_solutions) + "\n")
    f.close()


x, y = read_input()
partners = generate_partners(x, y)
next_on_right = generate_next_on_right(x, y)
total_solutions = main(partners, next_on_right)
write_output(total_solutions)

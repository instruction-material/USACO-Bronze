# ADDED: Distinct The Lost Cow learner; complete only the named tasks.
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
    # CHANGED: learner task main; retain the supplied driver.
    raise NotImplementedError("TASK: main")  # CHANGED


def write_output(dist_traveled):
    f = open("lostcow.out", "w")
    f.write(str(dist_traveled) + "\n")
    f.close()


starting_pos, bessie_pos = read_input()
dist_traveled = main(starting_pos, bessie_pos)
write_output(dist_traveled)

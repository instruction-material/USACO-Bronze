# ADDED: Distinct Diamond Collector learner; complete only the named tasks.
# http://usaco.org/index.php?page=viewproblem2&cpid=639


def read_input():
    fin = open("diamond.in")
    data = fin.readlines()
    fin.close()

    k = int(data[0].split()[1])
    sizes = []
    for i in range(1, len(data)):
        sizes.append(int(data[i]))
    return sizes, k


# given the smallest diamond in a display case, find the number of diamonds
# that can be displayed alongside it
def calc_num_diamonds(min_size, sizes, k):
    # CHANGED: learner task calc_num_diamonds; retain the supplied driver.
    raise NotImplementedError("TASK: calc_num_diamonds")  # CHANGED


def calc_max_diamonds(sizes, k):
    # test each diamond for how many can be displayed alongside it
    # CHANGED: learner task calc_max_diamonds; retain the supplied driver.
    raise NotImplementedError("TASK: calc_max_diamonds")  # CHANGED


def write_output(max_diamonds):
    fout = open("diamond.out", "w")
    fout.write(str(max_diamonds) + "\n")
    fout.close()


sizes, k = read_input()
max_diamonds = calc_max_diamonds(sizes, k)
write_output(max_diamonds)

# ADDED: Distinct Family Tree learner; complete only the named tasks.
def read_input():
    fin = open("family.in")
    data = fin.readlines()
    fin.close()
    cow1 = data[0].split()[1]
    cow2 = data[0].split()[2]
    parents = {}
    for i in data[1:]:
        parents[i.split()[1]] = i.split()[0]
    return cow1, cow2, parents


def main(cow1, cow2, parents):
    # CHANGED: learner task main; retain the supplied driver.
    raise NotImplementedError("TASK: main")  # CHANGED


def write_output(ans):
    fout = open("family.out", "w")
    fout.write(str(ans) + "\n")
    fout.close()


cow1, cow2, parents = read_input()
ans = main(cow1, cow2, parents)
write_output(ans)

# http://usaco.org/index.php?page=viewproblem2&cpid=639

def read_input():
    fin = open("diamond.in")
    data = fin.readlines()
    fin.close()

    k = int(data[0].split()[1])
    sizes = []
    for i in range(1,len(data)):
        sizes.append(int(data[i]))
    return sizes, k

# given the smallest diamond in a display case, find the number of diamonds
# that can be displayed alongside it
def calc_num_diamonds(min_size, sizes, k):
    num_diamonds = 0
    for diamond in sizes:
        if diamond >= min_size and diamond <= min_size + k:
            num_diamonds += 1
    return num_diamonds

def calc_max_diamonds(sizes, k):
    # test each diamond for how many can be displayed alongside it
    max_diamonds = 0
    for diamond in sizes:
        num_diamonds = calc_num_diamonds(diamond, sizes, k)
        max_diamonds = max(max_diamonds, num_diamonds)
    return max_diamonds

def write_output(max_diamonds):
    fout = open("diamond.out", "w")
    fout.write(str(max_diamonds) + "\n")
    fout.close()

sizes, k = read_input()
max_diamonds = calc_max_diamonds(sizes, k)
write_output(max_diamonds)

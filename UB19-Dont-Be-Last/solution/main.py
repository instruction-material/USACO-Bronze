# http://www.usaco.org/index.php?page=viewproblem2&cpid=687


def read_input():
    f = open("notlast.in")
    text = f.readlines()
    f.close()

    # create dictionary of milk amounts of each cow
    # note that cows need to be predefined in case a cow is not in the input

    cows = {
        "Bessie": 0,
        "Elsie": 0,
        "Daisy": 0,
        "Gertie": 0,
        "Annabelle": 0,
        "Maggie": 0,
        "Henrietta": 0,
    }

    for i in range(1, len(text)):
        cow = text[i].split()[0]
        milk = text[i].split()[1]
        cows[cow] += int(milk)

    return cows


# returns the second lowest amount of milk (-1 if all cows tie for the lowest amount)
def find_second_lowest(cows):
    milk_amts = []
    for cow in cows:
        milk_amts.append(cows[cow])

    milk_amts = sorted(milk_amts)
    lowest = milk_amts[0]
    second_lowest = -1
    for i in milk_amts:
        if i > lowest:
            second_lowest = i
            break

    return second_lowest


# find cow(s) associated with the second lowest amount of milk
def main(cows, second_lowest):
    num_cows_found = 0
    cow_name = ""
    if second_lowest != -1:
        for cow in cows:
            if cows[cow] == second_lowest:
                num_cows_found += 1
                cow_name = cow

    return cow_name, num_cows_found


def write_output(cow_name, second_lowest, num_cows_found):
    f = open("notlast.out", "w")
    if second_lowest == -1:
        f.write("Tie\n")
    elif num_cows_found > 1:
        f.write("Tie\n")
    else:
        f.write(cow_name + "\n")
    f.close()


cows = read_input()
second_lowest = find_second_lowest(cows)
cow_name, num_cows_found = main(cows, second_lowest)
write_output(cow_name, second_lowest, num_cows_found)

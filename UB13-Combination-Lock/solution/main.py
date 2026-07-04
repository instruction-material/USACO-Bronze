"""
ID: roobeel1
LANG: PYTHON3
TASK: combo
"""

def read_input():
    f = open("combo.in")
    text = f.readlines()
    f.close()

    # read in maxNum and the two codes
    max_num = int(text[0])
    farmer_combo = text[1].split()
    master_combo = text[2].split()
    for i in range(3):
        farmer_combo[i] = int(farmer_combo[i])
        master_combo[i] = int(master_combo[i])

    return max_num, farmer_combo, master_combo

# function that takes in a number and generates a list of the 2 numbers above and below
def generate_num_possibilities(num, max_num):
    nums = []

    # handle special case where maxNum <= 5
    if max_num <= 5:
        for i in range(1,max_num+1):
            nums.append(i)
        return nums

    for i in range(-2,3):
        code_num = num + i
        if code_num < 1:
            code_num = max_num + code_num
        elif code_num > max_num:
            code_num = code_num - max_num
        nums.append(code_num)
    return nums

# function that generates a set of the possible combos, given a code
def generate_combos(code, max_num):
    combos = set()
    num_possibilities = []

    for i in range(3):
        num_possibilities.append(generate_num_possibilities(code[i], max_num))

    for i in num_possibilities[0]:
        for j in num_possibilities[1]:
            for k in num_possibilities[2]:
                combo = str(i) + '-' + str(j) + '-' + str(k)
                combos.add(combo)

    return combos

def main(max_num, farmer_combo, master_combo):
    # generate the possible combos for both codes
    farmer_combos = generate_combos(farmer_combo, max_num)
    master_combos = generate_combos(master_combo, max_num)

    # find the size of the union of the possible combos
    num_possible_combos = len(farmer_combos.union(master_combos))

    return num_possible_combos

def write_output(num_possible_combos):
    f = open("combo.out", "w")
    f.write(str(num_possible_combos) + "\n")
    f.close()

max_num, farmer_combo, master_combo = read_input()
num_possible_combos = main(max_num, farmer_combo, master_combo)
write_output(num_possible_combos)

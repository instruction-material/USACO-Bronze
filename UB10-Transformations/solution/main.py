###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

"""
ID: your_id_here
LANG: PYTHON3
TASK: transform
"""


def read_input():
    fin = open("transform.in")
    data = fin.readlines()
    fin.close()

    # read in size of square from input
    size = int(data[0].strip())

    # read in original pattern from input
    original_pattern = []
    for i in range(1, size + 1):
        row = []
        for j in range(0, size):
            row.append(data[i][j])
        original_pattern.append(row)

    # read in new pattern from input
    new_pattern = []
    for i in range(size + 1, len(data)):
        row = []
        for j in range(0, size):
            row.append(data[i][j])
        new_pattern.append(row)

    return original_pattern, new_pattern


def rotate90(pattern):
    new_pattern = []
    size = len(pattern)

    # fill newPattern with appropriate dimensions
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append("")
        new_pattern.append(row)

    # create newPattern
    for i in range(0, size):
        for j in range(0, size):
            new_pattern[j][size - i - 1] = pattern[i][j]

    return new_pattern


def reflect(pattern):
    new_pattern = []
    size = len(pattern)

    # fill newPattern with appropriate dimensions
    for i in range(0, size):
        row = []
        for j in range(0, size):
            row.append("")
        new_pattern.append(row)

    # create newPattern
    for i in range(0, size):
        for j in range(0, size):
            new_pattern[i][size - j - 1] = pattern[i][j]

    return new_pattern


def main(original_pattern, new_pattern):
    # check and write which transformation was applied
    fout = open("transform.out", "w")

    rotate90pattern = rotate90(original_pattern)
    rotate180pattern = rotate90(rotate90(original_pattern))
    rotate270pattern = rotate90(rotate90(rotate90(original_pattern)))
    reflect_pattern = reflect(original_pattern)

    if new_pattern == rotate90pattern:
        fout.write("1\n")
    elif new_pattern == rotate180pattern:
        fout.write("2\n")
    elif new_pattern == rotate270pattern:
        fout.write("3\n")
    elif new_pattern == reflect_pattern:
        fout.write("4\n")
    elif new_pattern == rotate90(reflect_pattern):
        fout.write("5\n")
    elif new_pattern == rotate90(rotate90(reflect_pattern)):
        fout.write("5\n")
    elif new_pattern == rotate90(rotate90(rotate90(reflect_pattern))):
        fout.write("5\n")
    elif new_pattern == original_pattern:
        fout.write("6\n")
    else:
        fout.write("7\n")

    fout.close()


original_pattern, new_pattern = read_input()
main(original_pattern, new_pattern)

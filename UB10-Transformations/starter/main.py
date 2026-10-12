# ADDED: Distinct Transformations learner; complete only the named tasks.
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
    # CHANGED: learner task rotate90; retain the supplied driver.
    raise NotImplementedError("TASK: rotate90")  # CHANGED


def reflect(pattern):
    # CHANGED: learner task reflect; retain the supplied driver.
    raise NotImplementedError("TASK: reflect")  # CHANGED


def main(original_pattern, new_pattern):
    # check and write which transformation was applied
    rotate90pattern = rotate90(original_pattern)
    rotate180pattern = rotate90(rotate90(original_pattern))
    rotate270pattern = rotate90(rotate90(rotate90(original_pattern)))
    reflect_pattern = reflect(original_pattern)

    fout = open("transform.out", "w")  # CHANGED: open only after tasks return.

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

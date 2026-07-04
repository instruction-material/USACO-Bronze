"""
ID: your_id_here
LANG: PYTHON3
TASK: crypt1
"""


def read_input():
    f = open("crypt1.in")
    data = f.readlines()
    f.close()

    nums = data[1].strip().split()
    return nums


# generate all possible options for the two numbers that will be multipled together
def generate_options(nums):
    num_one_options = []
    num_two_options = []

    for i in nums:
        for j in nums:
            for k in nums:
                num_one_options.append(i + j + k)

    for i in nums:
        for j in nums:
            num_two_options.append(i + j)

    return num_one_options, num_two_options


def main(num_one_options, num_two_options):
    # generate the three numbers involved in the multiplication
    # check combination for its validity
    counter = 0
    for i in num_one_options:
        for j in num_two_options:
            num1 = i
            num2 = j

            row1 = int(num1) * int(num2[1])
            row2 = int(num1) * int(num2[0])
            product = int(num1) * int(num2)

            is_valid = True

            # make sure that each number is the correct number of digits
            if row1 > 999 or row2 > 999 or product > 9999:
                is_valid = False

            row1 = str(row1)
            row2 = str(row2)
            product = str(product)

            # check that each number only contains valid digits
            for k in row1:
                if k not in nums:
                    is_valid = False

            for k in row2:
                if k not in nums:
                    is_valid = False

            for k in product:
                if k not in nums:
                    is_valid = False

            if is_valid:
                counter += 1

    return counter


def write_output(answer):
    f = open("crypt1.out", "w+")
    f.write(str(answer) + "\n")
    f.close()


nums = read_input()
num_one_options, num_two_options = generate_options(nums)
answer = main(num_one_options, num_two_options)
write_output(answer)

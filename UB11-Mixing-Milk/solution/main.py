"""
ID: your_id_here
LANG: PYTHON3
TASK: milk
"""


def read_input():
    f = open("milk.in")
    text = f.readlines()
    f.close()

    num_units = int(text[0].split()[0])

    # create dictionary where keys are prices and values are lists of numUnits
    farmers = {}
    for i in range(1, len(text)):
        price = int(text[i].split()[0])
        units = int(text[i].split()[1])

        if price in farmers:
            farmers[price].append(units)
        else:
            farmers[price] = [units]

    return farmers, num_units


def calc_total_price(farmers, num_units):
    # loop through sorted dictionary until numUnits is reached
    total_units = 0
    total_price = 0

    for price in sorted(farmers.keys()):
        # calculate number of units offered at this price
        units = 0
        for i in farmers[price]:
            units += i

        # check if units remaining is less than units this farmer offers
        # if so, only buy as many units as needed, otherwise buy all
        remaining_units = num_units - total_units
        if remaining_units < units:
            total_price += remaining_units * price
            break
        else:
            total_units += units
            total_price += units * price

    return total_price


def write_output(total_price):
    f = open("milk.out", "w+")
    f.write(str(total_price) + "\n")
    f.close()


farmers, num_units = read_input()
total_price = calc_total_price(farmers, num_units)
write_output(total_price)

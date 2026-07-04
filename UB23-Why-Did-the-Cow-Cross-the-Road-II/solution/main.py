###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# http://usaco.org/index.php?page=viewproblem2&cpid=712

import string


def read_input():
    f = open("circlecross.in")
    text = f.readlines()
    f.close()

    circle = text[0].strip()
    return circle


def main(circle):
    # count the number of times a single letter appears between two letters
    # for each letter, only consider the letters that come after it to avoid
    # double-counting

    num_crossings = 0

    letters = string.ascii_uppercase
    for letter in letters:
        current_pos = circle.find(letter)
        unique_letters = []  # holds unique letters
        while True:
            current_pos += 1
            # handle case where circle wraps around
            if current_pos >= len(circle):
                current_pos = 0
            # break when we find the same letter again
            if circle[current_pos] == letter:
                break

            current_letter = circle[current_pos]
            if ord(current_letter) > ord(letter):
                # remove currentLetter from uniqueLetters if it appears twice
                if current_letter not in unique_letters:
                    unique_letters.append(current_letter)
                else:
                    unique_letters.remove(current_letter)

        num_crossings += len(unique_letters)
    return num_crossings


def write_output(num_crossings):
    f = open("circlecross.out", "w")
    f.write(str(num_crossings) + "\n")
    f.close()


circle = read_input()
num_crossings = main(circle)
write_output(num_crossings)

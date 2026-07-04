# http://www.usaco.org/index.php?page=viewproblem2&cpid=664

from string import ascii_lowercase


def read_input():
    f = open("blocks.in")
    text = f.readlines()
    f.close()

    # save word pairings in list of lists
    words = []
    for i in range(1, len(text)):
        words.append(text[i].split())
    return words


# generates dictionary where key is letter and value is number of times
# the letter appears in the word
def count_letters_in_word(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def main(words):
    # for each letter, save the number of times it appears most frequently
    # on either side of the block
    master_dict = {}
    for word_pair in words:
        word_one_dict = count_letters_in_word(word_pair[0])
        word_two_dict = count_letters_in_word(word_pair[1])

        # iterate through all letters contained in at least one of the two words
        for letter in set(word_one_dict.keys()).union(word_two_dict.keys()):

            # if the letter is in both words, add the larger count to masterDict
            if letter in word_one_dict and letter in word_two_dict:
                max_count = word_one_dict[letter]
                if word_two_dict[letter] > max_count:
                    max_count = word_two_dict[letter]

                if letter in master_dict:
                    master_dict[letter] += max_count
                else:
                    master_dict[letter] = max_count

            # else, just add the count from one of the words to masterDict
            else:
                max_count = 0
                if letter in word_one_dict:
                    max_count = word_one_dict[letter]
                else:
                    max_count = word_two_dict[letter]

                if letter in master_dict:
                    master_dict[letter] += max_count
                else:
                    master_dict[letter] = max_count

    return master_dict


def write_output(master_dict):
    f = open("blocks.out", "w")
    for letter in ascii_lowercase:
        if letter in master_dict:
            f.write(str(master_dict[letter]) + "\n")
        else:
            f.write(str(0) + "\n")
    f.close()


words = read_input()
master_dict = main(words)
write_output(master_dict)

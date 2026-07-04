# http://www.usaco.org/index.php?page=viewproblem2&cpid=736

def read_input():
    f = open("cownomics.in")
    text = f.readlines()
    f.close()

    num_cows = int(text[0].split()[0])
    num_positions = int(text[0].split()[1])
    spotty_cows = []
    plain_cows = []

    for i in range(1,num_cows+1):
        spotty_cows.append(text[i].strip())

    for i in range(num_cows+1,len(text)):
        plain_cows.append(text[i].strip())

    return spotty_cows, plain_cows, num_positions

def main(spotty_cows, plain_cows, num_positions):
    # for each position, store the plain cow genes in a set.
    # check if all the spotty cows have a different letter.
    # if they do, increase numPossibleGenes by 1.

    num_possible_genes = 0
    for i in range(0,num_positions):
        plain_cow_genes = set()
        for plain_cow in plain_cows:
            plain_cow_genes.add(plain_cow[i])

        spotty_cows_have_other_letters = True
        for spotty_cow in spotty_cows:
            if spotty_cow[i] in plain_cow_genes:
                spotty_cows_have_other_letters = False

        if spotty_cows_have_other_letters:
            num_possible_genes += 1

    return num_possible_genes

def write_output(num_possible_genes):
    f = open("cownomics.out","w")
    f.write(str(num_possible_genes) + "\n")
    f.close()

spotty_cows, plain_cows, num_positions = read_input()
num_possible_genes = main(spotty_cows, plain_cows, num_positions)
write_output(num_possible_genes)

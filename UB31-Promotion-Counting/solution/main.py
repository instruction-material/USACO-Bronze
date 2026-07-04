# http://www.usaco.org/index.php?page=viewproblem2&cpid=591

def read_input():
    fin = open("promote.in")
    data = fin.readlines()
    fin.close()

    participants = []
    for line in data:
        num_before = int(line.split()[0])
        num_after = int(line.split()[1])
        participants.append([num_before, num_after])
    return participants

def calc_promotions(participants):
    # promoted from G to P = num P after - num P before
    num_gto_p = participants[3][1] - participants[3][0]

    # promoted from S to G = num in G or P after - num in G or P before
    num_sto_g = (participants[2][1] + participants[3][1]) - (participants[2][0] + participants[3][0])

    # promoted from B to S = num in S or G or P after - num in S or G or P before
    num_bto_s = (participants[1][1] + participants[2][1] + participants[3][1]) - (participants[1][0] + participants[2][0] + participants[3][0])

    return num_gto_p, num_sto_g, num_bto_s

def write_output(num_gto_p, num_sto_g, num_bto_s):
    fout = open("promote.out", "w")
    fout.write(str(num_bto_s) + "\n")
    fout.write(str(num_sto_g) + "\n")
    fout.write(str(num_gto_p) + "\n")
    fout.close()

participants = read_input()
num_gto_p, num_sto_g, num_bto_s = calc_promotions(participants)
write_output(num_gto_p, num_sto_g, num_bto_s)

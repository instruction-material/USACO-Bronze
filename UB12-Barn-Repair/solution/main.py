"""
ID: your_id_here
LANG: PYTHON3
TASK: barn1
"""

def read_input():
    f = open("barn1.in")
    text = f.readlines()
    f.close()

    num_boards = int(text[0].split()[0])

    # create list of sorted stall numbers that are occupied
    occupied_stalls = []
    for i in range(1,len(text)):
        occupied_stalls.append(int(text[i]))

    return sorted(occupied_stalls), num_boards

# creates list of lengths of gaps between the occupied stalls
def calc_gap_lengths(occupied_stalls):
    gap_lengths = []
    gap_length = 0
    prev_stall_num = occupied_stalls[0]

    for i in range(1,len(occupied_stalls)):
        gap_lengths.append(occupied_stalls[i]-prev_stall_num-1)
        prev_stall_num = occupied_stalls[i]

    return gap_lengths

def calc_num_stalls_blocked(occupied_stalls, gap_lengths, num_boards):
    # the farmer can leave the N largest gaps uncovered, where N = numBoards - 1
    # thus, calculate the total length of the N largest gaps
    total_gap_length = 0
    gap_lengths = sorted(gap_lengths, reverse=True)
    for i in range(0,num_boards-1):
        # if there are more boards than gaps, break
        if i >= len(gap_lengths):
            break
        total_gap_length += gap_lengths[i]

    # the number of stalls blocked is then:
    max_stall_num = occupied_stalls[-1]
    min_stall_num = occupied_stalls[0]
    num_blocked = max_stall_num-min_stall_num+1-total_gap_length

    return num_blocked

def write_output(num_blocked):
    f = open("barn1.out", "w")
    f.write(str(num_blocked) + "\n")
    f.close()

occupied_stalls,num_boards = read_input()
gap_lengths = calc_gap_lengths(occupied_stalls)
num_blocked = calc_num_stalls_blocked(occupied_stalls, gap_lengths, num_boards)
write_output(num_blocked)

def read_input():
    fin = open("milkorder.in")
    data = fin.readlines()
    fin.close()
    N = int(data[0].split()[0])
    social = [int(x) for x in data[1].split()]
    req_cows = [[int(y) for y in x.split()] for x in data[2:]]
    return N, social, req_cows


# check if constraints work
def check(N, social, req_cows):
    ans = [0] * (N + 1)
    req = [0] * (N + 1)
    for i in req_cows:
        ans[i[1]] = i[0]
        req[i[0]] = i[1]

    cur_pos = 1
    placed = True
    for cow in social:
        if req[cow] != 0:
            if req[cow] < cur_pos:
                return False
            else:
                cur_pos = req[cow] + 1
            continue

        placed = False

        # greedily find next position to place cow
        while cur_pos <= N:
            if ans[cur_pos] == 0:
                placed = True
                ans[cur_pos] = cow
                break
            cur_pos += 1

    return placed


def main(N, social, req_cows):
    taken = [0] * (N + 1)
    one_exists = -1
    for i in req_cows:
        taken[i[1]] = i[0]
        if i[0] == 1:
            one_exists = i[1]

    if one_exists != -1:
        return one_exists

    ans = -1
    # Try all possible positions for cow 1
    for i in range(1, N + 1):
        if taken[i] != 0:
            continue
        req_cows.append([1, i])
        if check(N, social, req_cows):
            ans = i
            break
        req_cows.pop()
    return ans


def write_output(ans):
    fout = open("milkorder.out", "w")
    fout.write(str(ans) + "\n")
    fout.close()


N, social, req_cows = read_input()
ans = main(N, social, req_cows)
write_output(ans)

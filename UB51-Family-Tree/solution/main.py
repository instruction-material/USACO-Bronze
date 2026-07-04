
def read_input():
    fin = open("family.in")
    data = fin.readlines()
    fin.close()
    cow1 = data[0].split()[1]
    cow2 = data[0].split()[2]
    parents = {}
    for i in data[1:]:
        parents[i.split()[1]] = i.split()[0]
    return cow1, cow2, parents

def main(cow1, cow2, parents):
    count1 = 0
    count2 = -1
    done = False
    cur_cow1 = cow1;

    # loop over all ancestors of cow1
    while not done:
        cur_cow2 = cow2;
        count2 = 0

        # loop over all ancestors of cow2
        while not done:
            if cur_cow1 == cur_cow2:
                done = True
                break

            if cur_cow2 in parents:
                cur_cow2 = parents[cur_cow2]
                count2 += 1
            else:
                break

        if done:
            break
        if cur_cow1 in parents:
            cur_cow1 = parents[cur_cow1]
            count1 += 1
        else:
            break

    ans = ""
    if not done:
        ans = "NOT RELATED"
    elif count1 == 1 and count2 == 1:
        ans = "SIBLINGS"
    elif count1 > 1 and count2 > 1:
        ans = "COUSINS"
    else:
        if count1 > count2:
            # Swap cow1, cow2
            temp = cow1;
            cow1 = cow2;
            cow2 = temp;

            temp2 = count1;
            count1 = count2;
            count2 = temp2;

        ans = cow1 + " is the " + "great-"*(count2-2)

        if count1 == 0 and count2 > 1:
            ans += "grand-"
        if count1 == 0:
            ans += "mother"
        else:
            ans += "aunt"
        ans += " of " + cow2
    return ans

def write_output(ans):
    fout = open("family.out", "w")
    fout.write(str(ans) + "\n")
    fout.close()

cow1, cow2, parents = read_input()
ans = main(cow1, cow2, parents)
write_output(ans)
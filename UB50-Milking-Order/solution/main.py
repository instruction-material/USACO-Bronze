
def readInput():
    fin = open("milkorder.in")
    data = fin.readlines()
    fin.close()
    N = int(data[0].split()[0])
    social = [int(x) for x in data[1].split()]
    reqCows = [[int(y) for y in x.split()] for x in data[2:]]
    return N, social, reqCows

# check if constraints work 
def check(N, social, reqCows):
    ans = [0] * (N + 1)
    req = [0] * (N + 1)
    for i in reqCows:
        ans[i[1]] = i[0]
        req[i[0]] = i[1]
    
    curPos = 1;
    placed = True;
    for cow in social:
      if req[cow] != 0:
        if req[cow] < curPos:
            return False;
        else:
            curPos = req[cow] + 1;
        continue;
      
      placed = False

      # greedily find next position to place cow 
      while curPos <= N:
          if ans[curPos] == 0:
              placed = True
              ans[curPos] = cow
              break
          curPos += 1
 
    return placed

def main(N, social, reqCows):
    taken = [0] * (N + 1)
    oneExists = -1
    for i in reqCows:
        taken[i[1]] = i[0]
        if i[0] == 1:
            oneExists = i[1]
    
    if oneExists != -1:
        return oneExists
    
    ans = -1
    # Try all possible positions for cow 1
    for i in range(1, N + 1):
        if taken[i] != 0:
            continue
        reqCows.append([1, i])
        if check(N, social, reqCows):
            ans = i
            break
        reqCows.pop();
    return ans 

def writeOutput(ans):
    fout = open("milkorder.out", "w")
    fout.write(str(ans) + "\n")
    fout.close()

N, social, reqCows = readInput()
ans = main(N, social, reqCows)
writeOutput(ans)
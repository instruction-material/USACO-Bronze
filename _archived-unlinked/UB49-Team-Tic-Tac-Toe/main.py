
def readInput():
    fin = open("tttt.in")
    data = fin.readlines()
    fin.close()
    board = [list(s)[:3] for s in data]
    return board

# returns whether a single set of three chars can be claimed a win by poss1 and poss2
def check(cows, poss1, poss2):
    exist1 = False
    exist2 = poss2 == '-'
    for i in cows:
        if i != poss1 and i != poss2:
            return False;
        exist1 = exist1 or (i == poss1)
        exist2 = exist2 or (i == poss2)
    return exist1 and exist2

# returns whether team formed by poss1 and poss2 can win
def checkWin(board, poss1, poss2):
    canWin = False
    for i in range(3):
        canWin = canWin or check(board[i], poss1, poss2)
        canWin = canWin or check([board[0][i], board[1][i], board[2][i]], poss1, poss2)
    canWin = canWin or check([board[0][0], board[1][1], board[2][2]], poss1, poss2)
    canWin = canWin or check([board[0][2], board[1][1], board[2][0]], poss1, poss2)
    return 1 if canWin else 0 

def main(board):
    print(board)
    ans1 = 0
    ans2 = 0
    # Loop through all teams
    for i in range(26):
      ans1 += checkWin(board, chr(ord('A')+i), '-')
      for j in range(i+1, 26):
          ans2 += checkWin(board, chr(ord('A')+i), chr(ord('A')+j))
    return ans1, ans2

def writeOutput(ans1, ans2):
    fout = open("tttt.out", "w")
    fout.write(str(ans1) + "\n")
    fout.write(str(ans2) + "\n")
    fout.close()

board = readInput()
ans1, ans2 = main(board)
writeOutput(ans1, ans2)
# adapted from USACO solution: http://www.usaco.org/current/data/sol_prob2_bronze_feb22.html

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

need_to_move = [0]*N

# get the position of a given cow in the b list
def pos_in_B(x):
  for i in range(N):
    if B[i] == x:
      return i

# Loop through pairs of cows in their initial positions. 
for i in range(N):
  for j in range(i+1,N):
    # If the position of the first cow in the desired order (B) is greater than 
    # the position of the second cow, the second cow needs to be moved. 
    if pos_in_B(A[i]) > pos_in_B(A[j]):
      need_to_move[j] = 1

print(sum(need_to_move))
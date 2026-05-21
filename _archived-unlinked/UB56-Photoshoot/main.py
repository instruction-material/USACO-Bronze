# adapted from Benjamin Qi's USACO solution: http://www.usaco.org/current/data/sol_prob1_bronze_open22.html

N = int(input())
order = input()

last = '.'
min_reversals = 0

# check if the cows at consecutive even positions are different
for i in range(0,N,2):
  if order[i] != order[i+1]:
    if order[i] != last:
      min_reversals += 1
      # keep track of last cow breed encountered
      last = order[i]

# if the last cow breed at an even position is 'H', there is no need to reverse the last pair
if last == 'H':
  min_reversals -= 1

print(min_reversals)
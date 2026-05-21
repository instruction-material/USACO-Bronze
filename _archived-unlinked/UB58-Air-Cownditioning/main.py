# adapted from USACO solution: http://www.usaco.org/current/data/sol_prob2_bronze_dec21.html

# number of stalls
N = int(input())
# preferred temp
P = list(map(int,input().split()))
# current temp
T = list(map(int,input().split()))

# find the difference between the preferred temperature and the current temperature for each cow
difs = [x-y for x,y in zip(P,T)]
# calculate the sum of the absolute differences for each pair and divide by two
print(sum(abs(x-y) for x,y in zip(difs+[0],[0]+difs))//2)
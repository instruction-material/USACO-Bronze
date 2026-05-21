# adapted from USACO solution: http://www.usaco.org/current/data/sol_prob2_bronze_dec20.html

# read the number of flowers
n = int(input())

# create array for number of petals for each flower
petals = list(map(int, input().split()))

# count the number of photos that have an average flower
photos = 0

# loop through all possible photos and check if each photo has an average flower
for i in range(n):
    for j in range(i, n):
        total_petals = sum(petals[i:j+1])
        present = False
        for k in range(i, j+1):
            if petals[k] * (j - i + 1) == total_petals:
                present = True
                break
        if present:
            photos += 1

# output the result
print(photos)

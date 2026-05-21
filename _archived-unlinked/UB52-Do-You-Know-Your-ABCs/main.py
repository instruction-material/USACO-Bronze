# adapted from USACO solution: http://www.usaco.org/current/data/sol_prob1_bronze_dec20.html

# Read seven space-separated integers
numbers = list(map(int, input().split()))

# Sort the array in ascending order
numbers.sort()

# Calculate A, B, and C based on the properties given in the problem.
# A will be the smallest, B will be the second smallest, A + B + C will be the largest
A = numbers[0]
B = numbers[1]
C = numbers[6] - A - B

# Output the result
print(A, B, C)
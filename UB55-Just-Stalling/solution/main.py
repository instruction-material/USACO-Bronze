# adapted from USACO solution

# Get input values
n = int(input())
cows = list(map(int, input().split()))
stalls = list(map(int, input().split()))

# Sort the stalls in non-decreasing order
stalls.sort()

# Initialize the answer
answer = 1

# Iterate through each stall
for j in range(n):
  # Count how many cows can fit in the current stall
  cows_fit_current_stall = sum(1 for cow in cows if cow <= stalls[j])

  # Adjust for previously occupied stalls
  cows_fit_current_stall -= j

  # Multiply the answer by the number of ways to arrange cows for the current stall
  answer *= cows_fit_current_stall

# Print the final result
print(answer)

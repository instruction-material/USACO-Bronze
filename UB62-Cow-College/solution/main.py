# adapted from USACO
MAX_TUITION = 1000000
n = int(input())
tuition_to_cow = [0] * (MAX_TUITION + 1)
for x in input().split():
    tuition_to_cow[int(x)] += 1
max_money = 0
best_tuition = 0
current_cows = 0
for tuition in range(MAX_TUITION, 0, -1):
    current_cows += tuition_to_cow[tuition]
    if tuition * current_cows >= max_money:
        max_money = tuition * current_cows
        best_tuition = tuition
print(max_money, best_tuition)

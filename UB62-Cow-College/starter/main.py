# ADDED: Cow College learner pack; complete only choose_tuition.
MAX_TUITION = 1000000  # ADDED


def choose_tuition(tuition_to_cow):  # ADDED
    # TODO: scan prices downward while counting cows willing to pay each price.
    # TODO: compare revenue and keep the smallest price when revenue ties.
    # Return (maximum_revenue, smallest_optimal_tuition).
    raise NotImplementedError("Complete the tuition scan")  # ADDED


n = int(input())  # ADDED
tuition_to_cow = [0] * (MAX_TUITION + 1)  # ADDED
for x in input().split():  # ADDED
    tuition_to_cow[int(x)] += 1  # ADDED
max_money, best_tuition = choose_tuition(tuition_to_cow)  # ADDED
print(max_money, best_tuition)  # ADDED

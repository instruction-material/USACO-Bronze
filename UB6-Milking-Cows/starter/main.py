# ADDED: Distinct Milking Cows learner; complete only the named tasks.
"""
ID: your_id_here
LANG: PYTHON3
TASK: milk2
"""


# Returns a list of lists of start and end milking times
def read_input():
    with open("milk2.in") as fin:
        data = fin.readlines()
    times = []
    for i in range(1, len(data)):
        times.append([int(data[i].split()[0]), int(data[i].split()[1])])
    return times


# Returns an array of times when milking was active
def create_array(times):
    # Find earliest and latest time
    earliest_time = min(time[0] for time in times)
    latest_time = max(time[1] for time in times)

    # Create an array to track milking times
    milk_times = [False] * (latest_time - earliest_time)

    # CHANGED: record boundaries once instead of filling each interval.
    changes = [0] * (len(milk_times) + 1)  # ADDED
    for start, end in times:  # CHANGED
        changes[start - earliest_time] += 1  # ADDED
        changes[end - earliest_time] -= 1  # ADDED
    active = 0  # ADDED
    for i in range(len(milk_times)):  # CHANGED
        active += changes[i]  # ADDED
        milk_times[i] = active > 0  # CHANGED

    return milk_times, earliest_time, latest_time


# Returns longest consecutive milking and non-milking times
def calc_times(milk_times):
    # CHANGED: learner task calc_times; retain the supplied driver.
    raise NotImplementedError("TASK: calc_times")  # CHANGED


# Write output
def write_output(longest_milk_time, longest_no_milk_time):
    fout = open("milk2.out", "w")
    fout.write(str(longest_milk_time) + " " + str(longest_no_milk_time) + "\n")
    fout.close()


times = read_input()
milk_times, earliest_time, latest_time = create_array(times)
longest_milk_time, longest_no_milk_time = calc_times(milk_times)
write_output(longest_milk_time, longest_no_milk_time)

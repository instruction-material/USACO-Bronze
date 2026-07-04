# http://usaco.org/index.php?page=viewproblem2&cpid=713


def read_input():
    f = open("cowqueue.in")
    input_data = f.readlines()
    f.close()

    return input_data


def main(input_data):
    # create dictionary where the keys are arrival time and values are
    # total questioning times

    times = {}
    for i in range(1, len(input_data)):
        line = input_data[i].split()
        arrival_time = int(input_data[i].split()[0])
        questioning_time = int(input_data[i].split()[1])
        if arrival_time in times:
            times[arrival_time] += questioning_time
        else:
            times[arrival_time] = questioning_time

    latest_time = 0
    for arrival_time in sorted(times):
        questioning_times = times[arrival_time]

        # if the cows cannot get questionined immediately, add questioningTimes
        # to latestTime, otherwise just update latestTime to the time it would take
        # to question these cows

        if arrival_time < latest_time:
            latest_time += questioning_times
        else:
            latest_time = arrival_time + questioning_times

    return latest_time


def write_output(latest_time):
    f = open("cowqueue.out", "w")
    f.write(str(latest_time) + "\n")
    f.close()


input_data = read_input()
latest_time = main(input_data)
write_output(latest_time)

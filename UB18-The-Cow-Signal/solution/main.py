# http://www.usaco.org/index.php?page=viewproblem2&cpid=665


def read_input():
    f = open("cowsignal.in")
    text = f.readlines()
    f.close()

    factor = int(text[0].split()[2])

    signal = []
    for i in range(1, len(text)):
        signal.append(text[i].strip())

    return signal, factor


def main(signal, factor):
    # for each line, append that character n times
    # then append that line n times to newSignal
    new_signal = []
    for line in signal:
        new_line = ""
        for letter in line:
            for i in range(factor):
                new_line += letter
        for i in range(factor):
            new_signal.append(new_line)

    return new_signal


def write_output(new_signal):
    f = open("cowsignal.out", "w")
    for line in new_signal:
        f.write(line + "\n")
    f.close()


signal, factor = read_input()
new_signal = main(signal, factor)
write_output(new_signal)

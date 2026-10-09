# ADDED: Feeding the Cows learner pack; complete only place_patches.
def place_patches(cows, k):  # ADDED
    # TODO: create a patch list and separate G/H coverage boundaries.
    # TODO: scan left to right, placing a patch only for an uncovered cow.
    # TODO: handle the final positions without overwriting another breed.
    # Return the list of '.', 'G', and 'H' patch characters.
    raise NotImplementedError("Complete the patch placement")  # ADDED


t = int(input())  # ADDED
for _ in range(t):  # ADDED
    n, k = (int(x) for x in input().split())  # ADDED
    cows = input()  # ADDED
    patches = place_patches(cows, k)  # ADDED
    print(n - patches.count("."))  # ADDED
    print("".join(patches))  # ADDED

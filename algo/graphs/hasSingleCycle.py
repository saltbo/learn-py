def hasSingleCycle(array):
    totalJumps = 0
    currentIdx = 0
    while totalJumps < len(array):
        # If the current index is 0 and we have already jumped, then we are not in a single cycle
        # Because we have already visited the index 0
        if totalJumps > 0 and currentIdx == 0:
            return False

        totalJumps += 1
        currentIdx = (currentIdx+array[currentIdx]) % len(array)

    # If we have jumped the same number of times as the length of the array, then we are in a single cycle
    return currentIdx == 0


def hasSingleCycle2(array):
    jumps = 0
    currentIdx = 0
    while True:
        currentIdx += array[currentIdx]
        currentIdx %= len(array)
        jumps += 1
        if currentIdx == 0 or array[currentIdx] == 0 or jumps > len(array):
            break

    return jumps == len(array)


# array = [-26, 1, 2, 3, 4]
array = [2, 3, 1, -4, -4, 2]
print(hasSingleCycle(array))
print(hasSingleCycle2(array))
print(-26 % 5)

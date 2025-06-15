def longestStreakOfAdjacentOnes(array):
    currentMax = 0
    currentIdx = 0
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = 1
            max = getMaxStrike(array)
            array[i] = 0
            if max > currentMax:
                currentMax = max
                currentIdx = i
    return currentIdx


def getMaxStrike(array):
    maxStrike = 0
    currentStrike = 0
    for num in array:
        if num == 1:
            currentStrike += 1
        else:
            currentStrike = 0

        if currentStrike > maxStrike:
            maxStrike = currentStrike
    return maxStrike


def longestStreakOfAdjacentOnes2(array):
    """
    Using a single pass to find the longest streak of adjacent ones
    by keeping track of the last zero index and the current streak.
    """
    currentStreak = 0
    replaceZeroIdx = -1

    longestStreak = 0
    longestStreakIdx = -1
    for i in range(len(array)):
        if array[i] == 1:
            currentStreak += 1
        else:
            currentStreak = i - replaceZeroIdx
            replaceZeroIdx = i

        if currentStreak > longestStreak:
            longestStreak = currentStreak
            longestStreakIdx = replaceZeroIdx

        print(array[i], i, currentStreak)
    return longestStreakIdx


def longestStreakOfAdjacentOnes3(array):
    """
    Using a sliding window approach to find the longest streak of adjacent ones
    """
    zero_count = 0
    zero_idx = -1
    left = 0

    longest_streak = 0
    longest_zero_idx = 0
    for right in range(len(array)):
        if array[right] == 0:
            zero_count += 1
            zero_idx = right

        # If we have more than one zero, we need to move the left pointer
        # until we have at most one zero in the window
        while zero_count > 1:
            if array[left] == 0:
                zero_count -= 1
            left += 1

        # Calculate the current length of the window
        # and update the longest streak if necessary
        current_length = right - left + 1
        print(current_length)
        if current_length > longest_streak:
            longest_streak = current_length
            longest_zero_idx = zero_idx
    return longest_zero_idx


array = [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
print(longestStreakOfAdjacentOnes3(array))

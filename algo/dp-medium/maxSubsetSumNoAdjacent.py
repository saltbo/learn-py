# def maxSubsetSumNoAdjacent(array):
#     if len(array) == 0:
#         return 0
#     elif len(array) == 1:
#         return array[0]

#     dp = [9] * len(array)
#     dp[0] = array[0]
#     dp[1] = max(array[0], array[1])
#     for idx in range(2, len(array)):
#         dp[idx] = max(dp[idx-1], dp[idx-2]+array[idx])

#     return dp[-1]

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    prev2 = array[0]
    prev1 = max(array[0], array[1])
    for idx in range(2, len(array)):
        current = max(prev1, prev2+array[idx])
        prev2 = prev1
        prev1 = current

    return prev1


array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))

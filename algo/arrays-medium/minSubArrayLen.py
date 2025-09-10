from typing import List


def minSubArrayLen(target: int, nums: List[int]):
    left = 0
    curr = 0
    minimum = float('inf')
    for i in range(len(nums)):
        curr += nums[i]
        while curr >= target:
            minimum = min(minimum, i-left+1)
            curr -= nums[left]
            left += 1

    return minimum if minimum != float('inf') else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))

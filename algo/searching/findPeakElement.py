

from typing import List


def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums))  # Output: 5
nums = [1, 2, 3, 1]
print(findPeakElement(nums))  # Output: 2

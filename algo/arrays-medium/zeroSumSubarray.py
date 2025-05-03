def zeroSumSubarray(nums):
    s = set([0])
    currentSum = 0
    for idx in range(len(nums)):
        currentSum += nums[idx]
        if currentSum in s:
            return True
        s.add(currentSum)

    return False


nums = [-5, -5, 2, 3, -2]
print(zeroSumSubarray(nums))

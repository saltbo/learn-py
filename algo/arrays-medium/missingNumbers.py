def missingNumbers(nums):
    nums.sort()

    missingNums = []
    for idx in range(1, len(nums)+3):
        if idx not in nums:
            missingNums.append(idx)
    return missingNums


def missingNumbers2(nums):
    totalSum = sum(range(1, len(nums)+3))
    numsSum = sum(nums)
    missingNumsSum = totalSum - numsSum
    avg = missingNumsSum // 2

    leftHalfSum = 0
    rightHalfSum = 0
    for num in nums:
        if num <= avg:
            leftHalfSum += num
        else:
            rightHalfSum += num

    exceptedLeftSum = sum(range(1, avg+1))
    exceptedRightSum = sum(range(avg+1, len(nums)+3))
    return [exceptedLeftSum-leftHalfSum, exceptedRightSum-rightHalfSum]


nums = [1, 4, 3]
print(missingNumbers2(nums))

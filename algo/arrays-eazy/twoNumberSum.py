def twoNumberSum(array, targetSum):
    left = 0
    right = len(array)-1
    array.sort()
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left+=1
        elif currentSum > targetSum:
            right-=1
    return []



print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
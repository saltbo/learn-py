
def threeNumberSum(array, targetSum):
    array.sort()
    results = []
    for idx, first in enumerate(array):
        lIdx = idx + 1
        rIdx = len(array) - 1
        while lIdx < rIdx:
           second = array[lIdx]
           third = array[rIdx]
           cSum = first + second + third
           if cSum == targetSum:
               results.append([first, second, third])
               lIdx += 1
               rIdx -= 1
           elif cSum > targetSum:
               rIdx -= 1
           elif cSum < targetSum: 
               lIdx +=1
            
    return results

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 4], 0))
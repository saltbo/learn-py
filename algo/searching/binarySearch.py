from time import sleep


def binarySearch(array, target, overall_idx=0):
    length = len(array)
    mid = length//2
    current = array[mid]
    if array[mid] == target:
        return mid+overall_idx
    elif length > 1 and current > target:
        return binarySearch(array[:mid], target, overall_idx)
    elif length > 1 and current < target:
        return binarySearch(array[mid:], target, overall_idx+mid)
    return -1


def binarySearch2(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left+right)//2
        value = array[mid]
        if value > target:
            right = mid-1
        elif value < target:
            left = mid+1
        else:
            return mid

    return -1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
# array = [1, 5, 23, 111]
# target = 111
print(binarySearch2(array, target))

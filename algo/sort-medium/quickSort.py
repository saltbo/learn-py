def quickSort2(array):
    """
    Quick Sort Algorithm
    Time Complexity: O(n log n)
    Space Complexity: O(log n)
    """
    # It selects a pivot element and partitions the array into two sub-arrays, one with elements less than the pivot and one with elements greater than the pivot.
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [item for item in array if item < pivot]
    middle = [item for item in array if item == pivot]
    right = [item for item in array if item > pivot]

    return quickSort2(left) + middle + quickSort2(right)


def quickSort(array):
    """
    Quick Sort Algorithm(in-place)
    Time Complexity: O(n log n)
    Space Complexity: O(log n)
    """
    return quickSortHelper(array, 0, len(array) - 1)


def quickSortHelper(array, left, right):
    if left >= right:
        return array

    # Partition the array
    pivotIndex = partition(array, left, right)
    print(pivotIndex)

    # Recursively sort the left and right sub-arrays
    quickSortHelper(array, left, pivotIndex - 1)
    quickSortHelper(array, pivotIndex + 1, right)
    return array


def partition(array, left, right):
    pivotIdx = left
    pivot = array[pivotIdx]

    left += 1
    while left <= right:
        if array[left] > pivot and array[right] < pivot:
            array[left], array[right] = array[right], array[left]
        if array[left] <= pivot:
            left += 1
        if array[right] >= pivot:
            right -= 1

    array[pivotIdx], array[right] = array[right], array[pivotIdx]
    return right


array = [8, 5, 2, 9, 5, 6, 3]
sortedArray = quickSort(array)
print(sortedArray)
# Output: [2, 3, 5, 5, 6, 8, 9]

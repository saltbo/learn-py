def insertionSort(array):
    """
    Insertion Sort Algorithm
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # It iterates through the array, taking one element at a time and inserting it into its correct position in the sorted portion of the array.

    for idx in range(1, len(array)):
        while idx > 0 and array[idx] < array[idx - 1]:
            array[idx], array[idx-1] = array[idx-1], array[idx]
            idx -= 1
    return array


array = [8, 5, 2, 9, 5, 6, 3]
sortedArray = insertionSort(array)
print(sortedArray)

def longestPeak(array):
    tipIdxes = []
    for idx in range(1, len(array)-1):
        if array[idx] > array[idx-1] and array[idx] > array[idx+1]:
            tipIdxes.append(idx)

    peaks = []
    for tipIdx in tipIdxes:
        leftIdx = rightIdx = tipIdx
        while (leftIdx > 0 and array[leftIdx] > array[leftIdx-1]):
            leftIdx -= 1
        while (rightIdx < len(array)-1 and array[rightIdx] > array[rightIdx+1]):
            rightIdx += 1
        peaks.append(array[leftIdx:rightIdx+1])

    longestLength = 0
    for peak in peaks:
        if len(peak) > longestLength:
            longestLength = len(peak)
    return longestLength


def longestPeak2(array):
    tipIdxes = []
    for idx in range(1, len(array)-1):
        if array[idx] > array[idx-1] and array[idx] > array[idx+1]:
            tipIdxes.append(idx)

    longestPeakLength = 0
    for tipIdx in tipIdxes:
        leftIdx = rightIdx = tipIdx
        while (leftIdx > 0 and array[leftIdx] > array[leftIdx-1]):
            leftIdx -= 1
        while (rightIdx < len(array)-1 and array[rightIdx] > array[rightIdx+1]):
            rightIdx += 1

        currentPeakLength = rightIdx-leftIdx+1
        if currentPeakLength > longestPeakLength:
            longestPeakLength = currentPeakLength

    return longestPeakLength


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak2(array))

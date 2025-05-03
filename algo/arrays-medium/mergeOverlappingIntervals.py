def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        if currentInterval[1] >= nextInterval[0]:
            currentInterval[1] = max(nextInterval[1], currentInterval[1])
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)

    return mergedIntervals


intervals = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]

print(mergeOverlappingIntervals(intervals))

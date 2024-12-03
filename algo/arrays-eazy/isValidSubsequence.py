def isValidSubsequence(array, sequence):
    if len(sequence) > len(array):
        return False

    sequenceIndex = 0
    for value in array:
        if sequenceIndex == len(sequence):
            break
        if sequence[sequenceIndex] == value:
            sequenceIndex += 1
    return sequenceIndex == len(sequence)
    
    
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))
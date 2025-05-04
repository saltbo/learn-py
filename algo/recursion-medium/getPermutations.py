def getPermutations(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]

    permutations = []
    for idx in range(len(array)):
        current = array[idx]
        remaining = array[idx+1:]+array[:idx]
        for permutation in getPermutations(remaining):
            permutations.append([current]+permutation)

    return permutations


array = [1, 2, 3]
print(getPermutations(array))

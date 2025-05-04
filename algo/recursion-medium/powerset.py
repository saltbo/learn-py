# def powerset(array):
#     results = [[]]
#     for ele in array:
#         for idx in range(len(results)):
#             results.append(results[idx] + [ele])
#     return results


def powerset(array):
    # Base case: empty array has only empty set as powerset
    if len(array) == 0:
        return [[]]

    # Take the first element
    first_element = array[0]
    # Recursively find powerset of rest of array
    rest_powerset = powerset(array[1:])

    # For each subset in rest_powerset, create a new subset that includes first_element
    result = []
    for subset in rest_powerset:
        # Add the subset without the first element
        result.append(subset)
        # Add the subset with the first element
        result.append(subset + [first_element])

    return result


array = [1, 2, 3]
print(powerset(array))

# [[], [1], [2], [1,2]]
# [[], [1], [2], [1,2],[3],[1,3],[2,3],[1,2,3]]

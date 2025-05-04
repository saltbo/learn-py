def majorityElement(array):
    current = 0
    count = 0
    for num in array:
        if count == 0:
            current = num

        if num != current:
            count -= 1
        else:
            count += 1

    return current


# array = [1, 2, 3, 2, 2, 1, 2]
# array = [1, 1, 1, 1, 2, 2, 2, 2, 2]
array = [2, 2, 1]
print(majorityElement(array))

def productSum(array, depth=1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, depth+1)
        else:
            sum += element
    return sum * depth


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))

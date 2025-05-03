def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    for idx in range(len(array)):
        products[idx] = caculateOtherItem(array, idx)
    return products


def caculateOtherItem(array, excludeIdx):
    result = 1
    for idx, item in enumerate(array):
        if idx == excludeIdx:
            continue
        result *= item
    return result


array = [5, 1, 4, 2]
print(arrayOfProducts(array))

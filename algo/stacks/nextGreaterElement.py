def nextGreaterElement(array):
    result = [-1]*len(array)

    stack = []
    for idx in range(len(array)*2):
        circleIdx = idx % len(array)
        print(circleIdx)

        current = array[circleIdx]
        while len(stack) > 0 and current > array[stack[len(stack)-1]]:
            lastIdx = stack.pop()
            result[lastIdx] = current

        stack.append(circleIdx)

    return result


array = [2, 5, -3, -4, 6, 7, 2]
print(nextGreaterElement(array))

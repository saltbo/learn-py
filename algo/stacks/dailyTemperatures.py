from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        curr = temperatures[i]
        while stack and curr > temperatures[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev

        stack.append(i)

    return result


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# note：每一次迭代时将不符合条件（栈内的顺序）的弹出，只有符合条件的才入栈
# 栈内的顺序是从高到低。为什么不会出现71 69 72这样的顺序，因为在72入栈之前就把69 71这两个弹出了
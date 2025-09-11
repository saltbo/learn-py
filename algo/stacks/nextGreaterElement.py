def nextGreaterElement(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    # 遍历两次数组确保转完一圈
    for i in range(2*n):
        curr = nums[i % n]  # 使用模运算实现圈循环
        while stack and curr > nums[stack[-1]]:
            prev = stack.pop()
            result[prev] = curr

        # 只在第一轮时将索引加入栈
        if i < n:
            stack.append(i)

    return result


array = [2, 5, -3, -4, 6, 7, 2]
print(nextGreaterElement(array))

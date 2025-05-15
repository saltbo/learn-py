def bestDigits(number, numDigits):
    stack = []
    for digit in number:
        while numDigits > 0 and len(stack) > 0 and digit > stack[-1]:
            stack.pop()
            numDigits -= 1

        stack.append(digit)

    # case 321 or 22
    while numDigits > 0:
        stack.pop()
        numDigits -= 1

    return "".join(stack)


number = "462839"
numDigits = 2
print(bestDigits(number, numDigits))

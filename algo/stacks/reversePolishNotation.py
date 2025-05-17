def reversePolishNotation(tokens):
    stack = []

    for token in tokens:
        match token:
            case "+":
                stack.append(stack.pop()+stack.pop())
            case "-":
                firstToken = stack.pop()
                stack.append(stack.pop()-firstToken)
            case "*":
                stack.append(stack.pop()*stack.pop())
            case "/":
                firstToken = stack.pop()
                stack.append(int(stack.pop()/firstToken))
            case _:
                stack.append(int(token))

    return stack.pop()


tokens = ["10", "5", "+", "10", "*", "50", "-", "10", "/"]
print(reversePolishNotation(tokens))

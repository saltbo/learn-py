def balancedBrackets(string):
    stack = []
    openingBrackets = ["(", "[", "{"]
    closingBrackets = [")", "]", "}"]
    mactchingBrackets = {")": "(", "]": "[", "}": "{"}
    for char in string:
        if char in openingBrackets:
            stack.append(char)
            continue
        if char in closingBrackets:
            if stack and stack[-1] == mactchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


string = "([])(){}(())()()"
print(balancedBrackets(string))

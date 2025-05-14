# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self) -> None:
        self.stack = []

    def peekObject(self):
        return self.stack[len(self.stack)-1]

    def peek(self):
        return self.peekObject()["num"]

    def pop(self):
        return self.stack.pop()["num"]

    def push(self, number):
        minNum = min(number, self.getMin())
        maxNum = max(number, self.getMax())
        self.stack.append({"min": minNum, "max": maxNum, "num": number})

    def getMin(self):
        if len(self.stack) == 0:
            return float("Inf")

        return self.peekObject()["min"]

    def getMax(self):
        if len(self.stack) == 0:
            return float("-Inf")

        return self.peekObject()["max"]

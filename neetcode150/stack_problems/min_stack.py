# My first idea was to implement it as a list, where
# all of the even numbered indices contain the minimum
# up until that point in the stack. 

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else []

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else []
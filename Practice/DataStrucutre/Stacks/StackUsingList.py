class StackUsingList:

    def __init__(self) -> None:
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

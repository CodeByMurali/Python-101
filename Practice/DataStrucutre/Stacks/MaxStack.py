class MaxStack:

    def __init__(self) -> None:
        self.main_stack = []
        self.max_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        max_val = max(val, self.max_stack[-1] if self.max_stack else val)
        self.max_stack.append(max_val)

    def pop(self) -> None:
        if self.main_stack:
            self.main_stack.pop()
        if self.max_stack:
            self.max_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]

    def getMax(self) -> int:
        if self.max_stack:
            return self.max_stack[-1]


max_stack = MaxStack()
max_stack.push(5)
max_stack.push(1)
max_stack.push(3)
max_stack.push(5)

print(max_stack.top())  # Output: 5 (Top element)
print(max_stack.get_max())  # Output: 5 (Current maximum)
max_stack.pop()

print(max_stack.top())  # Output: 3 (New top element)
print(max_stack.get_max())  # Output: 5 (Maximum remains unchanged)

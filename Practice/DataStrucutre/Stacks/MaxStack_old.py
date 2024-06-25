class MaxStack:

    # MaxStack stack = new MaxStack();
    # stack.push(5);
    # stack.push(1);
    # stack.push(5);
    # stack.top(); -> 5
    # stack.popMax(); -> 5
    # stack.top(); -> 1
    # stack.peekMax(); -> 5
    # stack.pop(); -> 1
    # stack.top(); -> 5

    def __init__(self) -> None:
        self.stack = []
        self.max_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Always add the first elment to the max stack or
        # If the last element in the max stack element is greater than current element
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped_val = self.stack.pop()
            if popped_val == self.max_stack[-1]:
                self.max_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None  # Indicate error or empty stack

    def get_max(self) -> int:
        if self.max_stack:
            return self.max_stack[-1]
        else:
            return None  # Indicate error or empty stack


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

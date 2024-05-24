class MinStack:

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

    def __init__(self):
        self.stack = []  # Regular stack to store all elements
        self.min_stack = []  # Stack to store minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Update min_stack only if val is less than or equal to the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop from both stacks (if not empty)
        if self.stack:
            popped_val = self.stack.pop()
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None  # Indicate error or empty stack

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return None  # Indicate error or empty stack


min_stack = MinStack()
min_stack.push(3)  # Push value 3 onto the stack
min_stack.push(1)  # Push value 1 onto the stack
min_stack.push(5)  # Push value 5 onto the stack
min_stack.push(3)  # Push value 3 onto the stack
min_stack.push(1)  # Push value 1 onto the stack
min_stack.push(5)  # Push value 5 onto the stack
min_stack.push(3)  # Push value 3 onto the stack
min_stack.push(1)  # Push value 1 onto the stack
min_stack.push(5)  # Push value 5 onto the stack
min_stack.push(3)  # Push value 3 onto the stack
min_stack.push(1)  # Push value 1 onto the stack
min_stack.push(5)  # Push value 5 onto the stack
min_stack.pop()  # Remove the top element (5)
# Get the new top element (currently 1)
top_element_after_pop = min_stack.top()
print(top_element_after_pop)  # Output: 1
# Get the new top element (currently 1)
top_element_after_pop = min_stack.top()
print(top_element_after_pop)  # Output: 1

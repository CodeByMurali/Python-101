"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
[-2, 0, -3]
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # def push(self, val: int):
    #     self.stack.append(val)
    #     if not self.min_stack or val <= self.min_stack[-1]:
    #         self.min_stack.append(val)

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    # def pop(self):
    #     if self.stack:
    #         if self.stack[-1] == self.min_stack[-1]:
    #             self.min_stack.pop()
    #         self.stack.pop()

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]


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

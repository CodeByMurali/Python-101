from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        size = len(self.queue)
        self.queue.append(x)

        # Roatating the queue to simulate stack behaviour
        for _ in range(size):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        if self.queue:
            return self.queue.popleft()

    def top(self) -> int:
        if self.queue:
            # Since push would already rotate the elements its easy to return the first element
            return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())   # Output: 2
print(obj.pop())   # Output: 2
print(obj.empty())  # Output: False

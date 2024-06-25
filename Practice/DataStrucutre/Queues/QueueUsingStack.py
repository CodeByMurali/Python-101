class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.stack1[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.stack1) == 0

    def size(self):
        return len(self.stack1)

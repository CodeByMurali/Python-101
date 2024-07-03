from queue import Queue


def reverse_queue(q: Queue) -> Queue:
    stack = []

    # Dequeue all elements from the queue and push them onto the stack
    while not q.empty():
        stack.append(q.get())

    # Pop all elements from the stack and enqueue them back to the queue
    while stack:
        q.put(stack.pop())

    return q


if __name__ == "__main__":
    q: Queue = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)

    reversed_queue = reverse_queue(q)

    # Print reversed queue elements
    while not reversed_queue.empty():
        print(reversed_queue.get())

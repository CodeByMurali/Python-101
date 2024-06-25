from collections import deque

"""
Implement a Queue using List:

1. Create a queue class using list with methods enqueue, dequeue, front, is_empty, and size.
"""


def queue_using_list(input):
    dequeud_list = deque(input)
    # enqueue
    dequeud_list.append(10)
    dequeud_list.append(2)
    dequeud_list.append(3)

    # dequeue
    removed_element = dequeud_list.popleft()
    print(f"removed_element: {removed_element}")

    front = dequeud_list[0]
    print(f"front: {front}")

    # Check if queue is empty
    is_empty = len(dequeud_list) <= 0
    print(f"is_empty: {is_empty}")

    # Size
    size = len(dequeud_list)
    print(f"size: {size}")


queue_using_list([1, 2, 3])

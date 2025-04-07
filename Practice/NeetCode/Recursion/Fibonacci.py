from collections import deque
from typing import List, Deque
from typing import List
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


def fibonacci(n):
    logger.info(f"Entering fibonacci({n})")
    # Base case: F(0) = 0
    if n == 0:
        logger.info(f"Returning 0 for fibonacci({n})")
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        logger.info(f"Returning 1 for fibonacci({n})")
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        logger.info(f"Returning {result} for fibonacci({n})")
        return result


# Example usage
n = 5
logger.info(f"Fibonacci number F({n}) is: {fibonacci(n)}")


def remove_element(arr: List[int], element: int) -> List[int]:
    result = arr.copy()
    result.remove(element)
    return result


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)


def create_list_of_odds(n: int) -> List[int]:
    result = [i for i in range(n+1) if i % 2 == 1]
    return result


def create_list_of_odds(n: int) -> List[int]:
    return [i for i in range(1, n + 1, 2)]


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))


def reverse_list(arr: List[int]) -> List[int]:
    result = []
    for i in range(len(arr)):
        result.append(arr.pop())
    return result


def reverse_list(arr: List[int]) -> List[int]:
    arr_reverse = []

    while len(arr) > 0:
        arr_reverse.append(arr.pop())

    return arr_reverse


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque(arr)
    for i in range(k):
        element = queue.popleft()
        queue.append(element)
    return queue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    result = deque(arr)
    for i in range(k):
        result.appendleft(result.pop())
    return result


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))

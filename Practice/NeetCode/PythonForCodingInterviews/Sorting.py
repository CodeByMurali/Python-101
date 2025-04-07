from typing import List, Dict
from typing import List, Tuple
from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort()
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers


def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort()
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry",
      "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))


def sort_words(words: List[str]) -> List[str]:
    words.sort(reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    return numbers


def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort(reverse=True)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry",
      "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_word_length, reverse=True)
    return words


def get_word_length(word: str) -> int:
    return len(word)


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_abs_value)
    return numbers


def get_abs_value(num: int) -> int:
    return abs(num)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry",
      "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=lambda word: len(word), reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=lambda integer: abs(integer))
    return (numbers)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry",
      "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))


def sort_words(words: List[str]) -> List[str]:
    sorted_words = sorted(words)
    return sorted_words


def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_num = sorted(numbers, key=abs, reverse=True)
    return sorted_num


# do not modify below this line
original_words = ["cherry", "apple", "blueberry",
                  "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))


def sum_3_integers(triplet: List[int]) -> int:
    a, b, c = triplet
    return a + b + c


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    a, b, c = box_dimensions
    return a * b * c


# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_score, best_student_name = 0, ""

    for student, score in scores:
        if score > best_score:
            best_score, best_student_name = score, student
    return best_student_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90),
      ("Charlie", 80), ("David", 100)]))


def get_index_of_seven(nums: List[int]) -> int:
    if 7 not in nums:
        return -1
    else:
        for index, num in enumerate(nums):
            if num == 7:
                return index


def get_dist_between_sevens(nums: List[int]) -> int:
    first_seven_index = -1
    for i, num in enumerate(nums):
        if num == 7:
            if first_seven_index == -1:
                first_seven_index = i
            else:
                return i - first_seven_index


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))


def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    result = {}
    for name, score in zip(names, scores):
        result[name] = score
    return result


# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))


def is_arr_valid(names: List[str], max_length: int) -> bool:
    return 0 < len(names) <= max_length


# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 1))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 4))


def disallow_negatives(num: int) -> int:
    return max(0, num)


def max_difference(nums: List[int]) -> int:
    diff_list = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    return max(diff_list)


# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))


def max_difference(nums: List[int]) -> int:
    output = 0

    for i in range(len(nums) - 1):
        output = max(output, nums[i + 1] - nums[i])

    return output


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for i in arr2:
        arr1.append(i)
    return arr1


def pop_n(arr: List[int], n: int) -> List[int]:
    if n > len(arr):
        return []
    else:
        for i in range(n):
            arr.pop()
    return arr


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    if index < 0 or index >= len(arr):
        arr.append(element)
    else:
        arr.insert(index, element)
    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)
    return arr1


def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for integer in arr2:
        if integer in arr1:
            arr1.remove(integer)
    return arr1


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))


def combine_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    return arr1 + arr2


# do not modify below this line
arr1 = [1, 3, 5]
arr2 = [4, 6, 8]

print(combine_elements(arr1, arr2))
print(arr1)
print(arr2)
12345678910111213141516
arr2 = [4, 6, 8]

print(combine_elements(arr1, arr2))
print(arr1)
print(arr2)


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    arr = [0] * size
    arr[index] = value
    return arr


# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))

from functools import reduce
from itertools import zip_longest

"""
List and Accessing Item
Question: Create a list of the first 10 natural numbers. Access and print the 5th element in the list.
"""


def list_access(n, index):
    natural_numbers = [item for item in range(1, n + 1)]
    return natural_numbers[index]


# print(list_access(11, 5))


"""
List Packing and Unpacking
Question: Create a list of three items: "apple", "banana", and "cherry".
Unpack the list into three variables and print each variable.
"""

fruits = ["apple", "banana", "cherry", "orange", "pineapple"]
fruit1, fruit2, fruit3, *others = fruits
# print(fruit1)
# print(fruit2)
# print(fruit3)
# print(others)

"""
 Looping Over List
Question: Write a function print_list_items that takes a list as an argument and
prints each item in the list using a for loop.
"""


def print_list(items: list):
    for index, item in enumerate(items):
        print(index, item)


# print_list(["a", "b", "c"])


"""
4. Adding and Removing Items from List
Question: Create an empty list and perform the following operations:
Append the number 5 to the list.
Insert the number 10 at the beginning of the list.
Append the number 15 to the list.
Remove the first occurrence of the number 10.
Pop the last item from the list.
Clear the list.
"""

# my_list = []
# print(my_list)
# my_list.append(5)
# print(my_list)
# my_list.append("test")
# print(my_list)
# my_list.insert(0, 10)
# print(my_list)
# my_list.append(15)
# print(my_list)
# my_list.remove(10)
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.clear()
# print(my_list)


"""
Finding Item in List
Question: Create a list of numbers from 1 to 10. Write a function find_number that takes a list and
a number as arguments and returns the index of the number in the list if it exists.
Use list.index and if item in list to find the number.
"""


def find_number(input: list, target):
    if target in input:
        return input.index(target)
    return "None"


# print(find_number([1, 2, 3, 4, 5], 2))


"""
Sorting List
Question: Create a list of random numbers [4, 2, 9, 1, 5, 6].
Sort the list in ascending order and then in descending order using list.sort.
"""


def sort_list(input_list, flag):
    """
    The reason you are getting None as the output is that the list.sort()
    method sorts the list in place and returns None. Therefore, when you return the result of input_list.sort(),
    you are actually returning None.
    """
    # if flag.lower() == "asc":
    #     return input_list.sort()
    # else:
    #     return input_list.sort(reverse=True)
    if flag.lower() == "asc":
        input_list.sort()
    else:
        input_list.sort(reverse=True)
    return input_list


# print(sort_list([4, 2, 9, 1, 5, 6], "asc"))


"""
7. Sorted List
Question: Create a list of numbers [3, 1, 4, 1, 5, 9, 2].
Use the sorted function to return a new list that is sorted in ascending order and another new list that is sorted
in descending order without modifying the original list.
"""


def return_sorted_list(input_list):
    print(f"Original list: {input_list}, sorted in asc order: {
          sorted(input_list)}, sorted in desc order: {sorted(input_list, reverse=True)}")


# print(return_sorted_list([3, 1, 4, 1, 5, 9, 2]))


"""
8. Python program to interchange first and last elements in a list
Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]

"""


def interchange_nums(input_list: list):
    # List unpacking
    # first, *other, last = input_list
    # input_list[0] = last
    # input_list[-1] = first

    # Tuple assignment
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list


# print(interchange_nums([12, 35, 9, 56, 24]))

"""
9. Python Program to Swap Two Elements in a List

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]


Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""


def swap_two_elements(input_list: list, pos1, pos2):
    if (pos1 < 0 or pos2 > len(input_list)):
        return "Invalid arguments to swap"
    else:
        input_list[pos1 - 1], input_list[pos2 -
                                         1] = input_list[pos2 - 1], input_list[pos1 - 1]
    return input_list


# print(swap_two_elements([1, 2, 3, 4, 5], pos1=2, pos2=5))


"""
10. Sort elemens based on the second element in the list of tuples
"""


def sort_list_basedOn_value(input_list):
    return sorted(input_list, key=get_price[1])


def get_price(item):
    return item[1]


# print(sort_list_basedOn_value([("product1", 10),
#                                ("product2", 9),
#                                ("product3", 12)]))


"""
11. Do the same with lambda fucntion
"""


def sort_list_basedOn_value_lambda(input_list):
    # return sorted(input_list, key=lambda input_list: input_list[1])
    input_list.sort(key=lambda input_list: input_list[1])
    print(input_list)


# sort_list_basedOn_value_lambda([("product1", 10),
#                                 ("product2", 9),
#                                 ("product3", 12)])


"""
12. Basic Lambda Function

Question: Write a lambda function that takes a number x and returns x squared. Test it with the number 5.
"""


def return_square(x):
    print((lambda x: x**2)(x))


# return_square(5)

"""
13. Use map function to return only the second item in the list of tuple
"""


def return_second_item(input_list):
    op = list(map(lambda item: item[1], input_list))
    return op


items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

# print(return_second_item(items))  # Should print: [10, 9, 12]


"""
The first print(prices.sort()) returns None because the sort() method sorts the list in place and returns None.
This is a common mistake when using the sort() method.
"""
# prices = list(map(lambda items: items[1], items))
# print(prices.sort())

# print(prices)

"""
14. Using filter function return only values if items that are grater than or eqaul to 10 dollars
"""
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 15),
]

prices = list(filter(lambda items: items[1] >= 10, items))
# print(prices)


"""
15. Lambda with Map

Question: Use a lambda function with the map function to square each number in the list [1, 2, 3, 4, 5].
"""


def print_squares(input_list: list):
    result = map(lambda x: x*x, input_list)
    print(list(result))


# print_squares([1, 2, 3, 4])

"""
16. Lambda with Filter

Question: Use a lambda function with the filter function to filter out even numbers from the list [1, 2, 3, 4, 5].
"""


def filter_even_number(input_list):
    result = filter(lambda x: x % 2 != 0, input_list)
    print(list(result))


# filter_even_number([1, 2, 3, 4])

"""
17. Lambda with Reduce

Question: Use a lambda function with the reduce function from the functools module to calculate the product of all numbers in the list [1, 2, 3, 4, 5].
"""


def product_of_numbers_in_list(input_list):
    product = reduce(lambda x, y: x*y, input_list)
    print(product)


# product_of_numbers_in_list([1, 2, 3, 4, 5])


"""
18. Lambda with List Comprehension

Question: Use a lambda function inside a list comprehension to create a list of cubes of numbers from 1 to 10.
"""


def lambda_with_list_comprehension(input_list):
    # Create a lambda function to cube the input
    def cube_lambda(x): return x**3

    # Apply the lambda function to each item in input_list
    output_list = [cube_lambda(item) for item in input_list]

    print(output_list)


# lambda_with_list_comprehension([1, 2, 3, 4, 5])

"""
19. Problem: Sorting a list of tuples based on the second element of each tuple.
"""


def sort_tuple(input_tuple):
    input_tuple.sort(key=lambda input_tuple: input_tuple[1])
    print(input_tuple)


# sort_tuple([("Alice", 80), ("Bob", 75), ("Charlie", 90), ("David", 85)])

"""
20. Swap elements in String list
The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
replace G witg e in all ocurrances in the list
"""


def swap_elements_in_string(input_list):
    # Define a lambda function to perform both replacements
    def swap_lambda(item): return item.replace(
        "G", "X").replace("e", "G").replace("X", "e")

    # Apply the lambda function to each item in input_list using list comprehension
    new_list = [swap_lambda(item) for item in input_list]

    return new_list


# Example usage
# result_list = swap_elements_in_string(['Gfg', ' is ', 'Geeks'])
# print(result_list)


"""
21. Find sum of numbers
"""


def sum_of_numbers(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum


numbers = [1, 2, 3, 4]
# print(sum_of_numbers(numbers))

"""21. Reverses a given string using slicing and a loop."""


def reverse_string_inplace(text):
    output_string = ""
    for char in text[::-1]:
        output_string = output_string + char
    return output_string


# print(reverse_string_inplace("Hello world"))


"""
22. Remove duplicate form list
data = [1, 1, 2, 3, 4, 4, 4]
remove_duplicates(data)
"""


# def remove_duplicate_int(input_list):
#     non_duplicate_items = set()
#     for item in input_list:
#         if item not in non_duplicate_items:
#             non_duplicate_items.add(item)
#     return input_list, non_duplicate_items


# print(remove_duplicate_int([1, 1, 2, 3, 4, 4, 4]))

def remove_duplicate_int(input_list):
    return set(input_list)


# print(remove_duplicate_int([1, 1, 2, 3, 4, 4, 4]))


"""
22. Palindrome
"""


def is_palindrome(text):
    rev_string = ""
    for char in text[::-1]:
        rev_string = rev_string + char
    return text.lower() == rev_string.lower()


# print(is_palindrome("Ramar"))


"""
23. Find Maximum of two numbers in Python

Input: a = 2, b = 4
Output: 4

Input: a = -1, b = -4
Output: -1
"""


def return_max_of_two(a: int, b: int):
    return a if a > b else b


# print(return_max_of_two(-1, -4))

"""
24. Check if element exists in list in Python

Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.
"""


def check_if_element_exist(input_list, target_item):
    return target_item in input_list
    # return len([item for item in input_list if item == target_item]) != 0


# print(check_if_element_exist([1, 6, 3, 5, 3, 4], 0))

"""
25. Copying list
Python program to copy or clone a list Using the Slice Operator
"""

# def Cloning(li1):
# Approch 1
# li_copy = li1[:]

# Approch 2
# li_copy = []
# li_copy.extend(li1)

# Approch 3
# li_copy = li1
# return li_copy

"""
26. Count occurrences of an element in a list

Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
Output: 3
Explanation: 10 appears three times in given list.
Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
Output: 0
Explanation: 16 appears zero times in given list.
"""


def count_occurance_element(input_list, target_element):
    # The sum function adds up these 1s, giving the count of occurrences of target_element
    return sum(1 for item in input_list if item == target_element)


# print(count_occurance_element([8, 6, 8, 10, 8, 20, 10, 8, 8], 16))

"""
27. Python program to find second largest number in a list

Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70
"""


def find_second_largest(input_list):
    sorted_list = sorted(input_list)
    return sorted_list[-2]


# print(find_second_largest([70, 11, 20, 4, 100]))

"""
28: Create a list by picking an odd-index items from the first list and even index items from the second

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

Expected Output:
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""


def create_list(list1, list2):
    return list1[1::2] + list2[0::2]


# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# print(create_list(l1, l2))


"""
29. Write a function zip_uneven_lists(list1, list2) that zips two lists of different lengths.
What happens when you zip lists of different lengths?
"""

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24]


def zip_uneven_lists(list1, list2):
    print(list(zip(l1, l2)))


# Note that the last element is left out
# zip_uneven_lists(l1, l2)

# To combine the last element with 0


def zip_uneven_lists(list1, list2):
    result = list(zip_longest(list1, list2, fillvalue=0))
    print(result)


# zip_uneven_lists(l1, l2)

# Other appraoch - Using list comprehension
def zip_uneven_lists(list1, list2):
    max_length = max(len(list1), len(list2))
    result = [(list1[i] if i < len(list1) else 0, list2[i] if i <
               len(list2) else 0) for i in range(max_length)]
    print(result)


# zip_uneven_lists(l1, l2)

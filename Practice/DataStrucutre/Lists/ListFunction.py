from functools import reduce

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
# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 12),
#     ("product4", 15),
# ]

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
print(result_list)

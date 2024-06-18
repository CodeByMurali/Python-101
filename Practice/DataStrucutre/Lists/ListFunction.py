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


print(return_sorted_list([3, 1, 4, 1, 5, 9, 2]))

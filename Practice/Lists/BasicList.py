# 1. Fizz Buzz

def fizz_buzz(input):
    inputInteger = int(input)
    if (inputInteger % 3 == 0) and (inputInteger % 5 == 0):
        print("FizzBuzz")
    elif inputInteger % 3 == 0:
        print("Fizz")
    elif inputInteger % 5 == 0:
        print("Buzz")
    print(inputInteger)

# fizz_buzz(7)


# 2. Python program to interchange first and last elements in a list

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

# Appraoch 1

def interchange_elements(inputList):
    OutPutList = []
    for item in inputList:
        OutPutList.append(item)
    OutPutList[0] = inputList[-1]
    OutPutList[-1] = inputList[0]
    print(OutPutList)

# Approach 2


def interchange_elements(inputList):
    inputList[0], inputList[-1] = inputList[-1], inputList[0]
    print(inputList)

# Approach 3


def interchange_elements(inputList):
    # Packing
    get = (inputList[-1], inputList[0])

    # Unpack
    inputList[0], inputList[-1] = get

    print(inputList)

#  interchange_elements([12, 35, 9, 56, 24])

# 4. Python Program to Swap Two Elements in a List

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]


# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

# Approach 1


def swap_two_elements(inputList, pos1, pos2):
    inputList[pos1 - 1], inputList[pos2 -
                                   1] = inputList[pos2 - 1], inputList[pos1 - 1]
    print(inputList)

# Approach 2


def swap_two_elements(inputList, pos1, pos2):
    inputList[pos1], inputList[pos2] = inputList[pos2], inputList[pos1]
    print(inputList)

# Approach 3

# Python3 program to swap elements
# at given positions

# Swap function


def swapPositions(list, pos1, pos2):

    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)

    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

# print(swapPositions(List, pos1-1, pos2-1))


# 5. Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
# replace G witg e in all ocurrances in the list

# list comprehension
def swapStringList(inputStringList):
    res = [sub.replace('e', 'G')
           for sub in inputStringList]

    # printing result
    print("List after performing character swaps : " + str(res))

# swapStringList(['Gfg', 'is', 'best', 'for', 'Geeks'])


# 6. Find Maximum of two numbers in Python

# Input: a = 2, b = 4
# Output: 4

# Input: a = -1, b = -4
# Output: -1

def find_max_twoNumber(a: int,  b: int):
    # Approch 1
    # if a > b:
    #     print(f"Biggest number is {a}")
    # else:
    #     print(f"Biggest number is {b}")

    # Approch 2
    print(max(a, b))


# find_max_twoNumber(-1, -4)

# 7. Check if element exists in list in Python

# Input: test_list = [1, 6, 3, 5, 3, 4]
#             3  # Check if 3 exist or not.
# Output: True
# Explanation: The output is True because the element we are looking is exist in the list.

def check_element_exist(test_list, seaechItem):
    if seaechItem in test_list:
        print("element exist")
    else:
        print(f"Element {seaechItem} not found")


# check_element_exist(test_list=[1, 6, 3, 5, 3, 4], seaechItem=10)

# 9. Copying list
# Python program to copy or clone a list
# Using the Slice Operator
def Cloning(li1):
    # Approch 1
    # li_copy = li1[:]

    # Approch 2
    # li_copy = []
    # li_copy.extend(li1)

    # Approch 3
    li_copy = li1
    return li_copy


# Driver Code
# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1)
# print("After Cloning:", li2)


# 10. Count occurrences of an element in a list

# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
# Output: 3
# Explanation: 10 appears three times in given list.
# Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
# Output: 0
# Explanation: 16 appears zero times in given list.

def count_occurrence_of_element(lst: list, search_element: int):
    # Approch 1
    # x = [i for i in lst if i == search_element]
    # print("The element", search_element, "occurs", len(x), "times")

    # Approch 2
    # x = sum(1 for i in lst if i == search_element)
    # print("The element", search_element, "occurs", x, "times")

    # Approch 3
    print(lst.count(search_element))


# count_occurrence_of_element([15, 6, 7, 10, 12, 20, 10, 28, 10], 10)

# 11. Python program to find second largest number in a list

# Input: list1 = [10, 20, 4]
# Output: 10

# Input: list2 = [70, 11, 20, 4, 100]
# Output: 70

def find_second_largest_element(li):

    # To remove duplicates
    # set(li.sort())
    # print(li[-2])
    # new_list is a set of list1
    new_list = set(li)

    # Removing the largest element from temp list
    new_list.remove(max(li))

    # Elements in original list are not changed
    # print(list1)
    print(max(li))


# find_second_largest_element([10, 20, 4])


# https://pynative.com/python-data-structure-exercise-for-beginners/

# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second

# Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# Expected Output:
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]

# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]

l3 = [item for index, item in enumerate(l1) if index % 2 != 0]
l4 = [item for index, item in enumerate(l2) if index % 2 == 0]
print(l3 + l4)


# Approach 2:

# # Extracting odd-indexed elements from l1
# odd_index_l1 = [l1[i] for i in range(1, len(l1), 2)]

# # Extracting even-indexed elements from l2
# even_index_l2 = [l2[i] for i in range(0, len(l2), 2)]

# # Combining the two lists
# final_list = odd_index_l1 + even_index_l2

# print("Element at odd-index positions from list one:")
# print(odd_index_l1)
# print("Element at even-index positions from list two:")
# print(even_index_l2)
# print("\nPrinting Final third list:")
# print(final_list)


# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

# Given:

# list1 = [54, 44, 27, 79, 91, 41]
# Expected Output:

# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
# List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]

# list1 = [54, 44, 27, 79, 91, 41]

# indexFourItem = list1[4]
# list1.pop(4)
# list1.insert(2, indexFourItem)
# list1.append(indexFourItem)
# print(list1)


# Exercise 3: Slice list into 3 equal chunks and reverse each chunk

# Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Expected Outcome:

# Chunk  1 [11, 45, 8]
# After reversing it  [8, 45, 11]
# Chunk  2 [23, 14, 12]
# After reversing it  [12, 14, 23]
# Chunk  3 [78, 45, 89]
# After reversing it  [89, 45, 78]

# Sol
# Approach 1
# slice1 = sample_list[:3]
# slice2 = sample_list[3:6]
# slice3 = sample_list[6:]

# slice1.reverse()
# print(slice1)

# slice2.reverse()
# print(slice2)

# slice3.reverse()
# print(slice3)

# Approcah 2

# star_index = 0
# end_index = 3
# list_partition_count = len(sample_list)//3
# print(list_partition_count)

# for i in range(list_partition_count):
#     chunked_lis = sample_list[star_index: end_index]
#     star_index = star_index + 3
#     end_index = end_index + 3
#     print(list(reversed(chunked_lis)))

# # Approach 3

# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# print("Original list ", sample_list)

# length = len(sample_list)
# chunk_size = int(length / 3)
# start = 0
# end = chunk_size

# # run loop 3 times
# for i in range(3):
#     # get indexes
#     indexes = slice(start, end)

#     # get chunk
#     list_chunk = sample_list[indexes]
#     print("Chunk ", i, list_chunk)

#     # reverse chunk
#     print("After reversing it ", list(reversed(list_chunk)))

#     start = end
#     end += chunk_size


# Leet code 75
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

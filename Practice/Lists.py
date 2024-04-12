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


# def swap_two_elements(inputList, pos1, pos2):
#     inputList[pos1 - 1], inputList[pos2 -
#                                    1] = inputList[pos2 - 1], inputList[pos1 - 1]
#     print(inputList)

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


find_second_largest_element([10, 20, 4])

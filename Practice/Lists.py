# Fizz Buzz

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


# 1. Python program to interchange first and last elements in a list

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


# 2. Python Program to Swap Two Elements in a List

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


# 3. Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
# replace G witg e in all ocurrances in the list

# list comprehension
def swapStringList(inputStringList):
    res = [sub.replace('e', 'G')
           for sub in inputStringList]

    # printing result
    print("List after performing character swaps : " + str(res))


# 1. interchange_elements([12, 35, 9, 56, 24])


# 2. swap_two_elements([23, 65, 19, 90], 1, 3)
# inputList = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
# swap_two_elements(inputList, pos1 - 1, pos2 - 1)


swapStringList(['Gfg', 'is', 'best', 'for', 'Geeks'])

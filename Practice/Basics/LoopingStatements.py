# Sum of Numbers Using For Loop and Range
def sum_numbers(n):
    sum = 0
    for number in range(1, n+1):
        sum = sum + number
    return sum
# print(sum_numbers(5))


# Find Prime Numbers
# Write a function find_primes(n) that takes an integer n and prints all prime numbers less than n.
# a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
def find_primes(n):
    prime = []
    for number in range(2, n):
        for i in range(2, int(number ** 0.5 + 1)):
            if (number % i) == 0:
                break
        else:
            prime.append(number)
    return prime
# print(find_primes(15))


def first_repeating_char(s):
    input_str = s.lower()
    if len(s) <= 1:
        return "None"
    seen_char = set()
    for char in input_str:
        if char in seen_char:
            return char
        seen_char.append()
    return "None"
# print(first_repeating_char("eaq"))


# List Comprehension to Generate Squares
"""
Write a function generate_squares(n) that takes an integer n and returns a list of squares of numbers from 1 to n 
using a for loop and list comprehension.
"""


def generate_squares(n):
    return [number ** 2 for number in range(1, n+1)]
# print(generate_squares(5))


# Count Vowels in a String
# def count_vowels(s):
#     if len(s) == 0:
#         return "None"
#     vowels = []
#     for char in s.lower():
#         if char in ['a', 'e', 'i', 'o', 'u']:
#             vowels.append(char)
#     return len(vowels)
# print(count_vowels("mqweer"))

# Using list comprehension
def count_vowels(s):
    return sum(1 for char in s.lower() if char in ['a', 'e', 'i', 'o', 'u'])
# print(count_vowels("Hello World"))


# Escape sequence
# print("Menu \n Potato\twedges\n French \\fries\n Apple \'Fritter\"")


# Type conversion

"""
Question: Write a function convert_types that takes three arguments:
A string that represents an integer.
A string that represents a floating-point number.
A floating-point number.

The function should convert the string representations to their respective numeric types, add the two numbers, 
and then return the result as a string.
"""


def convert_types(a, b, c):
    return str((int(a) + float(b) + float(c)))


# print(convert_types("1", "4.2", 9.9))

"""
Truthy and Falsy Values
Question: Write a function is_truthy that takes an argument and returns True if the argument is truthy and False if it is falsy. 
Test the function with different values including None, 0, 0.0, [], {}, "0", and True.
"""


def is_truthy(input):
    return bool(input)


# print(is_truthy(None))
# print(is_truthy(0))
# print(is_truthy(0.0))
# print(is_truthy([]))
# print(is_truthy({}))
# print(is_truthy("0"))
# print(is_truthy(True))
# print(is_truthy(False))
# print(is_truthy("False"))
# print(is_truthy(-1))


"""
Write a function print_numbers_while that prints numbers from 1 to 10 using a while loop.
"""


def print_numbers_while(n: int):
    count = 1
    while (count <= n):
        print(count)
        count = count + 1


# print_numbers_while(5

"""
Write a function search_value that takes a list of integers and a target value. Use a while loop to search for the target value in the list. 
If the value is found, print "Found". 
If the loop completes without finding the value, use the else block to print "Not Found".
"""


# def search_value(intList: list, target: int):
#     while target in intList:
#         print("Found")
#         break
#     else:
#         print("Not found")


def search_value(intList: list, target: int):
    index = 0
    while index < len(intList):
        if intList[index] == target:
            print("Found")
            break
        index += 1
    else:
        print("Not found")


input_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

search_value(input_List, target=1)

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


print(first_repeating_char("eaq"))

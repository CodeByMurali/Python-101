# xargs: When you add * before the param name, python will consinder the parameters as a tuple
# xxargs: This will return a dictionary

"""
Question: Write a function add_numbers that takes two integers as arguments and returns their sum.
Specify the argument types and the return type.
"""


def add_numbers(a: int, b: int = 3) -> int:
    return a + b


# print(add_numbers(1))

"""
Question: Write a function sum_all that takes any number of integer arguments and returns their sum using *args.
"""


def sum_all(*input: int) -> int:
    return sum(num for num in input)


# print(sum_all(1, 2, 3, 0))


"""
**kwargs
Question: Write a function print_details that accepts a variable number of keyword arguments using **kwargs and
prints each key-value pair on a new line.
"""


def print_details(**car_specs):
    for spec, value in car_specs.items():
        print(f"{spec}: {value}")


# print_details(model=2020, make="kia", colour="white")


"""
Scope of Variables
Question: Write a function variable_scope that demonstrates the difference between local and global variables. 
Inside the function, define a local variable with the same name as a global variable and print both variables.
"""
firt_name = "Murali"
last_name = "Rajendran"


def variable_scope():
    firt_name = "Mark"
    print(firt_name)
    global last_name
    last_name = "Mayandi"
    print(last_name)


# variable_scope()


"""
FizzBuzz Problem Statement
Write a function fizzbuzz that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz". 
For numbers which are multiples of both three and five, print "FizzBuzz".
"""


def fizz_buzz(n):
    for number in range(1, n+1):
        if (number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        elif (number % 3 == 0):
            print("Fizz")
        elif (number % 5 == 0):
            print("Buzz")
        else:
            print(number)


# fizz_buzz(100)

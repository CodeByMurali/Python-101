# Exercise 5: Create a Python set such that it shows the element from both lists in a pair

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

# op  Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

final_list = [(item, item * item) for item in first_list]
# print(final_list)

# zip function
result = zip(first_list, second_list)
result_set = set(result)


# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# OP
# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}
instersection_set = (first_set & second_set)
print(instersection_set)
final_Set = first_set - instersection_set
print(final_Set)

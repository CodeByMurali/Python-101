# Exercise 4: Count the occurrence of each element from a list

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
num_count_dict = {item: sample_list.count(item) for item in sample_list}
# print(num_count_dict)

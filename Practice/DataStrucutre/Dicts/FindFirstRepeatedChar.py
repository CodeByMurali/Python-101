# Input: green apple
# Output: e

# In this case you dont care how many times a particular char is repeated
# Hence using a set is the best instead of using a dictionary
# We need a DS that just stores the keys

def first_repeated_char(input_string: str):
    char_set = set()
    for char in input_string.replace(" ", ""):
        if char in char_set:
            return char
        char_set.add(char)
    return None


print(first_repeated_char("green apple"))

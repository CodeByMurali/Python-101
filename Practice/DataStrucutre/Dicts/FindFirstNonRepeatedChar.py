# IP: a green apple
# OP: g

def find_first_non_repeated_char(input_string: str) -> str:
    char_count = {}
    # Count occurrences of each character
    for char in input_string:
        if char != " ":
            char_count[char] = char_count.get(char, 0) + 1

    # if you just iterate over the key value pairs, it might not be saved in the righ order
    # Dictionaries are hasmpas, they use hash functions to save the values, hency they are not in right order
    # Find the first non-repeated character
    for char in input_string:
        if char != " " and char_count[char] == 1:
            return char

    return None  # If no non-repeated character is found


print(find_first_non_repeated_char("a green apple"))  # Output: g

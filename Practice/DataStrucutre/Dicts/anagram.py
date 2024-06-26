"""Checks if two strings are anagrams (contain the same characters with the same frequency)."""
"""text1 = silent , text2 = listen"""


"""Issues:
Character Count Assumption: The current implementation assumes that each character should appear exactly twice (once in each string). 
However, this won't account for the frequency of characters correctly. For example, the strings "aabb" and "ab" would pass your check even though they are not anagrams.
Combined String Length: Combining the two strings and iterating over the combined string means that you are not separately counting occurrences in each string, which is essential for checking anagrams."""


def check_anagram(text1, text2):
    if len(text1) != len(text2):
        return False

    combined_string = (text1 + text2).lower()
    char_dict = {}
    for char in combined_string:
        char_dict[char] = char_dict.get(char, 0) + 1
    for int in char_dict.values():
        if int != 2:
            return False
    return True


print(check_anagram("silent", "listen"))


def is_anagram(text1, text2):
    """Checks if two strings are anagrams (contain the same characters with the same frequency)."""
    text1 = text1.lower()  # Convert to lowercase for case-insensitive comparison
    text2 = text2.lower()
    char_count = {}
    for char in text1:
        # Count occurrences of characters in text1
        char_count[char] = char_count.get(char, 0) + 1

    for char in text2:
        if char not in char_count or char_count[char] == 0:
            return False  # Return False if character not found in text1 or count becomes 0
        char_count[char] -= 1  # Decrement count for characters in text2

    return True  # If loop finishes without returning False, all characters matched


# Example usage
text1 = "silent"
text2 = "listen"
is_anagram_text = is_anagram(text1, text2)
print(is_anagram_text)  # Output: True


def are_anagrams(str1, str2):
    # Remove any spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of the strings are equal
    return sorted(str1) == sorted(str2)


# Example usage
string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')


# Most efficient

def is_anagram(text1, text2):
    # Convert to lowercase and remove spaces
    text1 = text1.replace(" ", "").lower()
    text2 = text2.replace(" ", "").lower()

    if len(text1) != len(text2):
        return False

    char_count = {}

    # Count occurrences of characters in text1 and text2 simultaneously
    for char1, char2 in zip(text1, text2):
        char_count[char1] = char_count.get(char1, 0) + 1
        char_count[char2] = char_count.get(char2, 0) - 1

    # Check if all counts are zero
    """all(...): The all() function takes an iterable 
    (in this case, the sequence of boolean values generated by the generator expression)
      and returns True if all elements in the iterable are True. Otherwise, it returns False"""
    return all(count == 0 for count in char_count.values())


# Example usage
text1 = "silent"
text2 = "listen"
is_anagram_text = is_anagram(text1, text2)
print(is_anagram_text)  # Output: True

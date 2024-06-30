class DictBasics:

    """    
    # Exercise 4: Count the occurrence of each element from a list
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

    #Lists conut function allowed
    charList = ['a', 'b', 'c', 'c', 'a']
    count_frequency_char(charList)
    """

    def count_ocurrance_of_element(self, int_list: list):
        return {integer: int_list.count(integer) for integer in int_list}

    # Lists count library function not allowed
    def count_ocurrance_of_chars(self, char_list: list):
        output_dict = {}
        for char in char_list:
            output_dict[char] = output_dict.get(char, 0) + 1
        return output_dict

    """
    For the given string find the most repeated character
    sentence = "This is a common interview question"
    """

    def most_repeated_char(self, input_string: str):
        output_dict = {}
        max_value = 0
        max_char = ''
        for char in input_string.lower():
            if char != " ":
                output_dict[char] = output_dict.get(char, 0) + 1
                if output_dict[char] > max_value:
                    max_value = output_dict[char]
                    max_char = char
        print(f"The most repeated char if {
              max_char}, it ocurred {max_value} time")

    """
    Checks if two strings are anagrams (contain the same characters with the same frequency).
    text1 = silent , text2 = listen
    """

    def is_angram(self, text1: str, text2: str):
        text1_dict = {}
        text2_dict = {}
        if len(text1) != len(text2):
            return False

        for char in text1:
            text1_dict[char] = text1_dict.get(char, 0) + 1

        for char in text2:
            text2_dict[char] = text2_dict.get(char, 0) + 1

        return text1_dict == text2_dict


dictBasics = DictBasics()
# print(dictBasics.count_ocurrance_of_element(
#     [11, 45, 8, 11, 23, 45, 23, 45, 89]))
# print(dictBasics.count_ocurrance_of_chars(['a', 'b', 'c', 'c', 'a']))
# dictBasics.most_repeated_char("This is a common interview question")
print(dictBasics.is_angram("listen", "silent"))


# For the given string find the most repeated character

sentence = "This is a common interview question"

# listOfChar = [char.capitalize() for char in sentence if char != " "]
# charCountList = [(char, listOfChar.count(char)) for char in listOfChar]


# sorted_list = sorted(charCountList, key=lambda x: x[1])

# print(f"The most repeating char in the sentence is {
#       sorted_list[-1][0]}. It occurred {sorted_list[-1][1]} times.")

# # Approach 2 using dictionaries


# dict_given = {char: sentence.count(char) for char in sentence}

# dict_sorted = dict(
#     sorted(dict_given.items(), key=lambda item: item[1], reverse=True))

# for key, val in dict_sorted.items():
#     print(f"The most repeated cahr is {key}. it is repeated for {val} times")
#     break


# Approach 2

# char_count = {}
# max_char = ''
# max_count = 0

# for char in sentence:
#     if char != ' ':  # Exclude spaces from counting
#         # Set default value 0 to the cahr for the first time and add 1 to it
#         char_count[char] = char_count.get(char, 0) + 1
#         if char_count[char] > max_count:
#             max_char = char
#             max_count = char_count[char]

# print(f"The most repeated character is '{
#       max_char}'. It is repeated {max_count} times.")

# Approach 3
# mostRepeatedChar = ''
# charList = []
# count = 0
# maxCount = 1
# for char in sentence:
#     if char != ' ':
#         charList.append(char)
# for item in charList:
#     count = charList.count(item)
#     if count > maxCount:
#         maxCount = count
#         print(f"The most repeating char in the sentence is {item}")

sentence = "This is a common interview question"
charCount = {}
maxCount = 0
maxChar = ''

for char in sentence:
    if char != ' ':
        charCount[char] = charCount.get(char, 0) + 1
        if charCount[char] > maxCount:
            maxCount = charCount[char]
            maxChar = char
print(f"The most repeated character is '{
      maxChar}'. It is repeated {maxCount} times.")

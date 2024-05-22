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

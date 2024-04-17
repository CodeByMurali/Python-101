# For the given string find the most repeated character

sentence = "This is a common interview question"

listOfChar = [char.capitalize() for char in sentence if char != " "]
charCountList = [(char, listOfChar.count(char)) for char in listOfChar]


sorted_list = sorted(charCountList, key=lambda x: x[1])

print(f"The most repeating char in the sentence is {
      sorted_list[-1][0]}. It occurred {sorted_list[-1][1]} times.")

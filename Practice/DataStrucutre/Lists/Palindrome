# def is_palindrome(text):
#     rev_string = ""
#     for char in text:
#         rev_string = char + rev_string
#     if rev_string == text:
#         print(f"{text} is a palindrome")
#     print(f"{text} is not a palindrome")


# is_palindrome("malayalam")


# Using two pointer algorithm

def check_palindrome(text):
    text = text.lower()
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


is_palindrome = check_palindrome("malayalam")
print(is_palindrome)

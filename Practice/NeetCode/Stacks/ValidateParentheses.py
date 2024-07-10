class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        # We create a hashmap to get what would be the corresponding closing char
        # for a given opening char
        close_bracket_dict = {'}': '{', ']': '[', ')': '('}

        for char in s:
            # Filtering only closing brackets as the below
            # statement only looks at the keys
            if char in close_bracket_dict:
                # The stack must not be empty as the first element
                # must not be a closing bracket
                if stack and stack[-1] == close_bracket_dict[char]:
                    # If the brackets matches pop them out
                    stack.pop()
                else:
                    return False
            else:
                # Appenf any number of closing chars
                stack.append(char)
        # true only when the array is empty as we pop out all matching brackets
        return True if not stack else False

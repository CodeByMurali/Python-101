"""
Write a function is_balanced(expression) that takes a string expression containing characters like {, }, [, ], (, and ) 
and returns True if the expression is balanced, 
meaning every opening bracket has a corresponding closing bracket in the correct order, and False otherwise.

For example:

is_balanced("{[()]}") should return True
is_balanced("{[(])}") should return False
is_balanced("{{[[(())]]}}") should return True
"""


def is_balanced_expression(text):
    if not text:
        raise ValueError("Input string is empty")

    my_stack = []
    # Allow only braces
    for char in text:
        if char in "{[(<>)]}":
            # Add only open bracket
            if char in "{[<(":
                my_stack.append(char)
            elif char == '}':
                if len(my_stack) == 0 or my_stack.pop() != '{':
                    return False
            elif char == ']':
                if len(my_stack) == 0 or my_stack.pop() != '[':
                    return False
            elif char == '>':
                if len(my_stack) == 0 or my_stack.pop() != '<':
                    return False
            elif char == ')':
                if len(my_stack) == 0 or my_stack.pop() != '(':
                    return False
    return True


print(is_balanced_expression("{[(])}"))

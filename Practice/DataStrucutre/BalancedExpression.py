import StacksUsingList


def balancedExpression(inputString: str) -> bool:
    if not inputString:
        raise ValueError("Input string is empty")

    # Clear the stack before using it
    StacksUsingList.clear()

    for char in inputString:
        if char in "()<>{}[]":
            if char in '(<[{':
                StacksUsingList.push(char)
            elif char == ')':
                if StacksUsingList.isEmpty() or StacksUsingList.pop() != '(':
                    return False
            elif char == '>':
                if StacksUsingList.isEmpty() or StacksUsingList.pop() != '<':
                    return False
            elif char == '}':
                if StacksUsingList.isEmpty() or StacksUsingList.pop() != '{':
                    return False
            elif char == ']':
                if StacksUsingList.isEmpty() or StacksUsingList.pop() != '[':
                    return False

    return StacksUsingList.isEmpty()


# Example usage
if __name__ == "__main__":
    print(balancedExpression("(<>)"))  # Should return True
    print(balancedExpression("(<>{})"))  # Should return True
    print(balancedExpression("(<{[}>])"))  # Should return False

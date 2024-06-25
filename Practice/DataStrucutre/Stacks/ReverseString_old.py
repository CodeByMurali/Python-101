# Import the StackUsingList module
import StacksUsingList


def reverseString(inputString: str):
    for char in inputString:
        # Use the push method from StackUsingList module
        StacksUsingList.push(char)

    reversedString = ''
    while not StacksUsingList.isEmpty():  # Use the isEmpty method from StackUsingList module
        # Use the pop method from StackUsingList module
        reversedString += StacksUsingList.pop()

    print(reversedString)


if __name__ == "__main__":
    reverseString("Test")

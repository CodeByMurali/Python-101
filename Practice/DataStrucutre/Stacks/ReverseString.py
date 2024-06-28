class ReverseString:

    def __init__(self) -> None:
        self.stack = []

    def reverse_string(self, input_string: str) -> str:
        output_string = ""
        for char in input_string:
            self.stack.append(char)

        while self.stack:
            output_string = output_string + self.stack.pop()

        return output_string


reverser = ReverseString()
print(reverser.reverse_string("hello"))

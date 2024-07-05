class Logger:
    def __init__(self) -> None:
        # Initialize the logger with a dictionary to store the messages and their allowed timestamps
        self.message_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If the message is not in the dictionary or the current timestamp is greater or equal
        # to the allowed timestamp, then update the allowed timestamp and return True
        if message not in self.message_dict or timestamp > self.message_dict[message]:
            self.message_dict[message] = timestamp + 10
            return True
        else:
            return False


# Example usage:
logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))  # return True
print(logger.shouldPrintMessage(2, "bar"))  # return True
print(logger.shouldPrintMessage(3, "foo"))  # return False
print(logger.shouldPrintMessage(8, "bar"))  # return False
print(logger.shouldPrintMessage(10, "foo"))  # return False
print(logger.shouldPrintMessage(11, "foo"))  # return True

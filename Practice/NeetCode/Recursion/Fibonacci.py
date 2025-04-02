import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()


def fibonacci(n):
    logger.info(f"Entering fibonacci({n})")
    # Base case: F(0) = 0
    if n == 0:
        logger.info(f"Returning 0 for fibonacci({n})")
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        logger.info(f"Returning 1 for fibonacci({n})")
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        logger.info(f"Returning {result} for fibonacci({n})")
        return result


# Example usage
n = 5
logger.info(f"Fibonacci number F({n}) is: {fibonacci(n)}")

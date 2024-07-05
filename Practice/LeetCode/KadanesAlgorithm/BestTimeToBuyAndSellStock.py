def maximum_profit_problem(prices):

    # setting it to max value so that i can update this later wiht a value form the array which rest assured is a minimum of the infinity
    min_value = float('inf')
    profit = 0

    for price in prices:
        if price < min_value:
            # Update min value with the lowest price encountered
            min_value = price
        # If its not a min value we dont worry about calculating the profit
        # Becase it is known that the profit will be lesser than the value that we currently is in
        elif price - min_value > profit:
            profit = price - min_value
    return profit


# Using 2 pointer sliding window approach
def maximum_profit_slidingWindow(prices):
    """
    left represents the day you buy the stock, and right represents the day you sell the stock.
    """
    left, right = 0, 1
    max_profit = 0
    while right <= len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
        else:
            left = right
        right = right + 1
    return max_profit

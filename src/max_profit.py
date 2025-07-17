def max_profit(prices):
    """
    Calculate the maximum profit from a list of stock prices by buying and selling once.

    :param prices: List[int] - prices[i] is the price on day i
    :return: int - maximum profit achievable
    """
    if len(prices) < 2:
        return 0  # Cannot buy and sell with fewer than 2 days

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        # Track the lowest price so far
        if price < min_price:
            min_price = price
        # Check if selling now gives a better profit
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit

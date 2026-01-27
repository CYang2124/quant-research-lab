import numpy as np

def simple_returns(prices):
    """
    Input: price array
    Output: simple return array
    """
    prices = np.asarray(prices)
    return prices[1:] / prices[:-1] - 1


def log_returns(prices):
    """
    Input: price array
    Output: log return array
    """
    prices = np.asarray(prices)
    return np.log(prices[1:]/prices[:-1])

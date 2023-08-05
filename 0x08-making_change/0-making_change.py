#!/usr/bin/python3
"""Making change
"""


def makeChange(coins, total):
    """make change function"""
    if total <= 0:
        return 0
    coins = sorted(list(set(coins)), reverse=True)
    ret = None
    for i in range(len(coins)):
        if coins[i] <= total:
            if ret and ret <= total // coins[i]:
                return ret
            change = getNumCoin(total % coins[i], coins[i:], total // coins[i])
            if not ret and change:
                ret = change
            if change and ret and change < ret:
                ret = change
    return -1


def getNumCoin(div, coins, count):
    """returns number of coins for an iteration"""
    for coin in coins:
        if coin > div:
            continue
        if not div % coin:
            return count + div // coin
        ret = getNumCoin(div % coin, coins, count + div // coin)
        if ret:
            return ret

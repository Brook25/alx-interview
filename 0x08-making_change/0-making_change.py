#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given
amount total"""


def makeChange(coins, total):
    """Return fewest number of coins needed to meet total"""

    if total <= 0:
        return (0)

    coins.sort(reverse=True)

    count = 0
    tmp = 0

    for i in coins:
        tmp = int(total / i)
        total = total - (tmp * i)
        count += tmp
        if total == 0:
            return (count)
    if total != 0:
        return (-1)

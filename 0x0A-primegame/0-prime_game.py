#!/usr/bin/python3
"""determine who the winner of each game is."""


def primes(n):
    """player that won the most rounds"""
    prime = []
    tmp = [True] * (n + 1)
    for i in range(2, n + 1):
        if (tmp[i]):
            prime.append(i)
            for j in range(i, n + 1, i):
                tmp[j] = False
    return prime


def isWinner(x, nums):
    """Return: Name of winner or None if winner cannot be found"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None

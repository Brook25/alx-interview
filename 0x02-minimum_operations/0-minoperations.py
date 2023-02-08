#!/usr/bin/python3
'''This module conatains a function that does the minimum operations
to get the given number of characters in a file.
'''


def minOperations(n):
    '''Returns the minimum number of operations
    needed to get n number of characters in a file
    '''
    m = n
    for i in range(n//2):
        if i > 0:
            k = n / i
            if k == int(k) and k + i < m:
                m = int(k + i)
    return m if m > 1 else 0

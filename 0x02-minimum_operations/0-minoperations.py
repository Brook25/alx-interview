#!/usr/bin/python3
'''This module conatains a function that does the minimum operations
to get the given number of characters in a file.
'''

m = 0


def minOperations(n):
    '''Returns the minimum number of operations
    needed to get n number of characters in a file
    '''
    global m
    for i in range(int(n//2)):
        if i > 1 and n / i == int(n / i):
            m += i
            minOperations(n / i)
            break
        if i == n//2 - 1: 
            m += n
    return int(m)

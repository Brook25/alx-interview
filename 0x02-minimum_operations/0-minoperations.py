#!/usr/bin/python3
'''This module conatains a function that does the minimum operations challange'''


def MinOperations(n):
    '''Returns the minimum number of operations
    '''
    m = n
    for i in range(n//2):
        if i > 0:
            k = n / i
            if k == int(k) and k + i < m:
                    m = int(k + i)
    return m

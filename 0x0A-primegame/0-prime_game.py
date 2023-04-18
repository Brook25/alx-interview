#!/usr/bin/python3
'''Module contains function that does
the prime game challange
'''


def isWinner(x, nums):
    '''Fucntion does the prime game challange'''
    max_val = max(nums) + 1
    lst_comp = {0, 1}
    for i in range(max_val):
        if i not in lst_comp:
            lst_comp.update(set((filter(lambda a: a % i == 0,
                            list(range(i + 1, max_val))))))
    dct = {'M': 0, 'B': 0}
    for i in range(x):
        x = 'B'
        for j in range(nums[i] + 1):
            if j not in lst_comp:
                x = 'M' if x == 'B' else 'B'
        dct[x] += 1
    if dct['M'] == dct['B']:
        return None
    return 'Maria' if dct['M'] > dct['B'] else 'Ben'

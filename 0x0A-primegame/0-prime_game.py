#!/usr/bin/python3
'''Module contains function that does
the prime game challange
'''

def isWinner(x, nums):
    '''Fucntion does the prime game challange'''
    if nums:
        dct = {'M': 0, 'B': 0}
        for i in range(x):
            vals, x = {0, 1}, 'B'
            if i >= len(nums):
                break
            for j in range(nums[i] + 1):
                if j not in vals:
                    x = 'M' if x == 'B' else 'B'
                    vals.update(set(filter(lambda x: x % j == 0,
                        set(range(j, nums[i] + 1)))))
            dct[x] += 1
        if dct['M'] == dct['B']:
            return None
        return 'Maria' if dct['M'] > dct['B'] else 'Ben'

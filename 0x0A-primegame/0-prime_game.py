#!/usr/bin/python3
'''Module contains function that does
the prime game challange
'''

def isWinner(x, nums):
    '''Fucntion does the prime game challange'''
    dct = {'M': 0, 'B': 0}
    if nums[0] == 0:
        return None
    for i in range(x):
        vals, x = {0, 1}, 'B'
        for j in range(nums[i] + 1):
            if j not in vals:
                x = 'M' if x == 'B' else 'B'
                vals.update(set(filter(lambda x: x % j == 0,
                    set(range(j, nums[i] + 1)))))
        dct[x] += 1
    if dct['M'] == dct['B']:
        return None
    return 'Maria' if dct['M'] > dct['B'] else 'Ben'


#nums = [0] * 10000
#for i in range(10000):
#    nums[i] = i


#nums = [0] * 100
#for i in range(100):
#    nums[i] = i * i

#print("Winner: {}".format(isWinner(100, nums)))


#print("Winner: {}".format(isWinner(10000, nums)))

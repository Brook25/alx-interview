#!/usr/bin/python3
'''Module contains a method that checks for unlockable boxes'''


def canUnlockAll(boxes):
    '''Determines if all boxes
    can be opened.
    '''
    keys = chk_keys = len(boxes)
    found_keys = []
    for i in range(keys - 1):
        for j in boxes[i]:
            if j not in found_keys and 0 < j <= keys - 1:
                found_keys += [j]
                chk_keys -= 1
    return False if chk_keys > 1 else True

#!/usr/bin/python3
'''Module contains function that does the
island perimeter challange
'''


def island_perimeter(grid):
    '''Function returns the perimeter of an island'''
    lst = []
    for y in range(len(grid)):
        if 1 not in grid[y]:
            continue
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                lst += [[x, y]]
    perim = 0
    for x in lst:
        perim += 4
        if [x[0]+1, x[1]] in lst:
            perim -= 1
        if [x[0]-1, x[1]] in lst:
            perim -= 1
        if [x[0], x[1]+1] in lst:
            perim -= 1
        if [x[0], x[1]-1] in lst:
            perim -= 1
    return perim

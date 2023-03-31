#!/usr/bin/python3
'''Module contains function that does the
island perimeter challange
'''


def island_perimeter(grid):
    '''Function returns the perimeter of an island'''
    perim = 0
    for y in range(len(grid)):
        if 1 not in grid[y]:
            continue
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                if grid[y+1][x] != 1:
                    perim += 1
                if grid[y-1][x] != 1:
                    perim += 1
                if grid[y][x-1] != 1:
                    perim += 1
                if grid[y][x+1] != 1:
                    perim += 1
    return perim

#!/usr/bin/python3
'''Module contains function that does the
island perimeter challange
'''


def island_perimeter(grid):
    '''Function returns the perimeter of an island'''
    perim = 0
    for y in range(len(grid) - 1):
        if 1 in grid[y]:
            for x in range(len(grid[0]) - 1):
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

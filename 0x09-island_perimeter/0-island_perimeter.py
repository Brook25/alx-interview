#!/usr/bin/python3
'''Module contains function that does the
island perimeter challange
'''


def island_perimeter(grid):
    '''Function returns the perimeter of an island'''
    perim = 0
    for y in range(len(grid)):
        if 1 in grid[y]:
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    if y == len(grid) - 1 or not grid[y+1][x]:
                        perim += 1
                    if y == 0 or not grid[y-1][x]:
                        perim += 1
                    if x == 0 or not grid[y][x-1]:
                        perim += 1
                    if x == len(grid[0]) - 1 or not grid[y][x+1]:
                        perim += 1
    return perim

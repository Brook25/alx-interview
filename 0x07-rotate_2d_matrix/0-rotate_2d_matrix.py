#!/usr/bin/python3
'''Module with a function that rotates
a 2-D matrix 90 degrees.
'''


def rotate_2d_matrix(matrix):
    '''Function rotates 2-D matrix 90 degrees
    '''
    mat_mirr = list(map(lambda x: list(map(lambda y: y, x)), matrix))
    i, j = 0, len(matrix) - 1
    while i < len(matrix):
        for k in range(len(matrix)):
            matrix[k][j] = mat_mirr[i][k]
        i, j = i + 1, j - 1

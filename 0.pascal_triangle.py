#!/usr/bin/python3
'''This Module contains a method that retuns pascal's triangle.'''


def pascal_triangle(n):
    '''Returns a list of lists of integers
    (pascal's triangle) depending on n.'''

    if n <= 0:
        return []

    list1 = [1]
    list_val = [[1]]
    for i in range(n - 1):
        list2 = list1.copy()
        list1 = [1]
        m = len(list2)
        for k in range(m//2):
            list1 += [list2[k] + list2[k + 1]]
        list1 += list1[-2::-1] if m % 2 == 0 else list1[::-1]
        list_val += [list1]
    return list_val


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(9))

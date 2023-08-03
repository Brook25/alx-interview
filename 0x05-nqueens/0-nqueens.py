#!/usr/bin/env python3
"""N-queens challange using backtracking algorithm.
   Without using much constraint propagation or heuristic selection.
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def main():
    '''Main function to print out all possible solutions
    of a given N queen puzzle
    '''
    for i in range(n):
        lst2 = [[0, i]]
        chk_queens(lst2, [], n)


def chk_queens(lst2, lst_col, n):
    '''recursively checks for possible mathces'''
    if len(lst2) == n:
        print(lst2)
        return
    for k in range(n):
        if k not in lst_col and chk_mate(lst2, [lst2[-1][0] + 1, k]):
            lst2 += [[lst2[-1][0] + 1, k]]
            lst_col += [k]
            chk_queens(lst2, lst_col, n)
            lst2.pop()
            lst_col.pop()


def chk_mate(lst1, lst2):
    '''checks if two spots can hhold queens
       without attacking eachother
    '''
    for lst in lst1:
        if lst[1] == lst2[1]:
            return False

        if lst[0] < lst2[0] and lst[1] < lst2[1]:
            n = lst2[0] - lst[0]
            if lst2[1] == lst[1] + n:
                return False
            else:
                continue

        if lst[0] < lst2[0] and lst[1] > lst2[1]:
            n = lst2[0] - lst[0]
            if lst2[1] == lst[1] - n:
                return False
    return True


if __name__ == "__main__":
    main()

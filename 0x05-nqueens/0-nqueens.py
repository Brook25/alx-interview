#!/usr/bin/python3
'''N-queens challange. Time complexity of this program is relatively higher.
will be optimzed.
'''


import sys
import time

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

lst2, lst1, lstr = [], [], []


def main():
    '''Main function to print out all possible solutions
    of a given N queen puzzle
    '''
    global lst2, n, time
    for j in range(n):
        lst2 = [[0, j]]
        start = time.time()
        chk_queens(all_spots([0, j]))
        print(start - time.time())

def all_spots(lst):
    '''returns all spots of non-attacking queens
    for a given index'''
    start = time.time()
    global lst2, lst1, lstr, n
    if lst1 == []:
        ls = list(range(n))
        for i in range(n):
            lst1 += map(lambda x: [i, x], ls)

    if lstr != []:
        ls = list(range(n))
        lst1 += list(map(lambda x: [lstr[0], x], ls))
        lst1 += list(map(lambda x: [x, lstr[1]], ls))
        lst1 += lstr[2:]
        lst1.remove([lstr[0], lstr[1]])
    lst1.remove([lst[0], lst[1]])
    lstr = [lst[0], lst[1]]
    k, j, m = lst[0] + 1, lst[1] + 1, lst[1] - 1
    while k < n:
        if m >= 0:
            lst1.remove([k, m])
            lstr += [[k, m]]
            m -= 1
        if j < n:
            lst1.remove([k, j])
            lstr += [[k, j]]
            j += 1
        k += 1

    k, j, m = lst[0] - 1, lst[1] - 1, lst[1] + 1
    while k >= 0:
        if j >= 0:
            lst1.remove([k, j])
            lstr += [[k, j]]
            j -= 1
        if m < n:
            lst1.remove([k, m])
            lstr += [[k, m]]
            m += 1
        k -= 1

    for j in range(n):
        if j != lst[0]:
            lst1.remove([j, lst[1]])

    for i in range(n):
        if i != lst[1]:
            lst1.remove([lst[0], i])
    end = time.time()
    print('-->', end - start)
    return lst1


def chk_queens(ls):
    '''recursively checks for possible mathces'''
    global lst2, n
    
    for i in range(len(ls)):
        if (len(ls[i:]) < n - len(lst2)):
            return
        lst2 += [ls[i]]
        if len(lst2) == n:
            print(lst2)
            lst2.pop()
            return
        lst3 = []
        for j in ls[i + 1:]:
            if (ls[i][0] != j[0] and ls[i][1] != j[1] and chk_mate(ls[i], j)):
                lst3 += [j]
        if len(lst3) >= n - len(lst2):
            chk_queens(lst3)
        lst2.pop()

def chk_mate(lst1, lst2):
    '''checks if two spots can hhold queens
    without attacking eachother'''

    if lst1[0] > lst2[0] and lst1[1] < lst2[1]:
        n = lst1[0] - lst2[0]
        return False if lst2[1] == lst1[1] + n else True
    if lst1[0] > lst2[0] and lst1[1] > lst2[1]:
        n = lst1[0] - lst2[0]
        return False if lst2[1] == lst1[1] - n else True
    if lst1[0] < lst2[0] and lst1[1] < lst2[1]:
        n = lst2[0] - lst1[0]
        return False if lst2[1] == lst1[1] + n else True
    if lst1[0] < lst2[0] and lst1[1] > lst2[1]:
        n = lst2[0] - lst1[0]
        return False if lst2[1] == lst1[1] - n else True


main()

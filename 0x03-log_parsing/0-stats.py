#!/usr/bin/python3
'''This module contains a script that reads computer metrics line
by line and prints statistics at certain intervals of keyboard interrupt
'''
import sys


st_cds = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
          "404": 0, "405": 0, "500": 0}


def log_parse(i, d):
    '''Prints stats based on status code
    to stdout
    '''
    print("File size: {}".format(i))
    st_lst = ["200", "301", "400", "401", "403", "404", "405", "500"]
    for k in st_lst:
        if k in d and d[k] != 0:
            print("{}: {}".format(k, d[k]))

n = a = 0
try:
    for i in sys.stdin:
        try:
            a += int(i.split()[-1])
            m = i.split()[-2]
            if m in st_cds.keys():
                st_cds[m] += 1
        except:
            pass
        if n == 9:
            log_parse(a, st_cds)
            n = -1
        n += 1
    log_parse(a, st_cds)
except KeyboardInterrupt:
    log_parse(a, st_cds)
    raise

#!/usr/bin/python3
'''This module contains a script that reads computer metrics line
by line and prints statistics at certain intervals of keyboard interrupt
'''
import sys


st_cds = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
          "404": 0, "405": 0, "500": 0}


def log_parse(total_size, st_cds):
    '''Prints stats based on status code
    to stdout
    '''
    print("File size: {}".format(total_size))
    st_lst = sorted(st_cds.keys())
    for k in st_lst:
        if st_cds[k] != 0:
            print("{}: {}".format(k, st_cds[k]))

n = total_size = 0
try:
    for line in sys.stdin:
        try:
            total_size += int(line.split()[-1])
            st_cd = line.split()[-2]
            if st_cd in st_cds.keys():
                st_cds[st_cd] += 1
        except ValueError and IndexError:
            pass
        if n == 9:
            log_parse(total_size, st_cds)
            n = -1
        n += 1
    log_parse(total_size, st_cds)
except KeyboardInterrupt:
    log_parse(total_size, st_cds)
    raise

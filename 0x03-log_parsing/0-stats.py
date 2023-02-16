#!/usr/bin/python3
'''This module contains a script that reads computer metrics line
by line and prints statistics at certain intervals of keyboard interrupt
'''
import sys
from time import sleep
import random


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


#def check_str(sr):
#    chk = sr.strip()
#    if len chk[0].strip('.') != 4:
#        return 0
#    for i in chk[0].strip('.'):
#        if !(1 <= int(i) <= 255):
#            return 0
#    if chk[1] != '-' or chk[2] :
#        ret

n = a = 0
for i in sys.stdin:
    try:
        #sleep(random.random())
        a += int(i.split()[-1])
        #print(a)
        m = i.split()[-2]
        #print(m)
        y = st_cds.get(m)
        if y is not None:
            st_cds[m] += 1
        if n == 9:
            log_parse(a, st_cds)
            n = -1
        n += 1
    except KeyboardInterrupt:
        log_parse(a, st_cds)
        raise KeyboardInterrupt from None

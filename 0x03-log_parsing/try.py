#!/usr/bin/python3

import datetime
import sys



x = sys.stdin
for line in x:
    y = eval(line.split('[')[1][:-1])
print(y, type(y));

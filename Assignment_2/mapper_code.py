#!/usr/bin/env python

import sys
for line in sys.stdin:
    # remove leading and trailing whitespace1
    line = line.strip()
    values = line.split(',')
    # print(values[0], values[3])
    try:
        print(int(values[0]), float(values[3]))
    except:
        print(values)
        
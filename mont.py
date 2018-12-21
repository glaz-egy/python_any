# -*- coding: utf-8 -*-

import random
import sys

def monte(n):
    i = 0
    for x in range(n):
        x, y = (random.random(), random.random())
        if x**2 + y**2 <= 1:
            i += 1
    return i

n = int(sys.argv[1])
m = monte(n)
print((m/n)*4)
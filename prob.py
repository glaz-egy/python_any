# -*- coding: utf-8 -*-

MaxNum = 2
num = 0
def prob(MaxNum):
    num = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    if (i == MaxNum or j == MaxNum or k == MaxNum or l == MaxNum) and (i <= MaxNum and j <= MaxNum and k <= MaxNum and l <= MaxNum):
                        num += 1
    return num

one = 1**4
two = 2**4 - one
thr = 3**4 - (one+two)
fo  = 4**4 - (one+two+thr)
fi  = 5**4 - (one+two+thr+fo)
six = 6**4 - (one+two+thr+fo+fi)
print(prob(1), one)
print(prob(2), two)
print(prob(3), thr)
print(prob(4), fo)
print(prob(5), fi)
print(prob(6), six)

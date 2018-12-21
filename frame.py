N = float(input())
a = list(map(float, input().split()))
aver = sum(a)//N

inta = (0, -1, 1, -2, 2, -3, 3)

for atest in inta:
    if atest+aver in a:
        print(a.index(atest+aver))
        break
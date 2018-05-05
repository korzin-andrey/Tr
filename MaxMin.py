num = [int(i) for i in input().split()]
imax = num.index(max(num))
imin = num.index(min(num))
num[imax], num[imin] = num[imin], num[imax]
print(' '.join([str(i) for i in num]))

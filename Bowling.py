N, k = map(int, input().split())
a = []
for i in range(k):
    a.append(list(map(int, input().split())))
keg = []
for i in range(N):
    keg.append('I')
for i in range(k):
    for t in range(a[i][0], (a[i][1]+1), 1):
        keg[t-1] = '.'
print(''.join(keg))

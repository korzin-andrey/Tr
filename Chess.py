a = []
k = 8
for i in range(k):
    s = []
    for j in range(k):
        s.append('.')
    a.append(s)
pos = input()
a[int(pos[1]) - 1][ord(pos[0]) - ord('a')] = 'K'
pos_str = int(pos[1]) - 1
pos_twr = ord(pos[0]) - ord('a')
for i in range(k):
    for j in range(k):
        if  abs(i - pos_str) == 1:
            if abs(j - pos_twr) == 2:
                a[i][j] = '*'
        if  abs(i - pos_str) == 2:
            if abs(j - pos_twr) == 1:
                a[i][j] = '*'
for i in range(k-1, -1, -1):
    print(' '.join(a[i]))

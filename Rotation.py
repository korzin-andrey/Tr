n, m = (map(int, input().split()))
mas = []
for i in range(n):
    s = input().split()
    mas.append(s)
new_mas = []
for i in range(m):
    new_mas.append([])
for j in range(m):
    for i in range(n - 1, -1, -1):
        new_mas[j].append(mas[i][j])
for j in range(m):
    print(' '.join(new_mas[j]))

f = open('input.txt', 'r')
alline = f.readlines()
for i in range(len(alline)):
    alline[i] = alline[i].rstrip('\n')
a = []
b = []
N = int(alline[0])
for i in range(N):
    a.append(alline[i+1].split(' '))
M = int(alline[N+1])
for i in range(N+1, len(alline) - 1, 1):
    b.append(alline[i+1].split(' '))
print(a)
print(b)
for i in range(len(b)):
    for j in range(len(a)):
        if a[j][0] == b[i][1]:
            for k in range(1, len(a[j]), 1):
                print(len(a[j]))
                if a[j][k].lower() == b[i][0].lower()[0]:
                    print('OK')
                    break
                if 'x' in b[i][0].lower():
                    if a[j][k].lower() == b[i][0].lower()[1]:
                        print('OK')
                        break
                if k == len(a[j]) - 1:
                    print('Access denied')

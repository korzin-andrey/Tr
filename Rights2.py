f = open('input.txt', 'r')
alline = f.readlines()
N = int(alline[0])
filelst = {}
for i in range(len(alline)):
    alline[i] = alline[i].rstrip('\n')
for i in range(1, N + 1, 1):
    name, *commands = alline[i].split(' ')
    filelst[name] = commands
access = {'read': 'R', 'write': 'W', 'execute': 'X'}
for i in range(N + 2, len(alline), 1):
    com, prog = alline[i].split(' ')
    if access[com] in filelst[prog]:
        print('OK')
    else:
        print('Access denied')

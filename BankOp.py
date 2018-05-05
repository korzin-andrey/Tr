def balance(name, a):
    if name in a:
        print(a[name])
    else:
        print('ERROR')
def deposit(name, money, a):
    if name not in a:
        a[name] = money
    else:
        a[name] += money
def withdraw(name, money, a):
    if name not in a:
        a[name] = - money
    else:
        a[name] -= money
def income(p, a):
    for x in a:
        if a[x] > 0:
            a[x] += int(a[x] * (p / 100))
def transfer(name1, name2, money, a):
    withdraw(name1, money, a)
    deposit(name2, money, a)
file = open('input.txt', 'r')
a = {}
for line in file.readlines():
    line = line.rstrip('\n')
    operation, *nasum = line.split(' ')
    if operation == 'DEPOSIT':
        deposit(nasum[0], int(nasum[1]), a)
    if operation == 'WITHDRAW':
        withdraw(nasum[0], int(nasum[1]), a)
    if operation == 'BALANCE':
        balance(nasum[0], a)
    if operation == 'TRANSFER':
        transfer(nasum[0], nasum[1], int(nasum[2]),  a)
    if operation == 'INCOME':
        income(int(nasum[0]), a)

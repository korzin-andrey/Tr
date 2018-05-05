def ip(s):
    try:
        s = list(map(int, s.split('.')))
    except:
        print('NO')
        return
    if len(s) != 4:
        print('NO')
        return
    else:
        for i in range(len(s)):
            if s[i] > 255 or s[i] < 0:
                print('NO')
                return
    print('YES')
    return       
s = input()
ip(s)
               


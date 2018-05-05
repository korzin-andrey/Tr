def createmas(k):
    m = []
    if k == 1:
        m = [0, 0]
    else:
       m.append(createmas(k - 1))
       m.append(createmas(k - 1))
    return(m)
k = int(input())
print(createmas(k))

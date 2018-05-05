def lag(N):
    N1 = int(N ** 0.5)
    for a in range(N1,-1,-1):
        if a ** 2 == N:
            print(a)
            return
        N2 = int((N - a ** 2) ** 0.5)
        for b in range(N2, -1, -1):
            if a ** 2 + b ** 2 == N:
                print(a, b, sep = ' ')
                return
            N3 = int((N - a ** 2 - b ** 2) ** 0.5)
            for c in range(N3, -1, -1):
                if a ** 2 + b ** 2 + c ** 2 == N:
                    print(a, b, c, sep = ' ')
                    return
                N4 = int((N - a ** 2 - b ** 2 - c ** 2) ** 0.5)
                for d in range(N4, -1, -1):
                    if a ** 2 + b ** 2 + c ** 2 + d ** 2 == N:
                        print(a, b, c, d, sep = ' ')
                        return
N = int(input())
lag(N)

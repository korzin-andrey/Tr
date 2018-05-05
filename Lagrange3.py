def lag(N):
    for i in range(4):
        N0 = int(N ** 0.5)
        N = N - N0 ** 2
        print(N0)
        if N == 0:
            return
    return
N = int(input())
lag(N)
        

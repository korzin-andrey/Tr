def lag(N, m):
    N0 = int(N ** 0.5)
    if N0 ** 2 == N:
        print(N0, ' ')
        return(N0 ** 2)
    sum = N0 ** 2
    if m + 1 <= 3:
        sum += lag(N-N0 ** 2, m+1)
        if sum == N:
            print(N0, ' ')
            return(sum)
    else:
        while N0 >= 0:
            sum = N0 ** 2    
            if sum == N:
                print(N0, ' ')
                return
        N0 -= 1
    return    
N = int(input())
lag(N, 0)

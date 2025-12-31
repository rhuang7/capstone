import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    Q = int(data[N+1])
    Ks = list(map(int, data[N+2:]))
    
    A.sort()
    
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]
    
    res = []
    for K in Ks:
        if K >= N:
            res.append(0)
            continue
        m = (N + K) // (K + 1)
        total = prefix[N] - prefix[m]
        res.append(total)
    
    for x in res:
        print(x)

if __name__ == '__main__':
    solve()
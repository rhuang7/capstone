import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    A = list(map(int, data[1:N+1]))
    Q = int(data[N+1])
    queries = list(map(int, data[N+2:]))
    
    A.sort()
    
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]
    
    result = []
    for K in queries:
        if K >= N:
            result.append(0)
            continue
        if K == 0:
            result.append(prefix[N])
            continue
        m = (N + K) // (K + 1)
        total = prefix[N] - prefix[m] + (m * (N - m))
        result.append(total)
    
    for res in result:
        print(res)

if __name__ == '__main__':
    solve()
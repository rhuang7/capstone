import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        res = []
        for i in range(N):
            min_val = float('inf')
            for j in range(N):
                val = A[j] + abs(i - j)
                if val < min_val:
                    min_val = val
            res.append(str(min_val))
        results.append(' '.join(res))
    print('\n'.join(results))
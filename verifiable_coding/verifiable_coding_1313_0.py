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
        if N == 0:
            results.append("-1")
            continue
        g = A[0]
        for num in A[1:]:
            g = math.gcd(g, num)
            if g == 1:
                break
        if g == 1:
            results.append("-1")
        else:
            results.append(str(g))
    print('\n'.join(results))
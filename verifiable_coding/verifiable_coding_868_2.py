import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        def is_beautiful(subarray):
            m = math.ceil(K / len(subarray))
            B = subarray * m
            B.sort()
            X = B[K-1]
            count_X = subarray.count(X)
            return str(count_X) in set(str(x) for x in subarray)
        
        count = 0
        for l in range(N):
            subarray = []
            for r in range(l, N):
                subarray.append(A[r])
                if len(subarray) >= K:
                    if is_beautiful(subarray):
                        count += 1
        results.append(str(count))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
import sys
import math
from collections import Counter

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
        
        count = 0
        
        for l in range(N):
            freq = Counter()
            unique = []
            for r in range(l, N):
                freq[A[r]] += 1
                unique.append(A[r])
                m = (K + len(unique) - 1) // len(unique)
                B = unique * m
                B.sort()
                X = B[K-1]
                F = freq[X]
                if str(F) in set(unique):
                    count += 1
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
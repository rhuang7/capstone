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
        
        count = 0
        
        for l in range(N):
            freq = defaultdict(int)
            unique = set()
            for r in range(l, N):
                freq[A[r]] += 1
                unique.add(A[r])
                len_sub = r - l + 1
                m = (K + len_sub - 1) // len_sub
                B = A[l:r+1] * m
                B.sort()
                X = B[K-1]
                F = freq[X]
                if F in unique:
                    count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
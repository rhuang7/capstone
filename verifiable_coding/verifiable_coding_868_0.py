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
            unique = []
            for r in range(l, N):
                freq[A[r]] += 1
                unique.append(A[r])
                len_s = r - l + 1
                m = math.ceil(K / len_s)
                B = unique * m
                B.sort()
                X = B[K-1]
                F = freq[X]
                if str(F) in unique:
                    count += 1
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
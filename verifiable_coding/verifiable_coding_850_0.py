import sys
import math
from collections import defaultdict

def solve():
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
        
        if N == 2:
            results.append(math.gcd(A[0], A[1]))
            continue
        
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1
        
        max_gcd = 0
        for num in freq:
            if freq[num] >= 2:
                current_gcd = num
                for i in range(num - 1, 0, -1):
                    if freq[i] >= 1:
                        current_gcd = i
                        break
                max_gcd = max(max_gcd, current_gcd)
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
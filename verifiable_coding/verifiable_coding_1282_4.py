import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx+1])
        idx += 2
        
        # Function to compute bitwise AND from L to i
        def and_val(i):
            res = L
            for j in range(L, i+1):
                res &= j
            return res
        
        # Compute sum from L to R
        total = 0
        for i in range(L, R+1):
            total += and_val(i)
            total %= MOD
        
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
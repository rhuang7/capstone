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
        N = int(data[idx])
        W = int(data[idx+1])
        idx += 2
        
        if N == 2:
            # For two-digit numbers, weight is D2 - D1 = W
            # D1 can be 1-9, D2 can be D1 + W
            # D2 must be between 0-9
            count = 0
            for d1 in range(1, 10):
                d2 = d1 + W
                if 0 <= d2 <= 9:
                    count += 1
            results.append(count % MOD)
        else:
            # For N > 2, the weight is sum_{i=2}^N (D_i - D_{i-1}) = D_N - D_1
            # So the weight is simply the difference between the last and first digit
            # So W must be between -9 and 9, but the problem says |W| <= 300, so we need to check if W is in this range
            if abs(W) > 9:
                results.append(0)
            else:
                # D1 can be 1-9, D_N can be D1 + W
                # D_N must be between 0-9
                count = 0
                for d1 in range(1, 10):
                    dN = d1 + W
                    if 0 <= dN <= 9:
                        count += 1
                results.append(count % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
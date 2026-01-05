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
            # D1 ranges from 1 to 9, D2 ranges from 0 to 9
            # So D2 = D1 + W
            # D2 must be between 0 and 9
            count = 0
            for d1 in range(1, 10):
                d2 = d1 + W
                if 0 <= d2 <= 9:
                    count += 1
            results.append(count % MOD)
        else:
            # For N >= 3, the weight is sum_{i=2}^N (D_i - D_{i-1}) = D_N - D_1
            # Because it's a telescoping sum: (D2 - D1) + (D3 - D2) + ... + (DN - D_{N-1}) = DN - D1
            # So weight W = D_N - D_1
            # D1 is from 1 to 9, D_N is from 0 to 9
            # So D_N = D_1 + W
            # D_N must be between 0 and 9
            count = 0
            for d1 in range(1, 10):
                d_n = d1 + W
                if 0 <= d_n <= 9:
                    count += 1
            results.append(count % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
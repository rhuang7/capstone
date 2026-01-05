import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        W = int(data[index+1])
        index += 2
        
        if N == 2:
            # For two digits, weight is D2 - D1 = W
            # D1 ranges from 1 to 9, D2 ranges from 0 to 9
            # D2 = D1 + W
            # D2 must be between 0 and 9
            count = 0
            for d1 in range(1, 10):
                d2 = d1 + W
                if 0 <= d2 <= 9:
                    count += 1
            results.append(count % MOD)
        else:
            # For N > 2, the weight is sum_{i=2}^N (D_i - D_{i-1}) = D_N - D_1
            # Because it's a telescoping sum
            # So weight W = D_N - D_1
            # D_1 is between 1 and 9
            # D_N is between 0 and 9
            # So W must be between -9 and 9
            # But the problem says |W| <= 300, so for N > 2, W must be between -9 and 9
            if abs(W) > 9:
                results.append(0)
            else:
                # D_1 ranges from 1 to 9
                # D_N = D_1 + W
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
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
            # For two digits, weight is D2 - D1 = W
            # D1 can be from 1 to 9, D2 can be from 0 to 9
            # D2 = D1 + W
            # D2 must be between 0 and 9
            count = 0
            for d1 in range(1, 10):
                d2 = d1 + W
                if 0 <= d2 <= 9:
                    count += 1
            results.append(count % MOD)
        else:
            # For N >= 3, we need to find the number of N-digit numbers with weight W
            # The weight is sum_{i=2}^N (D_i - D_{i-1}) = D_N - D_1
            # So W = D_N - D_1
            # D_1 is from 1 to 9, D_N is from 0 to 9
            # So W must be between -9 and 9
            # If W is outside this range, answer is 0
            if abs(W) > 9:
                results.append(0)
                continue
            
            # For N >= 3, the weight is D_N - D_1
            # So for each possible D1 (1-9) and D_N (0-9) such that D_N - D1 = W,
            # the number of valid sequences is 10^(N-2)
            # Because the digits in between can be anything
            count = 0
            for d1 in range(1, 10):
                d_n = d1 + W
                if 0 <= d_n <= 9:
                    count += 10**(N-2)
            results.append(count % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
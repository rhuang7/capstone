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
            # D1 can be 1-9, D2 can be D1 + W
            # D2 must be between 0-9
            count = 0
            for d1 in range(1, 10):
                d2 = d1 + W
                if 0 <= d2 <= 9:
                    count += 1
            results.append(count % MOD)
        else:
            # For N >= 3, the weight is sum_{i=2}^N (D_i - D_{i-1}) = D_N - D_1
            # Because sum_{i=2}^N (D_i - D_{i-1}) = D_N - D_1
            # So the weight is D_N - D_1 = W
            # So D_N = D_1 + W
            # D_1 is 1-9, D_N is 0-9
            # So D_1 + W must be between 0-9
            count = 0
            for d1 in range(1, 10):
                d_n = d1 + W
                if 0 <= d_n <= 9:
                    count += 1
            results.append(count % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        # The minimum sum of K distinct positive integers is 1 + 2 + ... + K = K*(K+1)//2
        min_sum = K * (K + 1) // 2
        if min_sum > N:
            print(-1)
            continue
        
        # The maximum possible gcd is the largest divisor of N that is <= N/K
        max_gcd = 0
        # We try all possible divisors of N up to sqrt(N)
        for i in range(1, int(math.isqrt(N)) + 1):
            if N % i == 0:
                # Check if i can be the gcd
                if i * K <= N:
                    max_gcd = max(max_gcd, i)
                # Check the corresponding co-divisor
                j = N // i
                if j * K <= N:
                    max_gcd = max(max_gcd, j)
        
        print(max_gcd)

if __name__ == '__main__':
    solve()
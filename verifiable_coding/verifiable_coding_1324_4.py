import sys
import math

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index+1])
        index += 2
        
        # The minimum sum of K distinct positive integers is 1 + 2 + ... + K = K*(K+1)//2
        min_sum = K * (K + 1) // 2
        if min_sum > N:
            print(-1)
            continue
        
        # The maximum possible gcd is the largest divisor of N that is <= N//K
        max_gcd = 0
        for i in range(1, int(math.isqrt(N)) + 1):
            if N % i == 0:
                if i <= N // K:
                    max_gcd = i
                if (N // i) <= N // K:
                    max_gcd = max(max_gcd, N // i)
        
        print(max_gcd)

if __name__ == '__main__':
    solve()
import sys
import math

def solve():
    import sys
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
        
        # The maximum possible gcd is the maximum d such that d * K <= N and d * (K*(K+1)//2) <= N
        # So we need to find the maximum d such that d * (K*(K+1)//2) <= N
        max_gcd = N // (K * (K + 1) // 2)
        
        # Check if there exists a multiple of max_gcd that can be used to distribute the bananas
        # We need to find the maximum d such that d * (K*(K+1)//2) <= N and d is a divisor of N
        # So we check all divisors of N up to max_gcd
        # To find the maximum possible gcd, we check all divisors of N up to max_gcd
        # We can find all divisors of N and check which is the maximum that satisfies the condition
        
        # Find all divisors of N up to max_gcd
        divisors = set()
        for i in range(1, int(math.isqrt(N)) + 1):
            if N % i == 0:
                if i <= max_gcd:
                    divisors.add(i)
                if (N // i) <= max_gcd:
                    divisors.add(N // i)
        
        # Check if any divisor of N can be used
        max_gcd = -1
        for d in divisors:
            if d * (K * (K + 1) // 2) <= N:
                max_gcd = d
                break
        
        print(max_gcd)

if __name__ == '__main__':
    solve()
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
        K = int(data[index + 1])
        index += 2
        
        # The minimum sum of K distinct positive integers is 1 + 2 + ... + K = K*(K+1)//2
        min_sum = K * (K + 1) // 2
        
        if min_sum > N:
            print(-1)
            continue
        
        # The maximum possible gcd is the largest divisor of N that is <= N//K
        max_gcd = 0
        # The maximum possible value for gcd is N // K
        max_possible_gcd = N // K
        
        # Check all possible divisors of N up to max_possible_gcd
        for i in range(min(max_possible_gcd, int(math.isqrt(N)) + 1), 0, -1):
            if N % i == 0:
                # Check if it's possible to have K distinct numbers with gcd i
                # The sum of K distinct numbers with gcd i is i*(1 + 2 + ... + K) = i*K*(K+1)//2
                required_sum = i * K * (K + 1) // 2
                if required_sum <= N:
                    max_gcd = i
                    break
        
        print(max_gcd)

if __name__ == '__main__':
    solve()
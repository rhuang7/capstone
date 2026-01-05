import sys
import math
from math import gcd
from functools import reduce

def compute_gcd(list_numbers):
    return reduce(math.gcd, list_numbers)

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        S = data[idx]
        idx += 1
        M, X, Y = map(int, data[idx:idx+3])
        idx += 3
        
        # Precompute all possible numbers with up to M digits
        possible_numbers = set()
        for i in range(1, N+1):
            for j in range(i, N+1):
                if j - i + 1 > M:
                    break
                num = int(S[i-1:j])
                possible_numbers.add(num)
        
        max_gcd = 0
        # Try all possible divisors from high to low
        for d in range(1000000, 0, -1):
            # Check if d is a divisor of any number in possible_numbers
            valid_numbers = []
            for num in possible_numbers:
                if num % d == 0:
                    valid_numbers.append(num)
            if not valid_numbers:
                continue
            
            # Check if we can split the string into parts with all numbers divisible by d
            # and use at least X and at most Y separators
            # We need to split the string into parts where each part is a number divisible by d
            # and the number of parts is between (Y+1) and (N - X)
            # We can use dynamic programming to check if it's possible
            # We'll use a DP array where dp[i] is True if the first i characters can be split
            dp = [False] * (N + 1)
            dp[0] = True
            for i in range(N + 1):
                if not dp[i]:
                    continue
                for j in range(i + 1, min(i + M + 1, N + 1)):
                    if dp[i] and (int(S[i:j]) % d == 0):
                        dp[j] = True
            if not dp[N]:
                continue
            
            # Now check if we can split into at least (Y+1) parts and at most (N - X) parts
            # The number of parts is between (Y+1) and (N - X)
            # We need to find the minimum number of parts
            min_parts = 0
            for i in range(N, 0, -1):
                if dp[i]:
                    min_parts = i
                    break
            if min_parts < (Y + 1) or min_parts > (N - X):
                continue
            
            # If we can split into at least X and at most Y separators
            # Then d is a candidate for maximum GCD
            max_gcd = d
            break
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
import sys
import math
from math import gcd
from functools import reduce

def compute_gcd(list_numbers):
    return reduce(gcd, list_numbers)

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
        possible_numbers = []
        for i in range(1, M+1):
            for j in range(N - i + 1):
                num_str = S[j:j+i]
                if len(num_str) > 0:
                    possible_numbers.append(int(num_str))
        
        max_gcd = 0
        # Try all possible divisors (from 1 to max possible number)
        max_possible = max(possible_numbers) if possible_numbers else 0
        for d in range(1, max_possible + 1):
            # Check if all numbers in the partition are divisible by d
            # We need to find a way to split S into at least X+1 and at most Y+1 parts
            # with each part having at most M digits
            # We can use dynamic programming to check if it's possible to split S into parts
            # with each part having at most M digits and divisible by d
            # We'll use a DP array where dp[i] is True if the first i characters can be split
            dp = [False] * (N + 1)
            dp[0] = True
            for i in range(N + 1):
                if dp[i]:
                    for j in range(i + 1, min(i + M + 1, N + 1)):
                        if j - i <= M:
                            num_str = S[i:j]
                            if len(num_str) > 0:
                                num = int(num_str)
                                if num % d == 0:
                                    dp[j] = True
            # Check if we can split into at least X+1 and at most Y+1 parts
            if dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (dp[N] and (
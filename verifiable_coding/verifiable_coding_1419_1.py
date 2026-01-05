import sys
import math
from math import gcd
from functools import reduce

def compute_gcd_list(lst):
    return reduce(gcd, lst)

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
        for i in range(N):
            num = 0
            for j in range(i, N):
                num = num * 10 + int(S[j])
                if j - i + 1 > M:
                    break
                possible_numbers.append(num)
        
        # Try all possible GCD candidates
        max_gcd = 0
        for candidate in set(possible_numbers):
            # Check if we can split the string into parts with this candidate as GCD
            # We need to split the string into parts that are multiples of candidate
            # And use between X and Y separators
            # We can use a dynamic programming approach to check if it's possible
            # To optimize, we can precompute the positions where the number is divisible by candidate
            positions = []
            for i in range(N):
                num = 0
                for j in range(i, N):
                    num = num * 10 + int(S[j])
                    if j - i + 1 > M:
                        break
                    if num % candidate == 0:
                        positions.append(j)
            
            # Now check if we can split the string into parts with at least X and at most Y separators
            # We can use dynamic programming to find the minimum number of separators
            dp = [float('inf')] * (N + 1)
            dp[0] = 0
            for i in range(N):
                if dp[i] == float('inf'):
                    continue
                for j in range(i + 1, N + 1):
                    if j - i > M:
                        break
                    if (int(S[i:j]) % candidate) == 0:
                        dp[j] = min(dp[j], dp[i] + 1)
            
            # Check if we can split with between X and Y separators
            if dp[N] != float('inf') and X <= dp[N] <= Y:
                max_gcd = max(max_gcd, candidate)
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
import sys
import math
from math import gcd
from functools import reduce

def compute_gcd_list(numbers):
    return reduce(math.gcd, numbers)

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
            # We need to split into at least X+1 parts (since X separators)
            # And at most Y+1 parts (since Y separators)
            # Also, all parts must be divisible by candidate
            # And each part must have at most M digits
            # We need to find if there's a way to split the string into parts with this candidate as GCD
            # We can use dynamic programming to check if it's possible
            # dp[i] = True if we can split the first i characters into parts with this candidate as GCD
            dp = [False] * (N + 1)
            dp[0] = True
            for i in range(N + 1):
                if not dp[i]:
                    continue
                for j in range(i + 1, min(i + M + 1, N + 1)):
                    num = 0
                    for k in range(i, j):
                        num = num * 10 + int(S[k])
                        if num % candidate != 0:
                            break
                    else:
                        if dp[j]:
                            continue
                        if j - i <= M:
                            dp[j] = True
            # Check if we can split into at least X+1 parts and at most Y+1 parts
            for i in range(N + 1):
                if dp[i] and i >= X + 1 and i <= Y + 1:
                    max_gcd = max(max_gcd, candidate)
                    break
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
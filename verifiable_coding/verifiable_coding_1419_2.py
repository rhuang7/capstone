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
                num = int(num_str)
                possible_numbers.append(num)
        
        # Try all possible GCD candidates
        max_gcd = 0
        for candidate in set(possible_numbers):
            # Check if we can split the string into parts with this GCD
            # We need to split the string into at least X and at most Y separators
            # So we need at least X+1 and at most Y+1 parts
            # Each part must have at most M digits
            # We can use dynamic programming to check if it's possible
            # dp[i][k] = True if we can split first i digits into k parts
            dp = [False] * (N + 1)
            dp[0] = True
            for i in range(1, N + 1):
                for j in range(i):
                    if dp[j] and len(S[j:i]) <= M:
                        num = int(S[j:i])
                        if num % candidate == 0:
                            dp[i] = True
                            break
            if any(dp[i] for i in range(X+1, Y+2)):
                # Check if the GCD of all parts is exactly candidate
                # We need to find a way to split the string into parts with this GCD
                # We can try to find a valid split
                # Use dynamic programming to find the GCD of all parts
                # dp[i] = GCD of first i digits
                dp_gcd = [0] * (N + 1)
                dp_gcd[0] = 0
                for i in range(1, N + 1):
                    for j in range(i):
                        if len(S[j:i]) <= M:
                            num = int(S[j:i])
                            if num % candidate == 0:
                                current_gcd = compute_gcd([num, dp_gcd[j]])
                                dp_gcd[i] = current_gcd
                                break
                if dp_gcd[N] == candidate:
                    max_gcd = max(max_gcd, candidate)
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
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
        for i in range(1, M+1):
            for j in range(N - i + 1):
                num = int(S[j:j+i])
                possible_numbers.append(num)
        
        # Try all possible GCD candidates
        max_gcd = 0
        for candidate in possible_numbers:
            if candidate == 0:
                continue
            # Check if we can split the string into parts with this GCD
            # We need to split into at least X and at most Y separators
            # So we need at least X+1 and at most Y+1 parts
            # We need to split the string into parts where each part is divisible by candidate
            # And the number of parts is between X+1 and Y+1
            # Also, each part must have at most M digits
            # We can use dynamic programming to check if it's possible
            # dp[i] = True if we can split the first i digits into valid parts
            dp = [False] * (N + 1)
            dp[0] = True
            for i in range(1, N + 1):
                for j in range(i):
                    if dp[j] and j + 1 <= i and i - j <= M:
                        num = int(S[j:i])
                        if num % candidate == 0:
                            dp[i] = True
                            break
            if dp[N]:
                # Check if the number of parts is between X+1 and Y+1
                # We can count the number of splits by counting the number of True in dp
                # But we need to find if there's a way to split into at least X+1 and at most Y+1 parts
                # We can use a different DP to count the number of parts
                count_dp = [0] * (N + 1)
                count_dp[0] = 1
                for i in range(1, N + 1):
                    for j in range(i):
                        if dp[j] and j + 1 <= i and i - j <= M:
                            num = int(S[j:i])
                            if num % candidate == 0:
                                count_dp[i] += count_dp[j]
                # Check if there's at least one way to split into between X+1 and Y+1 parts
                if any(count_dp[i] > 0 for i in range(X+1, Y+2)):
                    max_gcd = max(max_gcd, candidate)
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
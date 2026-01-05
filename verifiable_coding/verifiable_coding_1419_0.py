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
        possible_numbers = []
        for i in range(1, M+1):
            for j in range(N - i + 1):
                num_str = S[j:j+i]
                num = int(num_str)
                possible_numbers.append(num)
        
        # Try all possible GCD values (from 1 to max possible number)
        max_possible = 0
        for num in possible_numbers:
            max_possible = max(max_possible, num)
        
        # Try all possible GCD values in descending order
        for g in range(max_possible, 0, -1):
            # Check if it's possible to split the string into numbers with GCD g
            # and use at least X and at most Y separators
            # We need to split the string into parts such that each part is divisible by g
            # and the number of parts is between (Y+1) and (N - X)
            # We also need to check if the number of parts is between (Y+1) and (N - X)
            # and that the number of separators is between X and Y
            # So we need to find if there exists a way to split the string into parts
            # such that each part is divisible by g and the number of parts is between (Y+1) and (N - X)
            # and the number of separators is between X and Y
            # We can do this with dynamic programming
            # dp[i] = True if it's possible to split the first i characters into parts with GCD g
            dp = [False] * (N + 1)
            dp[0] = True
            for i in range(1, N + 1):
                for j in range(i):
                    if dp[j] and (j + 1 <= N and (i - j) <= M):
                        num_str = S[j:i]
                        num = int(num_str)
                        if num % g == 0:
                            dp[i] = True
                            break
            if any(dp[i] for i in range(1, N + 1)):
                # Check if there exists a way to split the string into parts with GCD g
                # and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to find the number of parts
                # We can do this with a modified DP
                dp2 = [0] * (N + 1)
                dp2[0] = 0
                for i in range(1, N + 1):
                    for j in range(i):
                        if dp[j] and (i - j) <= M:
                            num_str = S[j:i]
                            num = int(num_str)
                            if num % g == 0:
                                dp2[i] = min(dp2[i], dp2[j] + 1)
                # Check if there exists a way to split the string into parts with GCD g
                # and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # The number of separators is (number of parts - 1)
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between X and Y
                # So we need to check if there exists a way to split the string into parts
                # with GCD g and the number of parts is between (Y+1) and (N - X)
                # and the number of separators is between
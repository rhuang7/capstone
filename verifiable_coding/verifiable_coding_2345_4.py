import sys
import math
from collections import defaultdict

MOD = 998244353

def solve():
    input = sys.stdin.buffer.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx + n]))
        idx += n
        
        # Convert each number to a string to handle leading zeros
        s = [str(x) for x in a]
        
        # Compute the hash of each string
        hash_val = [0] * n
        for i in range(n):
            hash_val[i] = hash(s[i])
        
        # Compute the total number of permutations
        total = math.factorial(n)
        
        # Compute the number of valid permutations
        # We use dynamic programming to count valid permutations
        # dp[i][j] = number of ways to arrange first i cards such that the number mod 11 is j
        dp = [[0] * 11 for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(11):
                if dp[i - 1][j] == 0:
                    continue
                # Get the hash of the i-th card
                current_hash = hash_val[i - 1]
                # Compute the contribution of this card to the mod 11 value
                # We need to compute the value of the current card as a number and then mod 11
                # But since the card is a string, we can compute its value mod 11
                # We can do this by iterating through the digits of the string
                val = 0
                for c in s[i - 1]:
                    val = (val * 10 + int(c)) % 11
                # Update the dp table
                for k in range(11):
                    new_mod = (j * 10 + val) % 11
                    dp[i][new_mod] = (dp[i][new_mod] + dp[i - 1][k]) % MOD
        
        # The answer is the number of ways to arrange all cards such that the number mod 11 is 0
        results.append(dp[n][0] % MOD)
    
    for res in results:
        print(res)
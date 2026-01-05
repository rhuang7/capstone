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
        a = list(map(int, input[idx:idx+n]))
        idx += n
        
        # Precompute factorials modulo MOD
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Map numbers to their counts
        num_counts = defaultdict(int)
        for num in a:
            num_counts[num] += 1
        
        # Compute the hash of the number as a string
        def get_hash(num):
            return int(str(num))
        
        # Compute the hash of the entire number formed by the cards
        def get_total_hash(cards):
            s = ""
            for card in cards:
                s += str(card)
            return int(s)
        
        # Use dynamic programming to count valid permutations
        # dp[i][h] = number of ways to arrange i cards with hash h
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(n):
            for h in dp[i]:
                count = dp[i][h]
                for num in num_counts:
                    if num_counts[num] > 0:
                        new_h = (h * 10 + get_hash(num)) % 11
                        dp[i + 1][new_h] = (dp[i + 1][new_h] + count * num_counts[num]) % MOD
                        num_counts[num] -= 1
        
        # The answer is the number of ways to arrange all cards with hash 0
        results.append(dp[n][0] % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
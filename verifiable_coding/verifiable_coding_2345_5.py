import sys
import math
from collections import defaultdict

MOD = 998244353

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Precompute factorials modulo MOD
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Convert numbers to strings for easy concatenation
        s_list = [str(x) for x in a]
        
        # Compute the hash of the concatenated number modulo 11
        # Since 10^k mod 11 alternates between 1 and -1, we can compute the hash as:
        # sum( (digit * 10^k) mod 11 for k in range(len(s)) )
        # But since we are dealing with concatenated numbers, we can compute the hash as:
        # hash = 0
        # for s in s_list:
        #     hash = (hash * 10 + int(s)) % 11
        # However, since we need to consider all permutations, we need to compute the hash for all permutations
        # But this is not feasible directly, so we use dynamic programming with memoization
        
        # We use dynamic programming with memoization to count the number of permutations that result in a number divisible by 11
        # dp[i][j] = number of ways to arrange the first i cards such that the hash is j mod 11
        # We also need to track the count of each number to avoid overcounting permutations of the same number
        
        # Count the frequency of each number
        freq = defaultdict(int)
        for num in a:
            freq[num] += 1
        
        # Precompute the hash of each number mod 11
        hash_val = [0] * len(a)
        for i in range(len(a)):
            hash_val[i] = (hash_val[i - 1] * 10 + int(str(a[i]))) % 11
        
        # Now we use dynamic programming
        dp = [ [0] * 11 for _ in range(n + 1) ]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(11):
                if dp[i - 1][j] == 0:
                    continue
                for num in freq:
                    if freq[num] == 0:
                        continue
                    # Compute the hash contribution of this number
                    current_hash = (j * 10 + int(str(num))) % 11
                    # Multiply by the number of ways to choose this number
                    count = freq[num]
                    dp[i][current_hash] = (dp[i][current_hash] + dp[i - 1][j] * count) % MOD
                    freq[num] -= 1
        
        results.append(dp[n][0] % MOD)
    
    for res in results:
        print(res)
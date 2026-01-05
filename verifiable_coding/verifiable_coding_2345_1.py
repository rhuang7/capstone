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
        
        # Precompute factorials modulo MOD
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Map each number to its count
        num_counts = defaultdict(int)
        for num in a:
            num_counts[num] += 1
        
        # Compute the hash of each number as a string
        num_hashes = [str(num) for num in a]
        
        # Memoization for DP
        memo = {}
        
        def dp(i, mod):
            if i == n:
                return 1 if mod % 11 == 0 else 0
            key = (i, mod)
            if key in memo:
                return memo[key]
            
            total = 0
            for j in range(i, n):
                # Swap i and j
                num_i = num_hashes[i]
                num_j = num_hashes[j]
                # Compute the new mod value
                # The current mod is mod, and we are adding the number formed by num_j followed by num_i
                # The new mod is (mod * 10^len(num_i) + int(num_j)) % 11
                # But since we are moving from i to j, we need to compute the contribution of num_i and num_j
                # The new mod is (mod * 10^len(num_j) + int(num_i)) % 11
                len_j = len(num_j)
                len_i = len(num_i)
                new_mod = (mod * pow(10, len_j, 11) + int(num_i)) % 11
                # Recursively compute the number of ways for the rest
                total += dp(j + 1, new_mod)
                total %= MOD
            
            memo[key] = total
            return total
        
        # Initial call: start from index 0, mod 0
        result = dp(0, 0)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
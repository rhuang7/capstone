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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Precompute factorials modulo MOD
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Map numbers to their counts
        num_counts = defaultdict(int)
        for num in a:
            num_counts[num] += 1
        
        # Generate all unique numbers
        unique_nums = list(num_counts.keys())
        m = len(unique_nums)
        
        # DP table: dp[i][j] = number of ways to arrange first i unique numbers to get a remainder j mod 11
        dp = [[0] * 11 for _ in range(m + 1)]
        dp[0][0] = 1
        
        for i in range(1, m + 1):
            num = unique_nums[i - 1]
            count = num_counts[num]
            for j in range(11):
                if dp[i - 1][j] == 0:
                    continue
                # Compute the number formed by the current number
                num_str = str(num)
                num_len = len(num_str)
                # Compute the value of the number mod 11
                num_mod = 0
                for c in num_str:
                    num_mod = (num_mod * 10 + int(c)) % 11
                # Update dp[i][j + num_mod * (10 ** (num_len * (m - i))) % 11]
                # But we can't compute this directly, so we need to compute the contribution of adding this number
                # We'll use the fact that the contribution of this number is num_mod * (10 ** (num_len * (m - i))) % 11
                # However, since we don't know the exact position, we'll use the fact that the number is added at the end
                # So the contribution is num_mod * (10 ** (num_len * (m - i))) % 11
                # But since we don't know the exact exponent, we'll compute it as (10 ** (num_len * (m - i))) % 11
                # However, since we are working mod 11, we can compute it as pow(10, num_len * (m - i), 11)
                # But since m - i can be large, we need to compute this efficiently
                # We'll precompute powers of 10 mod 11
                pow10 = pow(10, num_len * (m - i), 11)
                for k in range(11):
                    if dp[i - 1][k] == 0:
                        continue
                    new_remainder = (k + num_mod * pow10) % 11
                    dp[i][new_remainder] = (dp[i][new_remainder] + dp[i - 1][k] * math.comb(count, 1)) % MOD
        
        # The answer is dp[m][0]
        results.append(dp[m][0] % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
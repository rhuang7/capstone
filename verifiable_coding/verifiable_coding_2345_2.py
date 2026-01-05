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
        
        # Generate all unique numbers
        unique_nums = list(num_counts.keys())
        m = len(unique_nums)
        
        # Precompute the hash of each number as a string
        num_hashes = [str(num) for num in unique_nums]
        
        # Use dynamic programming to count the number of valid permutations
        # dp[i][j] = number of ways to arrange the first i numbers to form a number with remainder j mod 11
        dp = [[0] * 11 for _ in range(m + 1)]
        dp[0][0] = 1
        
        for i in range(1, m + 1):
            num = unique_nums[i - 1]
            cnt = num_counts[num]
            hash_val = num_hashes[i - 1]
            hash_len = len(hash_val)
            
            # For each possible remainder j
            for j in range(11):
                if dp[i - 1][j] == 0:
                    continue
                
                # Compute the contribution of this number to the remainder
                # The number is added to the end, so the new remainder is (old_remainder * 10^len + num) % 11
                pow10 = pow(10, hash_len, 11)
                new_remainder = (j * pow10 + num) % 11
                
                # Multiply by the number of ways to choose the positions of this number
                # (cnt choose k) * k! where k is the number of times this number is used
                # Since we are using all occurrences of this number, it's cnt! / (cnt - cnt)! = cnt!
                # But we need to multiply by the number of ways to arrange the previous numbers
                # So we multiply by cnt! and add to dp[i][new_remainder]
                dp[i][new_remainder] = (dp[i][new_remainder] + dp[i - 1][j] * fact[cnt]) % MOD
        
        # The answer is the number of ways to arrange all numbers with remainder 0 mod 11
        results.append(dp[m][0] % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
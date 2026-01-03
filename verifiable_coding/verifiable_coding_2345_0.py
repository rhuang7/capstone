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
        
        # Convert each number to a string to handle leading zeros
        s = [str(x) for x in a]
        
        # Precompute the hash of each string
        hash_map = defaultdict(int)
        for num in s:
            hash_map[num] += 1
        
        # Precompute the factorial for modulo purposes
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Function to compute the hash of a number as a string
        def get_hash(num_str):
            h = 0
            for c in num_str:
                h = (h * 10 + int(c)) % MOD
            return h
        
        # Compute the total hash of all numbers
        total_hash = 0
        for num in s:
            total_hash = (total_hash * 10 + int(num)) % MOD
        
        # If total_hash is 0, then the number is divisible by 11
        if total_hash % 11 == 0:
            results.append(fact[n])
            continue
        
        # Use dynamic programming to count valid permutations
        dp = [0] * 11
        dp[0] = 1
        
        for num in s:
            new_dp = [0] * 11
            num_hash = get_hash(num)
            for rem in range(11):
                if dp[rem] == 0:
                    continue
                # Add the current number at the end
                new_rem = (rem * 10 + num_hash) % 11
                new_dp[new_rem] = (new_dp[new_rem] + dp[rem]) % MOD
                # Add the current number at the beginning
                new_rem = (num_hash * 10 + rem) % 11
                new_dp[new_rem] = (new_dp[new_rem] + dp[rem]) % MOD
            dp = new_dp
        
        results.append(dp[0] % MOD)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
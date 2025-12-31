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
        
        # Convert numbers to strings
        s = [str(x) for x in a]
        
        # Compute the number formed by concatenating the cards
        # We need to find the number mod 11
        # But since the number is very large, we can compute it mod 11
        # Using the property that a number mod 11 is equal to the alternating sum of its digits mod 11
        # But since the number is formed by concatenating strings, we can compute the mod 11 value
        # by processing each string and updating the mod value
        
        # Compute the mod 11 value of the entire number
        mod_11 = 0
        for num_str in s:
            num = int(num_str)
            mod_11 = (mod_11 * 10 + num) % 11
        
        # Now, we need to count the number of permutations of the cards such that the mod 11 of the concatenated number is 0
        # We can use dynamic programming with memoization
        
        # Memoization table: dp[i][j] = number of ways to arrange the first i cards such that the mod 11 is j
        # We also need to track the count of each number to avoid overcounting
        # Since the numbers are unique, but can have the same value, we need to count the permutations considering duplicates
        
        # First, count the frequency of each number
        freq = defaultdict(int)
        for num in a:
            freq[num] += 1
        
        # Now, we need to generate all unique permutations of the numbers, considering duplicates
        # But since n can be up to 2000, we need a more efficient approach
        
        # We can use dynamic programming with memoization
        # dp[i][j] = number of ways to arrange the first i numbers such that the mod 11 is j
        # We also need to track the count of each number
        
        # To handle the counts, we can use memoization with the current counts of each number
        
        # But since the numbers can be up to 1e9, we cannot use a simple memoization table
        # So we need to use memoization with the current counts of each number
        
        # We can use memoization with a tuple of the current counts of each number
        # But since the numbers can be up to 1e9, we need to map them to a unique identifier
        
        # So, we first map the numbers to unique identifiers
        unique_numbers = list(freq.keys())
        unique_numbers.sort()
        num_to_id = {num: i for i, num in enumerate(unique_numbers)}
        id_to_num = {i: num for i, num in enumerate(unique_numbers)}
        
        # Now, we can use memoization with the current counts of each number
        # We can use a memoization dictionary that maps a tuple of counts to the number of ways to arrange the numbers
        
        # We also need to track the current mod 11 value
        
        # So, the memoization key is (current_counts, mod_11)
        # But since the counts can be large, we need to use a tuple of counts for each number
        
        # We can use a memoization dictionary with the current counts and mod_11
        
        # We can also use a memoization function with lru_cache, but since the numbers can be up to 1e9, we need to use a unique identifier for each number
        
        # So, we can proceed with the following approach:
        
        # Use memoization with the current counts of each number and the current mod 11 value
        
        # The initial state is: all counts are zero, mod_11 is 0
        
        # We can use a recursive function with memoization
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dp(counts, mod_11):
            # counts is a tuple of the current counts of each number
            # mod_11 is the current mod 11 value
            # We need to return the number of ways to arrange the remaining numbers such that the final mod 11 is 0
            
            # If all counts are zero, we have a valid arrangement
            if all(c == 0 for c in counts):
                return 1 if mod_11 == 0 else 0
            
            total = 0
            for i in range(len(unique_numbers)):
                if counts[i] == 0:
                    continue
                # Take one occurrence of this number
                new_counts = list(counts)
                new_counts[i] -= 1
                new_counts = tuple(new_counts)
                
                # Compute the mod_11 contribution of this number
                num = id_to_num[i]
                num_val = int(str(num))
                new_mod = (mod_11 * 10 + num_val) % 11
                
                # Recursively compute the number of ways
                total += dp(new_counts, new_mod)
                total %= MOD
            
            return total
        
        # Initialize the counts with the frequencies of each number
        initial_counts = tuple([freq[num] for num in unique_numbers])
        
        # Compute the answer
        answer = dp(initial_counts, 0)
        
        results.append(answer)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
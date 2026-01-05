import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        L = int(data[idx])
        R = int(data[idx+1])
        idx += 2
        
        # Precompute powers of 2 up to 60 (since 2^60 is larger than 1e18)
        pow2 = [1] * 61
        for i in range(1, 61):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        # Function to compute the bitwise AND from L to i
        def and_val(i):
            res = L
            for j in range(L, i+1):
                res &= j
            return res
        
        # Precompute the AND values for all i from L to R
        # But since L and R can be up to 1e18, we need a smarter approach
        # Instead, we use the fact that the AND of a range of numbers
        # will eventually become 0 once a 0 bit is encountered
        
        # The AND of L to i will be the same as the AND of L to i-1 AND i
        # So we can compute it iteratively
        
        # We need to find the sum of AND from L to i for i from L to R
        # Let's compute this efficiently
        
        # The AND of L to i will eventually become 0 once a number with a 0 bit
        # in the same position as L has been included
        
        # We can find the position where the AND becomes 0
        # and compute the sum accordingly
        
        # Let's compute the AND from L to i for each i from L to R
        # and accumulate the sum
        
        sum_s = 0
        current_and = L
        for i in range(L, R+1):
            current_and &= i
            sum_s = (sum_s + current_and) % MOD
        
        results.append(sum_s)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
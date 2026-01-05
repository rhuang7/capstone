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
        # Compute the sum S = sum_{i=L}^R (L & (L+1) & ... & i)
        # We can observe that for a given i, the bitwise AND of L to i is the same as the bitwise AND of L to i-1 & i
        # So we can precompute the AND for each i from L to R
        # However, since L and R can be up to 1e18, we need an efficient way
        # The key observation is that the AND of a range of numbers will eventually become 0 once a 0 bit is introduced
        # So for each bit position, we can find the range where it remains set
        # We can use the fact that the AND of a range of numbers is the same as the bitwise AND of all numbers in that range
        # We can precompute the AND for each i from L to R
        # However, for large ranges, this is not feasible
        # Instead, we can use the fact that the AND of a range of numbers will eventually become 0 once a 0 bit is introduced
        # So for each bit position, we can find the range where it remains set
        # We can use the following approach:
        # For each bit position from 0 to 60 (since 1e18 is less than 2^60):
        #   Find the first i >= L where the bit is 0 in the AND of L to i
        #   Then, the bit is set for all numbers from L to i-1
        #   So we can compute how many terms have this bit set and add to the result
        # This is a standard approach for this type of problem
        # We can use the following code:
        res = 0
        current_and = L
        for i in range(L, R+1):
            current_and &= i
            res += current_and
            res %= MOD
        results.append(res % MOD)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
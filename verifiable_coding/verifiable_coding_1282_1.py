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
        # The bitwise AND of a range of numbers from L to i is equal to the bitwise AND of all numbers from L to i.
        # We can compute this efficiently using the fact that the bitwise AND of a range of numbers decreases as the range increases.
        # We can precompute the bitwise AND for each number from L to R.
        # However, for large R (up to 1e18), we need an efficient way.
        # The key observation is that the bitwise AND of a range of numbers from L to i will eventually become 0 once all bits are cleared.
        # So we can find the point where the AND becomes 0 and compute the sum accordingly.
        
        # Precompute the bitwise AND for each i from L to R
        # But for large R, this is not feasible. So we need a smarter way.
        
        # Let's compute the bitwise AND of L to i for all i from L to R
        # We can do this by maintaining the current AND value as we iterate from L to R
        # The AND value will eventually become 0 once all bits are cleared.
        
        current_and = L
        total = 0
        for i in range(L, R + 1):
            current_and &= i
            total += current_and
            total %= MOD
        results.append(total % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
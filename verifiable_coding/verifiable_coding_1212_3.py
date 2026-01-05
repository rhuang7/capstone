import sys
from collections import Counter

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    
    for S in cases:
        cnt = Counter(S)
        freq = list(cnt.values())
        n = len(S)
        freq.sort()
        
        # Find the maximum possible number of distinct characters that can be used
        # such that each occurs exactly k times
        # The total number of characters is n, so k * m = n, where m is the number of distinct characters
        # We need to find the maximum m such that k = n // m and k * m = n
        # Then, the minimum number of operations is n - (k * m)
        # But we need to find the maximum m such that k * m = n and k is the same for all characters
        # So we try all possible m from 1 to min(26, n)
        # For each m, check if n is divisible by m, and if so, compute the required number of operations
        
        min_ops = n
        for m in range(1, min(26, n) + 1):
            if n % m == 0:
                k = n // m
                # We need to have exactly m distinct characters, each appearing k times
                # So we need to have at least m characters in the frequency list with count >= k
                # So count how many frequencies are >= k
                count = 0
                for f in freq:
                    if f >= k:
                        count += 1
                if count >= m:
                    # We can make a balanced string with m distinct characters
                    # The number of operations is n - (k * m)
                    ops = n - (k * m)
                    if ops < min_ops:
                        min_ops = ops
        print(min_ops)

if __name__ == '__main__':
    solve()
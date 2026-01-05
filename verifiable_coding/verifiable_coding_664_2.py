import sys
import math

MOD = 998244353

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for _ in range(T):
        p = int(data[idx])
        q = int(data[idx+1])
        r = int(data[idx+2])
        idx += 3
        
        # Total rooms must be exactly r
        # We need to split the rooms into two types: footballer rooms and cricketer rooms
        # Let's say there are x footballer rooms and y cricketer rooms, such that x + y = r
        # Also, each cricketer room must have at least 2 cricketers
        # And each footballer room must have at least 1 footballer
        total = 0
        for x in range(0, r + 1):
            y = r - x
            # Check if x footballer rooms can hold p footballers
            # Each room must have at least 1, so we need to distribute p into x rooms with at least 1 each
            # This is equivalent to putting p - x into x rooms with no restriction
            # So the number of ways is comb(p - 1, x - 1)
            if p < x:
                continue
            ways_footballers = comb(p - 1, x - 1)
            # Check if y cricketer rooms can hold q cricketers
            # Each room must have at least 2, so we need to distribute q into y rooms with at least 2 each
            # This is equivalent to putting q - 2*y into y rooms with no restriction
            if q < 2 * y:
                continue
            ways_cricketers = comb(q - 1, y - 1)
            total += ways_footballers * ways_cricketers
            total %= MOD
        
        print(total % MOD)

if __name__ == '__main__':
    solve()
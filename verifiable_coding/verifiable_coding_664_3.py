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
        # Let x be the number of footballer rooms, y be the number of cricketer rooms
        # x + y = r
        # For each x, y = r - x
        # For each x, we need to choose x rooms for footballers and y rooms for cricketers
        # For cricketers, each room must have at least 2 players
        # So the number of ways to split q cricketers into y rooms with each room having at least 2 is:
        # C(q-1, y-1) - C(q-1, y-2) (using stars and bars with constraints)
        # But since the rooms are identical, we need to count the number of ways to partition q cricketers into y non-empty groups of size >=2
        # This is equivalent to the number of integer solutions of a1 + a2 + ... + ay = q, where ai >= 2
        # Which is the same as the number of integer solutions of b1 + b2 + ... + by = q - 2y, where bi >= 0
        # This is C(q - 2y + y - 1, y - 1) = C(q - y - 1, y - 1)
        # But only if q - y - 1 >= 0
        # So for each x in 0 to r:
        # y = r - x
        # If y < 0: continue
        # If q < 2*y: continue
        # Then the number of ways to split cricketers is C(q - y - 1, y - 1)
        # The number of ways to split footballers is C(p, x)
        # Multiply these and sum over all valid x
        total = 0
        for x in range(0, r + 1):
            y = r - x
            if y < 0:
                continue
            # Check if we can split footballers into x rooms
            if x > p:
                continue
            # Check if we can split cricketers into y rooms with each room having at least 2
            if q < 2 * y:
                continue
            # Number of ways to split footballers into x rooms
            ways_footballers = comb(p, x)
            # Number of ways to split cricketers into y rooms with each room having at least 2
            # This is equivalent to the number of integer solutions of a1 + a2 + ... + ay = q, where ai >= 2
            # Which is C(q - 2y + y - 1, y - 1) = C(q - y - 1, y - 1)
            ways_cricketers = comb(q - y - 1, y - 1)
            total += ways_footballers * ways_cricketers
            total %= MOD
        print(total % MOD)

if __name__ == '__main__':
    solve()
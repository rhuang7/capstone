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
    index = 1
    results = []
    for _ in range(T):
        p = int(data[index])
        q = int(data[index+1])
        r = int(data[index+2])
        index += 3
        
        # Total rooms must be exactly r
        # We need to split the rooms into two groups: footballer rooms and cricketer rooms
        # Let x be the number of rooms for footballers, y be the number of rooms for cricketers
        # x + y = r
        # Also, y must be at least 1 (since cricketers can't be alone)
        # And x must be at least 1 (since no room can be empty)
        # So y ranges from 1 to r-1, and x = r - y
        # For each y, we compute:
        # - Ways to choose y rooms for cricketers: comb(r, y)
        # - Ways to split q cricketers into y rooms, each with at least 2: this is the same as putting q cricketers into y rooms with each room having at least 2
        # - Ways to split p footballers into x rooms, each with at least 1: this is the same as putting p footballers into x rooms with each room having at least 1
        # The total is the sum over all valid y of (comb(r, y) * (ways to split cricketers) * (ways to split footballers))
        
        total = 0
        for y in range(1, r):
            x = r - y
            if x < 1 or y < 1:
                continue
            # Ways to choose y rooms for cricketers
            ways_c = comb(r, y)
            # Ways to split q cricketers into y rooms, each with at least 2
            # This is the same as putting q cricketers into y rooms with each room having at least 2
            # Which is equivalent to putting q - 2*y cricketers into y rooms with each room having at least 0
            # So it's comb(q - 2*y + y - 1, y - 1) = comb(q - y - 1, y - 1)
            if q < 2*y:
                continue
            ways_c += comb(q - y - 1, y - 1)
            # Ways to split p footballers into x rooms, each with at least 1
            # This is the same as putting p footballers into x rooms with each room having at least 1
            # Which is comb(p - 1, x - 1)
            if p < x:
                continue
            ways_f = comb(p - 1, x - 1)
            total += ways_c * ways_f
            total %= MOD
        results.append(total % MOD)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
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
    for _ in range(T):
        p = int(data[index])
        q = int(data[index+1])
        r = int(data[index+2])
        index += 3
        
        # Total rooms must be exactly r
        # Each room is non-empty, and contains only footballers or only cricketers
        # No cricketer can be alone in a room
        # All rooms are identical
        
        # We need to split the r rooms into two parts: some for footballers, some for cricketers
        # Let x be the number of rooms for footballers, y be the number for cricketers
        # x + y = r
        # x >= 0, y >= 0
        # For each x, y = r - x
        # We need to count the number of ways to split p footballers into x non-empty rooms
        # And q cricketers into y non-empty rooms, each of which has at least 2 cricketers
        
        total = 0
        for x in range(0, r + 1):
            y = r - x
            # Check if x rooms can hold p footballers (each room non-empty)
            # Number of ways to split p footballers into x non-empty rooms = S(p, x) * x! (Stirling numbers of the second kind)
            # But since rooms are identical, it's just S(p, x)
            # Similarly for cricketers: split into y rooms, each with at least 2 cricketers
            # Number of ways to split q cricketers into y rooms, each with at least 2 = S(q - y, y) * y! / (y!)? Wait, need to think
            # For cricketers, each room must have at least 2, so we need to distribute q cricketers into y rooms, each with at least 2
            # This is equivalent to distributing (q - 2y) cricketers into y rooms, each with at least 0
            # So the number of ways is comb(q - 2y + y - 1, y - 1) if q >= 2y, else 0
            # But since rooms are identical, it's the same as the number of integer solutions to a1 + a2 + ... + ay = q - 2y, where ai >= 0
            # Which is comb(q - 2y + y - 1, y - 1) = comb(q - y - 1, y - 1)
            # But only if q >= 2y
            # So for cricketers, the number of ways is comb(q - y - 1, y - 1) if q >= 2y, else 0
            # But since rooms are identical, we don't multiply by y! or anything
            # So the total is comb(p - 1, x - 1) * comb(q - y - 1, y - 1) if p >= x and q >= 2y
            # But since rooms are identical, we don't multiply by x! or y!
            # So the total for this x and y is comb(p - 1, x - 1) * comb(q - y - 1, y - 1)
            # But only if p >= x and q >= 2y
            # Also, x must be >= 1 or y must be >= 1 (but since x + y = r, if x=0 then y=r, but then cricketers must be in r rooms, each with at least 2)
            # So the code becomes:
            if x == 0:
                # All rooms are for cricketers
                if q >= 2 * r:
                    # Number of ways to split q cricketers into r rooms, each with at least 2
                    # This is comb(q - r - 1, r - 1)
                    ways = comb(q - r - 1, r - 1)
                    total += ways
                else:
                    pass
            elif y == 0:
                # All rooms are for footballers
                if p >= r:
                    # Number of ways to split p footballers into r rooms, each non-empty
                    # This is comb(p - 1, r - 1)
                    ways = comb(p - 1, r - 1)
                    total += ways
                else:
                    pass
            else:
                # x rooms for footballers, y rooms for cricketers
                if p >= x and q >= 2 * y:
                    # Number of ways to split p footballers into x rooms, each non-empty
                    # This is comb(p - 1, x - 1)
                    # Number of ways to split q cricketers into y rooms, each with at least 2
                    # This is comb(q - y - 1, y - 1)
                    ways = comb(p - 1, x - 1) * comb(q - y - 1, y - 1)
                    total += ways
        print(total % MOD)

if __name__ == '__main__':
    solve()
import sys
MOD = 998244353

def comb(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)
    return res

def solve():
    import sys
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
        # We need to split the rooms into two parts: some for footballers, some for cricketers
        # Let's try all possible ways to split the rooms into x for footballers and y for cricketers
        # where x + y = r, x >= 0, y >= 0
        total = 0
        for x in range(r + 1):
            y = r - x
            # Check if it's possible to place footballers in x rooms and cricketers in y rooms
            # Footballers: must be placed in x rooms, each room has at least 1
            # So the number of ways to place footballers is comb(p-1, x-1)
            # Cricketers: must be placed in y rooms, each room has at least 2
            # So the number of ways to place cricketers is comb(q-1, y-1) if q >= 2*y
            # But since cricketers can't be alone, each room must have at least 2
            # So the number of ways to place cricketers is comb(q-1, y-1) if q >= 2*y
            # But we also need to check if y is >= 1 (since cricketers can't be alone in a room)
            # So if y == 0, then q must be 0
            # Also, if x == 0, then p must be 0
            if x == 0:
                if p == 0:
                    # All rooms are for cricketers
                    if y == 0:
                        # No rooms, but p and q are 0
                        total += 1
                    else:
                        # All rooms are for cricketers, but y > 0
                        # So q must be >= 2*y
                        if q >= 2 * y:
                            # Number of ways to place cricketers is comb(q-1, y-1)
                            total += comb(q-1, y-1)
                else:
                    continue
            else:
                if p == 0:
                    continue
                # Number of ways to place footballers is comb(p-1, x-1)
                ways_footballers = comb(p-1, x-1)
                if y == 0:
                    # All rooms are for footballers
                    if q == 0:
                        total += ways_footballers
                    else:
                        continue
                else:
                    if q == 0:
                        continue
                    # Number of ways to place cricketers is comb(q-1, y-1) if q >= 2*y
                    if q >= 2 * y:
                        ways_cricketers = comb(q-1, y-1)
                        total += ways_footballers * ways_cricketers
        print(total % MOD)

if __name__ == '__main__':
    solve()
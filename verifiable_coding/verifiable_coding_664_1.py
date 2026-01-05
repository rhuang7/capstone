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
        
        # Total rooms must be r
        # We need to split r rooms into two parts: some for footballers, some for cricketers
        # Let x be the number of rooms for footballers, y be the number for cricketers
        # x + y = r
        # x >= 0, y >= 0
        # Also, for cricketers: y rooms, each must have at least 2 cricketers
        # So, the number of ways to distribute q cricketers into y rooms with each room having at least 2 is C(q-1, y-1) if q >= 2*y
        # The number of ways to distribute p footballers into x rooms with each room having at least 1 is C(p-1, x-1) if p >= x
        # Also, the number of ways to choose x rooms out of r is C(r, x)
        # So total ways is sum over x from 0 to r of [C(r, x) * C(p-1, x-1) * C(q-1, y-1)] where y = r - x and q >= 2*y
        total = 0
        for x in range(0, r + 1):
            y = r - x
            if y < 0:
                continue
            # Check if footballers can be distributed into x rooms
            if p < x:
                continue
            # Check if cricketers can be distributed into y rooms with each room having at least 2
            if q < 2 * y:
                continue
            # Number of ways to choose x rooms out of r
            c1 = comb(r, x)
            # Number of ways to distribute p footballers into x rooms
            c2 = comb(p-1, x-1)
            # Number of ways to distribute q cricketers into y rooms with each room having at least 2
            c3 = comb(q-1, y-1)
            total += c1 * c2 * c3
            total %= MOD
        print(total % MOD)

if __name__ == '__main__':
    solve()
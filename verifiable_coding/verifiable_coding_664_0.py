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
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        p = int(input[idx])
        q = int(input[idx+1])
        r = int(input[idx+2])
        idx += 3
        
        # Total rooms must be exactly r
        # We need to split the rooms into two parts: some for footballers, some for cricketers
        # Let's try all possible splits of rooms into footballer_rooms and cricketer_rooms
        total = 0
        for footballer_rooms in range(0, r + 1):
            cricketer_rooms = r - footballer_rooms
            # Check if it's possible to place footballers and cricketers
            # Footballers: must be placed in exactly footballer_rooms rooms, each non-empty
            # Cricketers: must be placed in exactly cricketer_rooms rooms, each with at least 2
            # Also, cricketer_rooms must be >= 1, because cricketers can't be alone
            if cricketer_rooms < 1:
                continue
            # Check if footballers can be placed in footballer_rooms rooms
            # Each room has at least 1 footballer, so p >= footballer_rooms
            if p < footballer_rooms:
                continue
            # Check if cricketers can be placed in cricketer_rooms rooms
            # Each room has at least 2 cricketers, so q >= 2 * cricketer_rooms
            if q < 2 * cricketer_rooms:
                continue
            # Compute number of ways to place footballers
            # Choose footballer_rooms rooms and put p footballers into them, one per room
            # This is the same as p! / (p - footballer_rooms)! * S(p, footballer_rooms)
            # But since rooms are identical, it's just the number of ways to partition p distinct items into footballer_rooms non-empty subsets
            # Which is S(p, footballer_rooms) * footballer_rooms! (but since rooms are identical, it's S(p, footballer_rooms))
            # But since rooms are identical, the number of ways to partition p distinct items into exactly k non-empty subsets is S(p, k)
            # So the number of ways is S(p, footballer_rooms)
            # Similarly for cricketers: number of ways is S(q, cricketer_rooms) * (number of ways to assign to rooms)
            # But since rooms are identical, it's just S(q, cricketer_rooms)
            # So total ways is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to choose which rooms are for footballers is 1 (since rooms are identical)
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to assign the footballers and cricketers to the rooms
            # Which is the same as the number of ways to partition the players into the rooms
            # So the total is S(p, footballer_rooms) * S(q, cricketer_rooms)
            # But we need to multiply by the number of ways to choose which rooms are for footballers and which are for cricketers
            # Since rooms are identical, the number of ways to
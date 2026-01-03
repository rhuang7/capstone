import sys
import math

MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    events = []
    idx = 1
    for _ in range(n):
        b = int(data[idx])
        d = int(data[idx+1])
        events.append((b, d))
        idx += 2

    if n == 0:
        print(0)
        return

    # Create events for boarding and departure
    events = [(b, 1) for b, d in events] + [(d, -1) for b, d in events]
    events.sort()

    # Process events
    res = 0
    current_passengers = 0
    prev_coord = None
    for coord, delta in events:
        if prev_coord is not None and coord != prev_coord:
            res += current_passengers * (coord - prev_coord)
            res %= MOD
        current_passengers += delta
        prev_coord = coord

    print(res % MOD)

if __name__ == '__main__':
    solve()
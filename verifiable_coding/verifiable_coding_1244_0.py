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

    # Sort events by boarding point
    events.sort()

    # Create a list of all unique points
    points = set()
    for b, d in events:
        points.add(b)
        points.add(d)
    points = sorted(points)

    # Create a list of events for each point
    events = []
    for p in points:
        for b, d in events:
            if b == p or d == p:
                events.append((p, 'start' if b == p else 'end'))

    # Sort events by point, and for same point, start before end
    events.sort(key=lambda x: (x[0], 0 if x[1] == 'start' else 1))

    # Calculate infection severity
    severity = 0
    passengers = 0
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        # The infection degree is the number of passengers at p1
        severity += passengers * (p2 - p1)
        severity %= MOD

    print(severity % MOD)

if __name__ == '__main__':
    solve()
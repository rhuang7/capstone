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
        idx += 2
        events.append((b, d))
    
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
    for b, d in events:
        events.append((b, 1))  # boarding
        events.append((d, -1))  # departure
    
    # Sort events by point, and for same point, departure before boarding
    events.sort(key=lambda x: (x[0], x[1]))
    
    # Calculate infection severity
    total = 0
    current_passengers = 0
    prev_point = None
    for i in range(len(points)):
        point = points[i]
        if prev_point is not None and prev_point != point:
            # Calculate the distance between prev_point and point
            distance = point - prev_point
            # Multiply by current_passengers and add to total
            total = (total + distance * current_passengers) % MOD
        prev_point = point
    
    # Add the last segment
    if prev_point is not None:
        # Calculate the distance from prev_point to infinity (but we need to stop when no passengers are left)
        # So we need to find the last point with passengers
        last_point = prev_point
        for b, d in events:
            if b > last_point:
                last_point = b
                break
        distance = last_point - prev_point
        total = (total + distance * current_passengers) % MOD
    
    print(total % MOD)

if __name__ == '__main__':
    solve()
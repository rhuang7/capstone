import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        while idx < len(data) and data[idx] == '':
            idx += 1
        if idx >= len(data):
            break
        n = int(data[idx])
        idx += 1
        while idx < len(data) and data[idx] == '':
            idx += 1
        points = []
        for _ in range(n):
            x = int(data[idx])
            y = int(data[idx+1])
            points.append((x, y))
            idx += 2
        # Sort points according to the rules
        points.sort(key=lambda p: (p[0], -p[1]))
        # Compute the path
        total = 0.0
        prev_x, prev_y = points[0]
        for i in range(1, len(points)):
            curr_x, curr_y = points[i]
            dx = curr_x - prev_x
            dy = curr_y - prev_y
            total += math.hypot(dx, dy)
            prev_x, prev_y = curr_x, curr_y
        # Add the last segment to the end point
        # The end point is the one with greatest X and least Y
        end_x, end_y = points[-1]
        # Find the point with greatest X and least Y
        end_point = None
        min_y = float('inf')
        for p in points:
            if p[0] == end_x and p[1] < min_y:
                min_y = p[1]
                end_point = p
        # Compute the distance from the last point to the end point
        dx = end_point[0] - prev_x
        dy = end_point[1] - prev_y
        total += math.hypot(dx, dy)
        results.append(f"{total:.2f}")
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
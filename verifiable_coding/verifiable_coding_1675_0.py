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
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            dx = x2 - x1
            dy = y2 - y1
            total += math.hypot(dx, dy)
        # Format the result to 2 decimal places
        results.append("{0:.2f}".format(total))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
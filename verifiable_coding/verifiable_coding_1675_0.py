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
            y = int(data[idx + 1])
            points.append((x, y))
            idx += 2
        # Sort points based on the given rules
        points.sort(key=lambda p: (p[0], -p[1]))
        # Calculate total distance
        total = 0.0
        for i in range(1, len(points)):
            total += math.hypot(points[i][0] - points[i-1][0], points[i][1] - points[i-1][1])
        results.append("{0:.2f}".format(total))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
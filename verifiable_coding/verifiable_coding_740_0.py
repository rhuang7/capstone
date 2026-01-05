import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx+1])
        K = int(data[idx+2])
        idx += 3
        plants = []
        for _ in range(K):
            r = int(data[idx])
            c = int(data[idx+1])
            plants.append((r, c))
            idx += 2
        
        # Convert to 0-based indices
        plants = [(r-1, c-1) for r, c in plants]
        
        # Compute the minimal fence length
        # The minimal fence length is the perimeter of the convex hull of the plants
        # We can use the convex hull algorithm to find the perimeter
        
        # Sort the points
        plants.sort()
        
        # Compute convex hull
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        
        def convex_hull(points):
            points = sorted(set(points))
            if len(points) <= 1:
                return points
            lower = []
            for p in points:
                while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                    lower.pop()
                lower.append(p)
            upper = []
            for p in reversed(points):
                while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                    upper.pop()
                upper.append(p)
            return lower[:-1] + upper[:-1]
        
        hull = convex_hull(plants)
        if len(hull) == 0:
            results.append(0)
            continue
        
        # Compute the perimeter of the convex hull
        perimeter = 0
        n = len(hull)
        for i in range(n):
            x1, y1 = hull[i]
            x2, y2 = hull[(i+1)%n]
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            perimeter += dx + dy
        
        results.append(perimeter)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
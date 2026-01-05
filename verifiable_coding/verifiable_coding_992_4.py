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
        idx += 1
        poly = []
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx+1])
            poly.append((x, y))
            idx += 2
        M = int(data[idx])
        idx += 1
        stripes = []
        for _ in range(M):
            L = int(data[idx])
            C = int(data[idx+1])
            stripes.append((L, C))
            idx += 2
        
        # Compute perimeter of the polygon
        perimeter = 0.0
        for i in range(N):
            x1, y1 = poly[i]
            x2, y2 = poly[(i+1)%N]
            dx = x2 - x1
            dy = y2 - y1
            perimeter += math.hypot(dx, dy)
        
        # Sort stripes by cost per unit length
        stripes.sort(key=lambda x: x[1]/x[0] if x[0] > 0 else 0)
        
        # Use greedy approach: use as many as possible of the cheapest stripe
        min_cost = 0
        for L, C in stripes:
            if L == 0:
                continue
            count = math.ceil(perimeter / L)
            min_cost += count * C
        
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
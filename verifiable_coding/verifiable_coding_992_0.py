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
        polygon = []
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx + 1])
            polygon.append((x, y))
            idx += 2
        M = int(data[idx])
        idx += 1
        stripes = []
        for _ in range(M):
            L = int(data[idx])
            C = int(data[idx + 1])
            stripes.append((L, C))
            idx += 2
        
        # Compute perimeter of the polygon
        perimeter = 0.0
        for i in range(N):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % N]
            dx = x2 - x1
            dy = y2 - y1
            perimeter += math.hypot(dx, dy)
        
        # Sort stripes by cost per unit length
        stripes.sort(key=lambda x: x[1] / x[0])
        
        # Use greedy approach: use the cheapest per unit length stripe as much as possible
        min_cost = 0
        for L, C in stripes:
            if perimeter <= 0:
                break
            if L >= perimeter:
                min_cost += math.ceil(perimeter / L) * C
                break
            else:
                count = math.ceil(perimeter / L)
                min_cost += count * C
                perimeter -= count * L
        
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
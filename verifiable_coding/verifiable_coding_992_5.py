import sys
import math

def compute_perimeter(polygon):
    perimeter = 0.0
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        dx = x2 - x1
        dy = y2 - y1
        perimeter += math.hypot(dx, dy)
    return perimeter

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
        perimeter = compute_perimeter(polygon)
        # Sort stripes by cost per unit length
        stripes.sort(key=lambda x: x[1]/x[0] if x[0] > 0 else 0)
        # Find minimum cost
        min_cost = 0
        remaining = perimeter
        for L, C in stripes:
            if remaining <= 0:
                break
            if L >= remaining:
                min_cost += math.ceil(remaining / L) * C
                remaining = 0
            else:
                min_cost += C
                remaining -= L
        results.append(str(min_cost))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
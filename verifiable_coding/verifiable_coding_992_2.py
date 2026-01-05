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
        # Use dynamic programming to find minimum cost
        # Sort stripes by cost per unit length
        stripes.sort(key=lambda x: x[1]/x[0] if x[0] > 0 else 0)
        # Precompute cost per unit length
        cost_per_unit = [c / l for l, c in stripes]
        # Use binary search to find minimum cost
        # We need to cover perimeter with stripes
        # We can use a greedy approach: use the cheapest per unit length stripe as much as possible
        min_cost = 0
        for l, c in stripes:
            if l == 0:
                continue
            if perimeter <= 0:
                break
            # How many of this stripe can we use?
            count = int(perimeter / l)
            min_cost += count * c
            perimeter -= count * l
        results.append(str(min_cost))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
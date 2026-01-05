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
        # We need to cover the perimeter with stripes
        # We can use a greedy approach: choose the cheapest stripe that can cover the most of the perimeter
        # Sort stripes by cost per unit length
        stripes.sort(key=lambda x: x[1] / x[0])
        
        total_cost = 0
        remaining = perimeter
        for L, C in stripes:
            if remaining <= 0:
                break
            # How much of the perimeter can this stripe cover?
            # Since the stripe can be placed anywhere, we can cover up to L length
            # So we can take min(L, remaining) of the perimeter
            # But since we want to minimize cost, we take as much as possible
            take = min(L, remaining)
            total_cost += (take / L) * C
            remaining -= take
        
        results.append(str(total_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
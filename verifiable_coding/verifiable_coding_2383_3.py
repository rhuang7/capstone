import sys

def solve():
    import math
    input = sys.stdin.buffer.read().split()
    t = int(input[0])
    idx = 1
    results = []
    for _ in range(t):
        a = int(input[idx])
        b = int(input[idx+1])
        idx += 2
        # Case 1: Place both rectangles side by side along the longer side
        side1 = max(2 * a, 2 * b)
        side2 = max(a, b)
        side = max(side1, side2)
        area1 = side * side
        
        # Case 2: Place both rectangles stacked on top of each other
        side3 = max(a, b)
        side4 = 2 * min(a, b)
        side = max(side3, side4)
        area2 = side * side
        
        # Case 3: One rectangle rotated, placed next to the other
        # Check both orientations
        side5 = max(a + b, max(a, b))
        side6 = max(a, b)
        side = max(side5, side6)
        area3 = side * side
        
        # Find the minimum area
        min_area = min(area1, area2, area3)
        results.append(str(min_area))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
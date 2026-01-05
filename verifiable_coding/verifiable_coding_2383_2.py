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
        # Two possibilities for placing the rectangles
        # 1. Place them side by side along the longer side
        # 2. Place them one on top of the other along the longer side
        # 3. Place them in a way that one is rotated
        # Compute the minimum square side
        # Case 1: Place side by side
        side1 = max(2 * a, b)
        # Case 2: Place one on top of the other
        side2 = max(a, 2 * b)
        # Case 3: One rotated, side by side
        side3 = max(2 * min(a, b), max(a, b))
        # Case 4: One rotated, one on top
        side4 = max(min(a, b), 2 * max(a, b))
        # Find the minimum side
        min_side = min(side1, side2, side3, side4)
        results.append(min_side * min_side)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
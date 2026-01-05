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
        # Find the minimum square side
        # Case 1: place side by side along the longer side
        side1 = max(2 * a, b)
        # Case 2: place one on top of the other along the longer side
        side2 = max(a, 2 * b)
        # Case 3: place one rotated (a and b swapped)
        # Check if rotating helps
        # Case 3a: place side by side along the longer side after rotation
        side3 = max(2 * b, a)
        # Case 3b: place one on top of the other along the longer side after rotation
        side4 = max(b, 2 * a)
        # Find the minimum side
        min_side = min(side1, side2, side3, side4)
        results.append(min_side * min_side)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
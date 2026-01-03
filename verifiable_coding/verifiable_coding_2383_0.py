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
        # Case 1: place both rectangles side by side horizontally
        side1 = max(2 * a, b)
        # Case 2: place both rectangles side by side vertically
        side2 = max(2 * b, a)
        # Case 3: place one rectangle on top of the other (rotated)
        side3 = max(a + b, max(a, b))
        # Find the minimum side
        min_side = min(side1, side2, side3)
        results.append(min_side * min_side)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
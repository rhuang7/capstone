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
        # 2. Place them one above the other along the longer side
        # 3. Place them in a way that one is rotated
        # Calculate the minimum side length of the square
        # Case 1: Place them side by side along the longer side
        # The total length is max(a, b) * 2, the height is min(a, b)
        # The square side is max(max(a, b) * 2, min(a, b))
        # Case 2: Place them one above the other along the longer side
        # The total height is max(a, b) * 2, the length is min(a, b)
        # The square side is max(max(a, b) * 2, min(a, b))
        # Case 3: Place them in a way that one is rotated
        # The total length is max(a, b) + min(a, b)
        # The square side is max(max(a, b) + min(a, b), max(a, b))
        # The minimum of all these cases
        side1 = max(2 * max(a, b), min(a, b))
        side2 = max(2 * max(a, b), min(a, b))
        side3 = max(max(a, b) + min(a, b), max(a, b))
        min_side = min(side1, side2, side3)
        results.append(min_side * min_side)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
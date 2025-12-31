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
        # 2. Place them one on top of the other
        # We need to find the minimum square that can contain both
        # Case 1: Place side by side along the longer side
        # The total length is max(a, b) * 2, the height is min(a, b)
        # The square side is max(max(a, b) * 2, min(a, b))
        # Case 2: Place one on top of the other
        # The total height is max(a, b) * 2, the width is min(a, b)
        # The square side is max(max(a, b) * 2, min(a, b))
        # The minimum of the two cases is the answer
        # But also consider the case where the rectangles are rotated
        # So we need to check both orientations
        # So we need to try all possible orientations
        # Try all possible orientations for the rectangles
        # The possible orientations are (a, b) and (b, a)
        # For each orientation, compute the minimum square side
        # The minimum of all possibilities is the answer
        min_side = float('inf')
        for w, h in [(a, b), (b, a)]:
            # Case 1: side by side
            side1 = max(2 * w, h)
            # Case 2: one on top of the other
            side2 = max(2 * h, w)
            min_side = min(min_side, side1, side2)
        results.append(str(min_side * min_side))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
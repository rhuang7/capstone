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
        # Case 1: Place them side by side along the longer side
        # The square side is max(2*a, b) if a >= b, or max(2*b, a) if b >= a
        # Case 2: Place them one on top of the other along the longer side
        # The square side is max(a, 2*b) if a >= b, or max(b, 2*a) if b >= a
        # Case 3: Place them in a way that one is rotated and the other is not
        # The square side is max(a + b, max(a, b)) if a != b, or max(2*a, a) if a == b
        # The minimal square side is the minimum of the above cases
        # The minimal square area is (min_square_side)^2
        # We need to consider all possible orientations
        # Case 1: both rectangles placed side by side along the longer side
        if a >= b:
            case1 = max(2*a, b)
        else:
            case1 = max(2*b, a)
        # Case 2: both rectangles placed one on top of the other along the longer side
        if a >= b:
            case2 = max(a, 2*b)
        else:
            case2 = max(b, 2*a)
        # Case 3: one rectangle rotated and the other not
        # The square side is max(a + b, max(a, b))
        case3 = max(a + b, max(a, b))
        # The minimal square side is the minimum of the above cases
        min_side = min(case1, case2, case3)
        results.append(min_side * min_side)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
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
        # Two possibilities for the square side:
        # 1. Place the two rectangles side by side (lengthwise)
        #    square side = max(a * 2, b)
        # 2. Place the two rectangles one on top of the other (heightwise)
        #    square side = max(a, b * 2)
        # 3. Rotate the rectangles and place them side by side
        #    square side = max(a + b, max(a, b))
        # 4. Rotate the rectangles and place them one on top of the other
        #    square side = max(a, b + a)
        # Take the minimum of all possible square sides
        side1 = max(a * 2, b)
        side2 = max(a, b * 2)
        side3 = max(a + b, max(a, b))
        side4 = max(a, b + a)
        min_side = min(side1, side2, side3, side4)
        results.append(str(min_side * min_side))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
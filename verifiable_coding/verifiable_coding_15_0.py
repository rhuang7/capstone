import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        x = int(data[index+2])
        y = int(data[index+3])
        index += 4
        
        # Max area without the dead pixel
        # Consider all possible rectangles that don't include (x, y)
        # The maximum area is the maximum of:
        # (a - 1) * b (exclude the dead pixel from the left)
        # a * (b - 1) (exclude the dead pixel from the bottom)
        # (x) * b (exclude the dead pixel from the right)
        # a * (y) (exclude the dead pixel from the top)
        # Also consider the maximum of (a - x - 1) * b and a * (b - y - 1)
        # The maximum of these is the answer
        max_area = max(
            (a - 1) * b,
            a * (b - 1),
            x * b,
            a * y,
            (a - x - 1) * b,
            a * (b - y - 1)
        )
        results.append(str(max_area))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
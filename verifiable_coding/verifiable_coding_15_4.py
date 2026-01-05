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
        # Consider all possible rectangles that avoid (x, y)
        # The maximum area is the maximum of:
        # (a - 1) * b (exclude the dead pixel from the left)
        # a * (b - 1) (exclude the dead pixel from the bottom)
        # (x) * b (exclude the dead pixel from the right)
        # a * (y) (exclude the dead pixel from the top)
        # Also consider the maximum of (a - 1) * (b - 1) if the dead pixel is in the middle
        max_area = max((a - 1) * b, a * (b - 1), x * b, a * y)
        results.append(max_area)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
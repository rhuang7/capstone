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
        # The dead pixel divides the screen into four regions
        # We can take the maximum area from these regions
        max_area = 0
        # Left region
        max_area = max(max_area, (x) * b)
        # Right region
        max_area = max(max_area, (a - x - 1) * b)
        # Top region
        max_area = max(max_area, a * y)
        # Bottom region
        max_area = max(max_area, a * (b - y - 1))
        results.append(str(max_area))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
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
        
        # Calculate the maximum area of a rectangle that doesn't include (x, y)
        # The maximum area is the maximum of the following four possibilities:
        # 1. Rectangle to the left of x
        # 2. Rectangle to the right of x
        # 3. Rectangle above y
        # 4. Rectangle below y
        max_area = 0
        max_area = max(max_area, x * b)  # left
        max_area = max(max_area, (a - x - 1) * b)  # right
        max_area = max(max_area, a * y)  # below
        max_area = max(max_area, a * (b - y - 1))  # above
        results.append(str(max_area))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
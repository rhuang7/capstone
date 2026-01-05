import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        points = []
        for _ in range(4 * N - 1):
            x = int(data[idx])
            y = int(data[idx + 1])
            points.append((x, y))
            idx += 2
        
        x_counts = collections.defaultdict(int)
        y_counts = collections.defaultdict(int)
        
        for x, y in points:
            x_counts[x] += 1
            y_counts[y] += 1
        
        missing_x = None
        missing_y = None
        
        for x in x_counts:
            if x_counts[x] == 1:
                missing_x = x
                break
        
        for y in y_counts:
            if y_counts[y] == 1:
                missing_y = y
                break
        
        results.append(f"{missing_x} {missing_y}")
    
    print("\n".join(results))
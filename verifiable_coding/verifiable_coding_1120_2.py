import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        R = int(data[idx])
        C = int(data[idx+1])
        idx += 2
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        
        # Total number of cells
        total = R * C
        # Distance from initial case to the farthest cell
        max_dist = max(abs(x), abs(y), R - 1 - x, C - 1 - y)
        # Days required is the maximum distance
        days = max_dist
        
        results.append(str(days))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
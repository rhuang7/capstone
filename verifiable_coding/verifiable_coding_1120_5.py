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
        
        # Calculate the number of days needed to infect the entire grid
        # The virus spreads in all four directions (up, down, left, right)
        # The maximum distance from the initial cell is max(R-1 - x, C-1 - y, x, y)
        # The number of days is the maximum distance + 1
        max_dist = max(R - 1 - x, C - 1 - y, x, y)
        days = max_dist + 1
        results.append(str(days))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
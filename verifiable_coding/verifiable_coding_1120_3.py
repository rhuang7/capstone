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
        
        # Calculate the number of days
        # The virus spreads in all 4 directions each day
        # The number of days is the maximum of (x, y, R-1-x, C-1-y) + 1
        # Because the virus spreads from the initial point in all directions
        # The maximum distance from the initial point to any cell is the maximum of the four distances
        # The number of days is that maximum distance + 1 (since day 0 is the initial day)
        max_dist = max(x, y, R-1-x, C-1-y)
        days = max_dist + 1
        results.append(str(days))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
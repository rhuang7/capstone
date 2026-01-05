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
        
        # Calculate the number of days required to infect the entire grid
        # The virus spreads in all four directions each day
        # The maximum distance from the initial point is max(R-1-x, C-1-y)
        # The number of days is the maximum distance + 1
        max_dist = max(R - 1 - x, C - 1 - y)
        days = max_dist + 1
        results.append(str(days))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
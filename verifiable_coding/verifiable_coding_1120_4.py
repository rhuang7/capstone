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
        # The virus spreads in all four directions each day
        # The maximum distance from the initial case is max(R-1, C-1)
        # The number of days is the ceiling of log2(total_cells / initial_cells)
        total_cells = R * C
        initial_cells = 1
        if total_cells == 1:
            results.append(0)
            continue
        
        # The number of days is the smallest integer d such that 2^d >= total_cells
        # Since the virus spreads exponentially, the number of days is the ceiling of log2(total_cells)
        days = math.ceil(math.log2(total_cells))
        results.append(days)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
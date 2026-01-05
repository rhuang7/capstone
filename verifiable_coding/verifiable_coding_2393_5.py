import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        grid = data[idx:idx + n]
        idx += n
        
        # Check if the grid is valid
        valid = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '1':
                    # Check if it's possible for this 1 to be placed by a cannon
                    # It must be reachable from the top or left
                    # Also, it must not be blocked by another 1 in the direction of the cannon
                    # Check if it's in the first row or first column
                    if i == 0 or j == 0:
                        # It could be placed by a cannon in the first row or first column
                        continue
                    # Check if there is a path from the top or left to this cell without being blocked
                    # Check if there is a 1 in the same column above it
                    has_one_above = False
                    for k in range(i - 1, -1, -1):
                        if grid[k][j] == '1':
                            has_one_above = True
                            break
                    # Check if there is a 1 in the same row to the left
                    has_one_left = False
                    for k in range(j - 1, -1, -1):
                        if grid[i][k] == '1':
                            has_one_left = True
                            break
                    # If both have ones, then this cell is blocked
                    if has_one_above and has_one_left:
                        valid = False
                        break
            if not valid:
                break
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))
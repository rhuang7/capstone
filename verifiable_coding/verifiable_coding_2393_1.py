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
        grid = data[idx]
        idx += 1
        grid = [list(grid[i*n:(i+1)*n]) for i in range(n)]
        
        valid = True
        # Check if any 1 is in a position that cannot be reached by any cannon
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '1':
                    # Check if it's in the first row or first column
                    if i == 0 or j == 0:
                        # It can be reached by a cannon
                        continue
                    # Check if it's in a position that would require a 1 to be in front of it
                    # For a cannon in row i, moving right
                    if i > 0 and grid[i][j] == '1':
                        # Check if there's a 1 in the same column above it
                        for k in range(i-1, -1, -1):
                            if grid[k][j] == '1':
                                valid = False
                                break
                        if not valid:
                            break
                    # For a cannon in column j, moving down
                    if j > 0 and grid[i][j] == '1':
                        # Check if there's a 1 in the same row to the left
                        for k in range(j-1, -1, -1):
                            if grid[i][k] == '1':
                                valid = False
                                break
                        if not valid:
                            break
                    if not valid:
                        break
            if not valid:
                break
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()
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
        grid = data[idx:idx+n]
        idx += n
        
        # Check if the grid is valid
        valid = True
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '1':
                    # Check if it's on the first row or first column
                    if i == 0 and j == 0:
                        valid = False
                        break
                    if i == 0:
                        # It must be reachable from the first row cannons
                        # Check if there is a 1 in the same column below it
                        found = False
                        for k in range(1, n):
                            if grid[k][j] == '1':
                                found = True
                                break
                        if not found:
                            valid = False
                            break
                    if j == 0:
                        # It must be reachable from the first column cannons
                        # Check if there is a 1 in the same row to the right of it
                        found = False
                        for k in range(1, n):
                            if grid[i][k] == '1':
                                found = True
                                break
                        if not found:
                            valid = False
                            break
            if not valid:
                break
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))
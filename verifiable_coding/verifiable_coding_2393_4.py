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
        matrix = []
        for i in range(n):
            row = data[idx]
            matrix.append(row)
            idx += 1
        
        # Check if the matrix is valid
        valid = True
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == '1':
                    # Check if it's possible for this 1 to be placed by a cannon
                    # It must be reachable from the first row or first column
                    # Also, it must not be blocked by any other 1 in its path
                    # Check if it's in the first row or first column
                    if i == 0 or j == 0:
                        # Check if there's a path from the first row or column to this cell
                        # without any other 1 blocking
                        # Check from first row
                        blocked = False
                        for k in range(n):
                            if matrix[0][k] == '1' and k < j:
                                blocked = True
                                break
                        if not blocked:
                            # Check from first column
                            blocked = False
                            for k in range(n):
                                if matrix[k][0] == '1' and k < i:
                                    blocked = True
                                    break
                        if not blocked:
                            valid = False
                    else:
                        # Check if it's reachable from first row or column
                        # Check from first row
                        blocked = False
                        for k in range(n):
                            if matrix[0][k] == '1' and k < j:
                                blocked = True
                                break
                        if not blocked:
                            # Check from first column
                            blocked = False
                            for k in range(n):
                                if matrix[k][0] == '1' and k < i:
                                    blocked = True
                                    break
                        if not blocked:
                            valid = False
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))
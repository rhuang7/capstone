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
        for _ in range(n):
            row = data[idx]
            matrix.append(row)
            idx += 1
        
        # Check if the matrix is valid
        valid = True
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == '1':
                    # Check if it can be reached by a cannon shot
                    # Check if it's on the first row or first column
                    if i == 0 or j == 0:
                        # It can be shot by a cannon
                        continue
                    # Check if there is a 1 in the same row to the left or same column above
                    # If not, then it's invalid
                    has_left = False
                    has_above = False
                    for k in range(j):
                        if matrix[i][k] == '1':
                            has_left = True
                            break
                    for k in range(i):
                        if matrix[k][j] == '1':
                            has_above = True
                            break
                    if not has_left and not has_above:
                        valid = False
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
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
        
        valid = True
        # Check if any 1 is in a position that cannot be reached by any cannon
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == '1':
                    # Check if it's in the first row or first column
                    if i == 0 or j == 0:
                        # It can be shot from a cannon
                        continue
                    # Check if it's blocked by a 1 in the same row or column
                    # Check row i
                    blocked = False
                    for k in range(1, n):
                        if matrix[i][k] == '1':
                            blocked = True
                            break
                    if not blocked:
                        valid = False
                        break
                    # Check column j
                    blocked = False
                    for k in range(1, n):
                        if matrix[k][j] == '1':
                            blocked = True
                            break
                    if not blocked:
                        valid = False
                        break
            if not valid:
                break
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
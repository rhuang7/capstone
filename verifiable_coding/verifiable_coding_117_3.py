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
        m = int(data[idx+1])
        idx += 2
        
        rows = []
        for _ in range(n):
            row = list(map(int, data[idx:idx+m]))
            rows.append(row)
            idx += m
        
        cols = []
        for _ in range(m):
            col = list(map(int, data[idx:idx+n]))
            cols.append(col)
            idx += n
        
        # Create a set of all elements
        all_elements = set()
        for row in rows:
            all_elements.update(row)
        all_elements = sorted(all_elements)
        
        # Create a dictionary to map value to its position
        value_to_pos = {}
        for i in range(n):
            for j in range(m):
                value_to_pos[rows[i][j]] = (i, j)
        
        # Create a matrix to store the result
        matrix = [[0]*m for _ in range(n)]
        
        # Fill the matrix
        for val in all_elements:
            i, j = value_to_pos[val]
            matrix[i][j] = val
        
        # Output the matrix
        for row in matrix:
            results.append(' '.join(map(str, row)) + ' ')
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index+1])
        a = int(data[index+2])
        b = int(data[index+3])
        index += 4
        
        # Check if it's possible to construct the matrix
        if (n * a) % m != 0 or (m * b) % n != 0:
            results.append("NO")
            continue
        
        # Check if the total number of ones is consistent
        total_ones = n * a
        if total_ones != m * b:
            results.append("NO")
            continue
        
        # Construct the matrix
        matrix = [[0] * m for _ in range(n)]
        row = 0
        col = 0
        
        for i in range(n):
            # Place a ones in the current row
            for j in range(a):
                if col >= m:
                    col = 0
                matrix[i][col] = 1
                col += 1
            row += 1
        
        # Check if the column counts are correct
        valid = True
        for j in range(m):
            count = 0
            for i in range(n):
                if matrix[i][j] == 1:
                    count += 1
            if count != b:
                valid = False
                break
        
        if not valid:
            results.append("NO")
            continue
        
        results.append("YES")
        for row in matrix:
            results.append(''.join(map(str, row)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
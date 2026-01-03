import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        a = int(data[idx+2])
        b = int(data[idx+3])
        idx += 4
        
        # Check if the total number of ones is consistent
        total_ones = n * a
        if total_ones % m != 0:
            print("NO")
            continue
        if total_ones != m * b:
            print("NO")
            continue
        
        # Check if it's possible to distribute the ones
        if (n * a) % m != 0 or (m * b) % n != 0:
            print("NO")
            continue
        
        # Check if the required conditions are met
        if a == 0 or b == 0:
            print("NO")
            continue
        
        # Check if the required number of ones per row and column is possible
        if (n * a) % m != 0 or (m * b) % n != 0:
            print("NO")
            continue
        
        # Create the matrix
        matrix = []
        for i in range(n):
            row = ['0'] * m
            for j in range(a):
                row[i * a + j] = '1'
            matrix.append(''.join(row))
        
        # Check if the column counts are correct
        col_counts = [0] * m
        for i in range(n):
            for j in range(m):
                col_counts[j] += int(matrix[i][j])
        
        # If column counts are not correct, try a different arrangement
        if any(count != b for count in col_counts):
            print("NO")
            continue
        
        print("YES")
        for row in matrix:
            print(row)
    
if __name__ == '__main__':
    solve()
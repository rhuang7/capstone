import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        n = int(data[index])
        m = int(data[index+1])
        a = int(data[index+2])
        b = int(data[index+3])
        index += 4
        
        # Check if the total number of ones is consistent
        total_ones = n * a
        if total_ones % m != 0:
            print("NO")
            continue
        if total_ones != m * b:
            print("NO")
            continue
        
        # Check if the conditions are possible
        if (n * a) % m != 0 or (m * b) % n != 0:
            print("NO")
            continue
        
        # Check if the row and column constraints are possible
        if a > m or b > n:
            print("NO")
            continue
        
        # Create the matrix
        matrix = [[0] * m for _ in range(n)]
        row = 0
        col = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                    row += 1
                    col += 1
                    if row == a:
                        row = 0
                        col = 0
                    if col == m:
                        col = 0
        # Check if the matrix meets the conditions
        valid = True
        for i in range(n):
            if sum(matrix[i]) != a:
                valid = False
                break
        for j in range(m):
            col_sum = 0
            for i in range(n):
                col_sum += matrix[i][j]
            if col_sum != b:
                valid = False
                break
        if not valid:
            print("NO")
        else:
            print("YES")
            for row in matrix:
                print(''.join(map(str, row)))
                
if __name__ == '__main__':
    solve()
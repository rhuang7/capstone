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
        
        # Check if it's possible to construct the matrix
        if (n * a) % m != 0 or (m * b) % n != 0:
            print("NO")
            continue
        
        # Check if the total number of ones is the same
        total_ones = n * a
        if total_ones != m * b:
            print("NO")
            continue
        
        # Construct the matrix
        matrix = [[0] * m for _ in range(n)]
        row = 0
        col = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if row < n and col < m:
                        matrix[i][j] = 1
                        row += 1
                        if row == n:
                            row = 0
                            col += 1
                        else:
                            col = 0
                    else:
                        break
                else:
                    col += 1
                    if col == m:
                        col = 0
        
        # Check if the constructed matrix satisfies the conditions
        valid = True
        for i in range(n):
            if sum(matrix[i]) != a:
                valid = False
                break
        for j in range(m):
            total = 0
            for i in range(n):
                total += matrix[i][j]
            if total != b:
                valid = False
                break
        
        if valid:
            print("YES")
            for row in matrix:
                print(''.join(map(str, row)))
        else:
            print("NO")

if __name__ == '__main__':
    solve()
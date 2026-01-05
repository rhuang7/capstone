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
        
        # Check if the total number of ones is consistent
        total_ones = n * a
        if total_ones != m * b:
            print("NO")
            continue
        
        # Construct the matrix
        matrix = []
        for i in range(n):
            row = ['0'] * m
            # Place a ones in the row
            for j in range(a):
                # Distribute the ones evenly across columns
                col = (i * a + j) % m
                row[col] = '1'
            matrix.append(''.join(row))
        
        # Check if the column constraints are satisfied
        valid = True
        for j in range(m):
            count = 0
            for i in range(n):
                if matrix[i][j] == '1':
                    count += 1
            if count != b:
                valid = False
                break
        
        if valid:
            print("YES")
            for row in matrix:
                print(row)
        else:
            print("NO")

if __name__ == '__main__':
    solve()
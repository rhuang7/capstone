import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    p = int(data[2])
    
    commands = []
    index = 3
    for _ in range(p):
        i = int(data[index])
        j = int(data[index+1])
        commands.append((i, j))
        index += 2
    
    # Initialize matrix
    matrix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = j + 1  # 1-based index
    
    # Apply commands
    for i, j in commands:
        matrix[i-1][j-1] += 1
    
    # Process each row
    result = []
    for i in range(n):
        row = matrix[i]
        total = 0
        valid = True
        for j in range(m-1, 0, -1):
            if row[j] < row[j-1]:
                valid = False
                break
            total += row[j] - row[j-1]
        if valid:
            result.append(str(total))
        else:
            result.append("-1")
    
    print("\n".join(result))

if __name__ == '__main__':
    solve()
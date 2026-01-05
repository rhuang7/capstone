import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    p = int(data[2])
    
    commands = data[3:]
    
    # Initialize the matrix
    # Since m can be up to 1e5 and n up to 1e5, we can't store the full matrix
    # Instead, we'll track the number of increments for each (i, j)
    # We'll use a list of dictionaries to track the increments for each row
    increments = [{} for _ in range(n)]
    
    idx = 3
    for _ in range(p):
        i = int(commands[idx]) - 1  # 0-based index
        j = int(commands[idx + 1]) - 1
        increments[i][j] = increments[i].get(j, 0) + 1
        idx += 2
    
    # For each row, compute the answer
    for i in range(n):
        # Initialize the current value for each column
        # Initially, each a_ij = j (1-based), so for 0-based it's j+1
        # But we'll track the value as j+1 + increments[i].get(j, 0)
        # We'll compute the values from right to left
        # We'll also track the previous value to compute the cost
        prev = 0
        total = 0
        for j in range(m - 1, -1, -1):
            current = (j + 1) + increments[i].get(j, 0)
            if j == m - 1:
                prev = current
                continue
            if current < prev:
                print(-1)
                break
            total += prev - current
            prev = current
        else:
            print(total)
    
if __name__ == '__main__':
    solve()
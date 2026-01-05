import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    L = int(data[idx])
    idx += 1
    R = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1

    grid = []
    for _ in range(L):
        row = data[idx]
        idx += 1
        grid.append(row)

    queries = []
    for _ in range(Q):
        K = int(data[idx])
        idx += 1
        c = data[idx]
        idx += 1
        queries.append((K, c))

    # Precompute prefix sums for rows
    prefix = [[0]*(R+1) for _ in range(L)]
    for i in range(L):
        for j in range(R):
            prefix[i][j+1] = prefix[i][j] + (1 if grid[i][j] == 'M' else 0)

    # Precompute prefix sums for columns
    col_prefix = [[0]*(L+1) for _ in range(R)]
    for j in range(R):
        for i in range(L):
            col_prefix[j][i+1] = col_prefix[j][i] + (1 if grid[i][j] == 'M' else 0)

    # Function to check if there is a KxK submatrix with all M or all F
    def check(K, c):
        if K > L or K > R:
            return False
        if c == 'M':
            target = 1
        else:
            target = 0
        for i in range(L - K + 1):
            for j in range(R - K + 1):
                # Calculate sum of KxK submatrix using prefix sums
                sum_ = 0
                for x in range(K):
                    sum_ += (prefix[i+x][j+K] - prefix[i+x][j])
                for y in range(K):
                    sum_ += (col_prefix[j+y][i+K] - col_prefix[j+y][i])
                # Subtract overlapping parts
                sum_ -= (prefix[i+K][j+K] - prefix[i+K][j]) + (prefix[i+K][j+K] - prefix[i][j+K]) - (prefix[i+K][j+K] - prefix[i][j])
                if sum_ == K*K * target:
                    return True
        return False

    output = []
    for K, c in queries:
        if check(K, c):
            output.append("yes")
        else:
            output.append("no")

    print("\n".join(output))

if __name__ == '__main__':
    solve()
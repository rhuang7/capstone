import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    L = int(data[idx]); idx +=1
    R = int(data[idx]); idx +=1
    Q = int(data[idx]); idx +=1

    grid = []
    for _ in range(L):
        row = data[idx]
        grid.append(row)
        idx +=1

    queries = []
    for _ in range(Q):
        K = int(data[idx])
        c = data[idx+1]
        queries.append((K, c))
        idx +=2

    # Precompute prefix sums for rows
    prefix = [[0]*(R+1) for _ in range(L+1)]
    for i in range(L):
        for j in range(R):
            prefix[i+1][j+1] = prefix[i][j+1] + (1 if grid[i][j] == 'M' else 0)
    # Precompute prefix sums for columns
    col_prefix = [[0]*(L+1) for _ in range(R+1)]
    for j in range(R):
        for i in range(L):
            col_prefix[j+1][i+1] = col_prefix[j][i+1] + (1 if grid[i][j] == 'M' else 0)

    def is_all(c, K):
        if K > min(L, R):
            return False
        for i in range(L - K + 1):
            for j in range(R - K + 1):
                # Check if KxK submatrix starting at (i,j) is all c
                # Using row prefix sums
                row_sum = prefix[i+K][j+K] - prefix[i][j+K] - (prefix[i+K][j] - prefix[i][j])
                if c == 'M':
                    if row_sum == K*K:
                        return True
                else:
                    if row_sum == 0:
                        return True
        return False

    output = []
    for K, c in queries:
        if is_all(c, K):
            output.append("yes")
        else:
            output.append("no")

    print("\n".join(output))

if __name__ == '__main__':
    solve()
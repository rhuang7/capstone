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
        if K > min(L, R):
            return "no"
        if c == 'M':
            target = 1
        else:
            target = 0
        for i in range(L - K + 1):
            for j in range(R - K + 1):
                # Calculate the sum of the KxK submatrix
                sum_val = 0
                for x in range(K):
                    sum_val += prefix[i+x][j+K] - prefix[i+x][j]
                for y in range(K):
                    sum_val += col_prefix[j+y][i+K] - col_prefix[j+y][i]
                # Subtract the overlapping parts
                sum_val -= (prefix[i+K][j+K] - prefix[i][j+K]) + (prefix[i+K][j] - prefix[i][j]) - prefix[i+K][j]
                if sum_val == K*K * target:
                    return "yes"
        return "no"
    
    for K, c in queries:
        print(check(K, c))

if __name__ == '__main__':
    solve()
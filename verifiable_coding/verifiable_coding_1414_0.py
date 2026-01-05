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
        grid.append(row)
        idx += 1
    
    queries = []
    for _ in range(Q):
        K = int(data[idx])
        idx += 1
        c = data[idx]
        idx += 1
        queries.append((K, c))
    
    # Preprocess prefix sums for M and F
    prefix_m = [[0]*(R+1) for _ in range(L+1)]
    prefix_f = [[0]*(R+1) for _ in range(L+1)]
    
    for i in range(1, L+1):
        for j in range(1, R+1):
            prefix_m[i][j] = prefix_m[i-1][j] + prefix_m[i][j-1] - prefix_m[i-1][j-1] + (1 if grid[i-1][j-1] == 'M' else 0)
            prefix_f[i][j] = prefix_f[i-1][j] + prefix_f[i][j-1] - prefix_f[i-1][j-1] + (1 if grid[i-1][j-1] == 'F' else 0)
    
    def is_valid(k, c):
        if k > L or k > R:
            return False
        for i in range(1, L - k + 2):
            for j in range(1, R - k + 2):
                if c == 'M':
                    total = prefix_m[i+k-1][j+k-1] - prefix_m[i-1][j+k-1] - prefix_m[i+k-1][j-1] + prefix_m[i-1][j-1]
                    if total == k*k:
                        return True
                else:
                    total = prefix_f[i+k-1][j+k-1] - prefix_f[i-1][j+k-1] - prefix_f[i+k-1][j-1] + prefix_f[i-1][j-1]
                    if total == k*k:
                        return True
        return False
    
    for k, c in queries:
        if is_valid(k, c):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()
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

    # Preprocess prefix sums for M and F
    prefix_m = [[0]*(R+1) for _ in range(L+1)]
    prefix_f = [[0]*(R+1) for _ in range(L+1)]

    for i in range(1, L+1):
        for j in range(1, R+1):
            prefix_m[i][j] = prefix_m[i-1][j] + prefix_m[i][j-1] - prefix_m[i-1][j-1] + (1 if grid[i-1][j-1] == 'M' else 0)
            prefix_f[i][j] = prefix_f[i-1][j] + prefix_f[i][j-1] - prefix_f[i-1][j-1] + (1 if grid[i-1][j-1] == 'F' else 0)

    def is_possible(K, c):
        if K > L or K > R:
            return False
        for i in range(1, L - K + 2):
            for j in range(1, R - K + 2):
                if c == 'M':
                    total = prefix_m[i+K-1][j+K-1] - prefix_m[i-1][j+K-1] - prefix_m[i+K-1][j-1] + prefix_m[i-1][j-1]
                    if total == K*K:
                        return True
                else:
                    total = prefix_f[i+K-1][j+K-1] - prefix_f[i-1][j+K-1] - prefix_f[i+K-1][j-1] + prefix_f[i-1][j-1]
                    if total == K*K:
                        return True
        return False

    for K, c in queries:
        if is_possible(K, c):
            print("yes")
        else:
            print("no")

if __name__ == '__main__':
    solve()
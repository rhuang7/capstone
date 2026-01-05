import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        X = int(input[idx])
        Y = int(input[idx+1])
        Z = int(input[idx+2])
        idx += 3
        B = []
        for i in range(X):
            row = []
            for j in range(Y):
                line = list(map(int, input[idx:idx+Z]))
                row.extend(line)
                idx += Z
            B.append(row)
        A = [[ [0]*Z for _ in range(Y) ] for _ in range(X) ]
        for i in range(X):
            for j in range(Y):
                for k in range(Z):
                    if i == 0 and j == 0 and k == 0:
                        A[i][j][k] = B[i][j][k]
                    else:
                        A[i][j][k] = B[i][j][k] - (B[i-1][j][k] if i > 0 else 0) - (B[i][j-1][k] if j > 0 else 0) - (B[i][j][k-1] if k > 0 else 0) + (B[i-1][j-1][k] if i > 0 and j > 0 else 0) + (B[i-1][j][k-1] if i > 0 and k > 0 else 0) + (B[i][j-1][k-1] if j > 0 and k > 0 else 0) - (B[i-1][j-1][k-1] if i > 0 and j > 0 and k > 0 else 0)
        for i in range(X):
            for j in range(Y):
                print(' '.join(map(str, A[i][j])))
        if _ != T - 1:
            print()

if __name__ == '__main__':
    solve()
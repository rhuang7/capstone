import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        X = int(input[ptr])
        Y = int(input[ptr+1])
        Z = int(input[ptr+2])
        ptr += 3
        B = []
        for i in range(X):
            row = []
            for j in range(Y):
                line = list(map(int, input[ptr:ptr+Z]))
                ptr += Z
                row.extend(line)
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
                for k in range(Z):
                    print(A[i][j][k])
                    if k == Z-1:
                        print()
        if X > 0 and Y > 0 and Z > 0:
            print()

if __name__ == '__main__':
    solve()
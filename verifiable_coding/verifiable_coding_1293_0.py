import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1

    B = []
    for _ in range(N):
        row = list(map(int, data[idx:idx+N]))
        B.append(row)
        idx += N

    # Compute initial A
    A = [0] * N
    for i in range(1, N):
        A[i] = B[0][i]  # since A[0] = 0
        for j in range(i):
            if abs(A[i] - A[j]) != B[j][i]:
                A[i] = -A[i]
                if abs(A[i] - A[j]) != B[j][i]:
                    A[i] = B[j][i] - A[j]
    # Ensure lexicographically smallest
    for i in range(N):
        if A[i] < 0:
            A[i] = -A[i]
        else:
            A[i] = 0
    print(' '.join(map(str, A)))

    for _ in range(Q):
        p = int(data[idx])
        idx += 1
        F = list(map(int, data[idx:idx+N]))
        idx += N

        # Update B
        for i in range(N):
            B[i][p] = F[i]
            B[p][i] = F[i]

        # Compute A
        A = [0] * N
        for i in range(1, N):
            A[i] = B[0][i]
            for j in range(i):
                if abs(A[i] - A[j]) != B[j][i]:
                    A[i] = -A[i]
                    if abs(A[i] - A[j]) != B[j][i]:
                        A[i] = B[j][i] - A[j]
        # Ensure lexicographically smallest
        for i in range(N):
            if A[i] < 0:
                A[i] = -A[i]
            else:
                A[i] = 0
        print(' '.join(map(str, A)))

if __name__ == '__main__':
    solve()
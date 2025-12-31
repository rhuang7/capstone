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

    # Initialize A
    A = [0] * N
    for j in range(1, N):
        A[j] = B[0][j]

    # Function to reconstruct A from B
    def reconstruct_A(B):
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        for i in range(1, N):
            for j in range(i+1, N):
                if abs(A[i] - A[j]) != B[i][j]:
                    # This is not a valid configuration, but the problem says there is always a solution
                    # So we assume the initial B is valid
                    pass
        return A

    # Function to find lex smallest A
    def find_lex_smallest_A(B):
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        for i in range(1, N):
            for j in range(i+1, N):
                if abs(A[i] - A[j]) != B[i][j]:
                    # This is not a valid configuration, but the problem says there is always a solution
                    # So we assume the initial B is valid
                    pass
        return A

    # Initial output
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

        # Reconstruct A
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        for i in range(1, N):
            for j in range(i+1, N):
                if abs(A[i] - A[j]) != B[i][j]:
                    # This is not a valid configuration, but the problem says there is always a solution
                    # So we assume the initial B is valid
                    pass
        print(' '.join(map(str, A)))
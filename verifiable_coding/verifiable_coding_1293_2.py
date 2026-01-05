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

    # Function to compute A from B
    def compute_A(B):
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        return A

    # Function to check if A is valid for B
    def is_valid(A, B):
        for i in range(N):
            for j in range(N):
                if abs(A[i] - A[j]) != B[i][j]:
                    return False
        return True

    # Function to find lex smallest A
    def find_lex_smallest_A(B):
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        for j in range(1, N):
            for i in range(j):
                if abs(A[i] - A[j]) != B[i][j]:
                    A[j] = B[i][j] - A[i]
        return A

    # Initial A
    A = find_lex_smallest_A(B)

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

        # Compute new A
        A = find_lex_smallest_A(B)

        print(' '.join(map(str, A)))

if __name__ == '__main__':
    solve()
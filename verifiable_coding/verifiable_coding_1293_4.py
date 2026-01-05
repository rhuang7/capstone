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

    # Function to find lexicographically smallest A
    def find_lex_smallest_A(B):
        A = [0] * N
        for j in range(1, N):
            A[j] = B[0][j]
        # Try to find a lexicographically smaller A
        for j in range(1, N):
            for k in range(j, N):
                # Try to adjust A[k] to make A lex smaller
                # We need to find a value for A[k] such that A[k] - A[j] = B[j][k]
                # A[k] = A[j] + B[j][k]
                # But we need to find a value that makes A lex smaller
                # Try to find a value for A[k] that is smaller than current A[k]
                # and satisfies the condition
                # We can try to set A[k] = A[j] - B[j][k]
                # and check if it's valid
                new_A = A.copy()
                new_A[k] = A[j] - B[j][k]
                if is_valid(new_A, B):
                    A = new_A
                    break
            else:
                continue
            break
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
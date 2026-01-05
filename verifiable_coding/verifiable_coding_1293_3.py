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
        idx += N
        B.append(row)

    # Compute initial A
    A = [0] * N
    for j in range(1, N):
        A[j] = B[0][j]  # since A[0] = 0

    # Check if A is valid
    valid = True
    for i in range(N):
        for j in range(N):
            if abs(A[i] - A[j]) != B[i][j]:
                valid = False
                break
        if not valid:
            break

    # If not valid, find lexicographically smallest A
    if not valid:
        # We need to find A such that A[0] = 0 and B[i][j] = |A[i] - A[j]|
        # We can use the fact that A[i] = A[0] + B[0][i] if B[0][i] is positive
        # But since B[0][i] = |A[i] - A[0]| = |A[i] - 0| = |A[i]|
        # So A[i] can be B[0][i] or -B[0][i], but we want the lex smallest
        # So we choose A[i] = -B[0][i] for i > 0
        A = [0] * N
        for j in range(1, N):
            A[j] = -B[0][j]

    # Function to check if A is valid
    def is_valid(A):
        for i in range(N):
            for j in range(N):
                if abs(A[i] - A[j]) != B[i][j]:
                    return False
        return True

    # Function to find lex smallest A
    def find_lex_smallest_A():
        A = [0] * N
        for j in range(1, N):
            A[j] = -B[0][j]
        return A

    # Initial output
    print(' '.join(map(str, A)))

    # Process queries
    for _ in range(Q):
        p = int(data[idx])
        idx += 1
        F = list(map(int, data[idx:idx+N]))
        idx += N

        # Update B
        for i in range(N):
            B[i][p] = F[i]
            B[p][i] = F[i]

        # Find new A
        A = [0] * N
        for j in range(1, N):
            A[j] = -B[0][j]

        # Check if valid
        if not is_valid(A):
            A = find_lex_smallest_A()

        print(' '.join(map(str, A)))

if __name__ == '__main__':
    solve()
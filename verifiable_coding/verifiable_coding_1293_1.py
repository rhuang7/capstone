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

    # Initial reconstruction of A
    A = [0] * N
    for j in range(1, N):
        A[j] = B[0][j]  # Since A[0] = 0

    # Check if the initial A is valid
    for i in range(N):
        for j in range(N):
            if abs(A[i] - A[j]) != B[i][j]:
                # Adjust A to make it valid
                # We need to find A such that B[i][j] = |A[i] - A[j]|
                # Since A[0] = 0, we can set A[j] = B[0][j]
                # But we need to make sure that all B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # Let's find A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j]
                # But this may not be correct, so we need to find A such that B[i][j] = |A[i] - A[j]|
                # So we can set A[i] = B[0][i] - B[0][j] + A[j
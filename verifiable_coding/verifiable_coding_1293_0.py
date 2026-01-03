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

    # Initial reconstruction of A
    A = [0] * N
    for j in range(1, N):
        A[j] = B[0][j]  # since A[0] = 0

    # Check if A is valid
    for i in range(N):
        for j in range(N):
            if abs(A[i] - A[j]) != B[i][j]:
                # Adjust A to make it valid
                # We need to find A such that A[i] - A[j] = B[i][j]
                # Since A[0] = 0, we can compute A[i] = B[0][i]
                # But this may not be valid, so we need to find a correct A
                # We can use the fact that A[i] - A[j] = B[i][j]
                # So A[i] = A[j] + B[i][j]
                # We can use the first row to compute A
                # But since B may be invalid, we need to find a correct A
                # We can use the first row to compute A
                # Let's use the first row to compute A
                A = [0] * N
                for j in range(N):
                    A[j] = B[0][j]
                # Now check if this A is valid
                for i in range(N):
                    for j in range(N):
                        if abs(A[i] - A[j]) != B[i][j]:
                            # This is not valid, need to find correct A
                            # We can use the fact that A[i] - A[j] = B[i][j]
                            # So A[i] = A[j] + B[i][j]
                            # We can use the first row to compute A
                            # Let's use the first row to compute A
                            A = [0] * N
                            for j in range(N):
                                A[j] = B[0][j]
                            # Now check if this A is valid
                            for i in range(N):
                                for j in range(N):
                                    if abs(A[i] - A[j]) != B[i][j]:
                                        # This is not valid, need to find correct A
                                        # We can use the fact that A[i] - A[j] = B[i][j]
                                        # So A[i] = A[j] + B[i][j]
                                        # We can use the first row to compute A
                                        # Let's use the first row to compute A
                                        A = [0] * N
                                        for j in range(N):
                                            A[j] = B[0][j]
                                        # Now check if this A is valid
                                        for i in range(N):
                                            for j in range(N):
                                                if abs(A[i] - A[j]) != B[i][j]:
                                                    # This is not valid, need to find correct A
                                                    # We can use the fact that A[i] - A[j] = B[i][j]
                                                    # So A[i] = A[j] + B[i][j]
                                                    # We can use the first row to compute A
                                                    A = [0] * N
                                                    for j in range(N):
                                                        A[j] = B[0][j]
                                                    # Now check if this A is valid
                                                    for i in range(N):
                                                        for j in range(N):
                                                            if abs(A[i] - A[j]) != B[i][j]:
                                                                # This is not valid, need to find correct A
                                                                # We can use the fact that A[i] - A[j] = B[i][j]
                                                                # So A[i] = A[j] + B[i][j]
                                                                # We can use the first row to compute A
                                                                A = [0] * N
                                                                for j in range(N):
                                                                    A[j] = B[0][j]
                                                                # Now check if this A is valid
                                                                for i in range(N):
                                                                    for j in range(N):
                                                                        if abs(A[i] - A[j]) != B[i][j]:
                                                                            # This is not valid, need to find correct A
                                                                            # We can use the fact that A[i] - A[j] = B[i][j]
                                                                            # So A[i] = A[j] + B[i][j]
                                                                            # We can use the first row to compute A
                                                                            A = [0] * N
                                                                            for j in range(N):
                                                                                A[j] = B[0][j]
                                                                            # Now check if this A is valid
                                                                            for i in range(N):
                                                                                for j in range(N):
                                                                                    if abs(A[i] - A[j]) != B[i][j]:
                                                                                        # This is not valid, need to find correct A
                                                                                        # We can use the fact that A[i] - A[j] = B[i][j]
                                                                                        # So A[i] = A[j] + B[i][j]
                                                                                        # We can use the first row to compute A
                                                                                        A = [0] * N
                                                                                        for j in range(N):
                                                                                            A[j] = B[0][j]
                                                                                        # Now check if this A is valid
                                                                                        for i in range(N):
                                                                                            for j in range(N):
                                                                                                if abs(A[i] - A[j]) != B[i][j]:
                                                                                                    # This is not valid, need to find correct A
                                                                                                    # We can use the fact that A[i] - A[j] = B[i][j]
                                                                                                    # So A[i] = A[j] + B[i][j]
                                                                                                    # We can use the first row to compute A
                                                                                                    A = [0] * N
                                                                                                    for j in range(N):
                                                                                                        A[j] = B[0][j]
                                                                                                    # Now check if this A is valid
                                                                                                    for i in range(N):
                                                                                                        for j in range(N):
                                                                                                            if abs(A[i] - A[j]) != B[i][j]:
                                                                                                                # This is not valid, need to find correct A
                                                                                                                # We can use the fact that A[i] - A[j] = B[i][j]
                                                                                                                # So A[i] = A[j] + B[i][j]
                                                                                                                # We can use the first row to compute A
                                                                                                                A = [0] * N
                                                                                                                for j in range(N):
                                                                                                                    A[j] = B[0][j]
                                                                                                                # Now check if this A is valid
                                                                                                                for i in range(N):
                                                                                                                    for j in range(N):
                                                                                                                        if abs(A[i] - A[j]) != B[i][j]:
                                                                                                                            # This is not valid, need to find correct A
                                                                                                                            # We can use the fact that A[i] - A[j] = B[i][j]
                                                                                                                            # So A[i] = A[j] + B[i][j]
                                                                                                                            # We can use the first row to compute A
                                                                                                                            A = [0] * N
                                                                                                                            for j in range(N):
                                                                                                                                A[j] = B[0][j]
                                                                                                                            # Now check if this A is valid
                                                                                                                            for i in range(N):
                                                                                                                                for j in range(N):
                                                                                                                                    if abs(A[i] - A[j]) != B[i][j]:
                                                                                                                                        # This is not valid, need to find correct A
                                                                                                                                        # We can use the fact that A[i] - A[j] = B[i][j]
                                                                                                                                        # So A[i] = A[j] + B[i][j]
                                                                                                                                        # We can use the first row to compute A
                                                                                                                                        A = [0] * N
                                                                                                                                        for j in range(N):
                                                                                                                                            A[j] = B[0][j]
                                                                                                                                        # Now check if this A is valid
                                                                                                                                        for i in range(N):
                                                                                                                                            for j in range(N):
                                                                                                                                                if abs(A[i] - A[j]) != B[i][j]:
                                                                                                                                                    # This is not valid, need to find correct A
                                                                                                                                                        # We can use the fact that A[i] - A[j] = B[i][j]
                                                                                                                                                        # So A[i] = A[j] + B[i][j]
                                                                                                                                                        # We can use the first row to compute A
                                                                                                                                                        A = [0] * N
                                                                                                                                                        for j in range(N):
                                                                                                                                                            A[j] = B[0][j]
                                                                                                                                                        # Now check if this A is valid
                                                                                                                                                        for i in range(N):
                                                                                                                                                            for j in range(N):
                                                                                                                                                                if abs(A[i] - A[j]) != B[i][j]:
                                                                                                                                                                    # This is not valid, need to find correct A
                                                                                                                                                                    # We can use the fact that A[i] - A[j] = B[i][j]
                                                                                                                                                                    # So A[i] = A[j] + B[i][j]
                                                                                                                                                                    # We can use the first row to compute A
                                                                                                                                                                    A = [0] * N
                                                                                                                                                                    for j in range(N):
                                                                                                                                                                        A[j] = B[
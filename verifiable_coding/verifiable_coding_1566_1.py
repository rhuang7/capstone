import sys
import math
from collections import defaultdict

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        Q = int(data[idx+1])
        idx += 2
        filled = defaultdict(dict)
        for __ in range(Q):
            i = int(data[idx]) - 1
            j = int(data[idx+1]) - 1
            val = int(data[idx+2])
            idx += 3
            filled[i][j] = val
            filled[j][i] = val
        # Check for contradictions
        valid = True
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if (i, j) in filled:
                    val = filled[i][j]
                    if (j, i) in filled:
                        if filled[j][i] != val:
                            valid = False
                            break
                    else:
                        # We need to check if it's possible to fill it
                        # For the matrix to be good, B[i][j] = |A[i] - A[j]|
                        # So B[i][j] must be equal to B[j][i]
                        # So if B[i][j] is 0 or 1, we need to check if it's possible
                        # to have B[j][i] = val
                        # For this, we can assume that B[j][i] = val
                        # But we need to check if this is consistent with other constraints
                        pass
                else:
                    # We can fill it with any value, but we need to ensure that it's consistent
                    # with the existing values
                    pass
        if not valid:
            results.append("no")
            continue
        # Check for consistency
        # We can assign A[0] = 0, and then assign A[i] = B[0][i]
        # Then check if all values are consistent
        A = [0] * N
        for i in range(N):
            if i == 0:
                continue
            if (0, i) in filled:
                val = filled[0][i]
                A[i] = val
            else:
                # We can assign A[i] = 0 or any value, but we need to check consistency
                # For this problem, we can assume that A[i] = 0
                A[i] = 0
        # Check all filled values
        valid = True
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if (i, j) in filled:
                    val = filled[i][j]
                    if val != abs(A[i] - A[j]):
                        valid = False
                        break
            if not valid:
                break
        if valid:
            results.append("yes")
        else:
            results.append("no")
    print("\n".join(results))

if __name__ == '__main__':
    solve()
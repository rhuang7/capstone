import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        if N % 2 != 0:
            results.append("NO")
            continue
        opposite = [0] * N
        for i in range(N):
            j = (i + N // 2) % N
            opposite[i] = j
        valid = True
        for i in range(N):
            if A[i] != -1:
                j = opposite[i]
                if A[j] != -1 and A[i] != A[j]:
                    valid = False
                    break
        if not valid:
            results.append("NO")
            continue
        B = [0] * N
        for i in range(N):
            if A[i] == -1:
                j = opposite[i]
                if B[j] == 0:
                    B[i] = 1
                else:
                    B[i] = B[j]
            else:
                B[i] = A[i]
        total = sum(B)
        if total == 0:
            results.append("NO")
            continue
        results.append("YES")
        results.append(' '.join(map(str, B)))
    print('\n'.join(results))
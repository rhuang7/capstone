import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N
    
    # Preprocess for each position, the next higher position within 100 distance
    next_higher = [0] * (N + 2)  # 1-based indexing
    for i in range(N):
        j = i + 1
        while j <= min(i + 100, N):
            if A[j] > A[i]:
                next_higher[i] = j
                break
            j += 1
    
    def update_range(L, R, X):
        for i in range(L, R + 1):
            A[i] += X
    
    def query(i, k):
        current = i
        for _ in range(k):
            if next_higher[current] == 0:
                return current
            current = next_higher[current]
        return current
    
    output = []
    for _ in range(Q):
        op = int(data[idx])
        idx += 1
        if op == 1:
            i = int(data[idx]) - 1  # 0-based
            idx += 1
            k = int(data[idx])
            idx += 1
            res = query(i, k)
            output.append(str(res + 1))
        else:
            L = int(data[idx]) - 1
            idx += 1
            R = int(data[idx]) - 1
            idx += 1
            X = int(data[idx])
            idx += 1
            update_range(L, R, X)
    
    print('\n'.join(output))
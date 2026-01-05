import sys

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
        inversions = 0
        local = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    inversions += 1
        for i in range(N-1):
            if A[i] > A[i+1]:
                local += 1
        if inversions == local:
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))
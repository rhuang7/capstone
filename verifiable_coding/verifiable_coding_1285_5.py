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
        matrix = []
        for _ in range(N):
            row = list(map(int, data[idx:idx+N]))
            matrix.append(row)
            idx += N
        max_trace = 0
        for l in range(1, N+1):
            for i in range(N - l + 1):
                for j in range(N - l + 1):
                    trace = 0
                    for k in range(l):
                        trace += matrix[i + k][j + k]
                    if trace > max_trace:
                        max_trace = trace
        results.append(str(max_trace))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
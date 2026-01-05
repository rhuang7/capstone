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
        res = [1] * N
        for i in range(N-2, -1, -1):
            if (A[i] > 0 and A[i+1] < 0) or (A[i] < 0 and A[i+1] > 0):
                res[i] = res[i+1] + 1
        results.append(' '.join(map(str, res)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
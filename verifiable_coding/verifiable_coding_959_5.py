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
        A = list(map(int, data[idx:idx + N]))
        idx += N
        A.sort()
        max_sum = 0
        for i in range(0, N, 2):
            max_sum += abs(A[i] - A[i + 1])
        results.append(str(max_sum))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
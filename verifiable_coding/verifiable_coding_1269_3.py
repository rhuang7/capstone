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
        B = list(map(int, data[idx:idx+N]))
        idx += N
        A.sort()
        B.sort()
        S = 0
        for i in range(N):
            S += 2 * min(A[i], B[i])
        results.append(S)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
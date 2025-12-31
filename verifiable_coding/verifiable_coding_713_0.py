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
        M = int(data[idx])
        idx += 1
        B = list(map(int, data[idx:idx+M]))
        idx += M
        # Check if B is a subsequence of A
        j = 0
        found = True
        for i in range(N):
            if j < M and A[i] == B[j]:
                j += 1
        if j == M:
            results.append("Yes")
        else:
            results.append("No")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
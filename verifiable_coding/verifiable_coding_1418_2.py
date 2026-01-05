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
        # The maximum sum S is achieved by sorting the array in non-decreasing order
        # and then multiplying each element by its position (1-based index)
        A.sort()
        S = 0
        for i in range(N):
            S += A[i] * (i + 1)
        results.append(S)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        Q = int(data[idx])
        idx += 1
        prefix_sum = [0] * (N + 1)
        for i in range(1, N+1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]
        for __ in range(Q):
            Q1 = int(data[idx])
            Q2 = int(data[idx+1])
            idx += 2
            res = prefix_sum[Q2] - prefix_sum[Q1-1]
            print(res)

if __name__ == '__main__':
    solve()
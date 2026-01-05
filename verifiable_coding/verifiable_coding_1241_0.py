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
        N, X = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        total = sum(A)
        remaining = N - X
        if remaining < 0:
            results.append("Jesse")
            continue
        sum_remaining = total - sum(A[:remaining])
        if sum_remaining % 2 == 0:
            results.append("Jesse")
        else:
            results.append("Walter")
    print("\n".join(results))

if __name__ == '__main__':
    solve()
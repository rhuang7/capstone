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
        P = list(map(int, data[idx:idx+N]))
        idx += N
        count = 0
        for i in range(N):
            # Consider the previous 5 days, but not before day 1
            start = max(0, i - 5)
            end = i
            min_prev = float('inf')
            for j in range(start, end):
                if P[j] < min_prev:
                    min_prev = P[j]
            if P[i] < min_prev:
                count += 1
        results.append(count)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
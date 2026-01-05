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
            # Check the previous 5 days, but not before day 1
            # Take the minimum of the previous 5 days (if available)
            prev = []
            for j in range(1, 6):
                if i - j >= 0:
                    prev.append(P[i-j])
            if not prev:
                # No previous days, consider as good
                count += 1
            else:
                if P[i] < min(prev):
                    count += 1
        results.append(count)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
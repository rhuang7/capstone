import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        # Compute the required coins
        coins = 0
        for i in range(1, n):
            if prefix[i] > 0:
                coins += prefix[i]
        results.append(str(coins))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
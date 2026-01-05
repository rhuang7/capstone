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
        # Compute the prefix sums of the array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        # The minimum coins needed is the sum of the absolute values of the prefix sums
        # except the last one (which is zero)
        coins = 0
        for i in range(1, n):
            coins += abs(prefix[i])
        results.append(str(coins))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
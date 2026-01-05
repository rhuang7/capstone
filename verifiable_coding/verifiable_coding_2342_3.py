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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        # Check if it is possible to make all elements zero
        # The key observation is that the prefix sum must be non-decreasing
        # and the suffix sum must be non-decreasing
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        # Check if prefix sums are non-decreasing
        valid = True
        for i in range(1, n):
            if prefix[i] > prefix[i + 1]:
                valid = False
                break
        if not valid:
            results.append("NO")
            continue
        # Check if the total sum is zero
        if prefix[n] != 0:
            results.append("NO")
            continue
        results.append("YES")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
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
        # Check if it's possible to make all elements zero
        # The key insight is that the prefix sums must be non-decreasing
        prefix = 0
        for num in a:
            prefix += num
            if prefix < 0:
                results.append("NO")
                break
        else:
            results.append("YES")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
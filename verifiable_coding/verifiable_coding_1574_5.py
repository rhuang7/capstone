import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    h = list(map(int, data[1:]))

    from collections import defaultdict

    count = defaultdict(int)
    for i in range(N - 1):
        a = h[i]
        b = h[i + 1]
        start = min(a, b)
        end = max(a, b)
        for height in range(start, end + 1):
            count[height] += 1

    max_k = 0
    for k in count.values():
        if k > max_k:
            max_k = k

    print(max_k)

if __name__ == '__main__':
    solve()
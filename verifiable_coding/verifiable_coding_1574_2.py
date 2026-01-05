import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    h = list(map(int, data[1:]))

    # Count occurrences of each height
    count = collections.defaultdict(int)
    for height in h:
        count[height] += 1

    # For each segment between consecutive heights, determine the range of heights
    # and increment the count for each height in that range
    # But since we are looking for maximum K, we can track the maximum count
    max_k = 0
    for i in range(N - 1):
        a = h[i]
        b = h[i + 1]
        if a > b:
            # Descending
            for height in range(a, b - 1, -1):
                count[height] += 1
        else:
            # Ascending
            for height in range(a, b + 1):
                count[height] += 1
        max_k = max(max_k, count[height])

    print(max_k)

if __name__ == '__main__':
    solve()
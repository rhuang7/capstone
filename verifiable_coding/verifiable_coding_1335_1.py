import sys

def solve():
    import sys
    from collections import Counter

    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    a = list(map(int, data[1:]))

    count = Counter(a)
    max_count = max(count.values())
    result = 0

    # If the maximum count is more than 2, the number of days is (max_count // 2) + 1
    # Otherwise, it's the maximum count
    if max_count > 2:
        result = (max_count // 2) + 1
    else:
        result = max_count

    print(result)

if __name__ == '__main__':
    solve()
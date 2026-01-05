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
        from collections import defaultdict
        count = defaultdict(int)
        for num in a:
            count[num] += 1
        max_len = 0
        for num in count:
            left = count[num]
            for other in count:
                if other == num:
                    continue
                if other in count:
                    middle = count[other]
                    total = left + middle + left
                    if total > max_len:
                        max_len = total
        results.append(str(max_len))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
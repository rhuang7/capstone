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
        for a_val in count:
            for b_val in count:
                if a_val == b_val:
                    max_len = max(max_len, count[a_val])
                else:
                    left = count[a_val]
                    right = count[b_val]
                    max_len = max(max_len, left + right + min(left, right))
        results.append(str(max_len))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
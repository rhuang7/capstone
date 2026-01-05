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
        m = int(data[idx+1])
        idx += 2
        banned = set(data[idx:idx+n])
        idx += n
        all_bin = []
        for i in range(2**m):
            s = format(i, '0{}b'.format(m))
            if s not in banned:
                all_bin.append(s)
        k = len(all_bin)
        median_idx = (k-1) // 2
        results.append(all_bin[median_idx])
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
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
        total = 1 << m
        k = total - n
        median_idx = (k - 1) // 2
        # Generate all binary strings of length m
        # Use binary counting to generate strings
        found = 0
        for i in range(total):
            s = format(i, '0{}b'.format(m))
            if s not in banned:
                found += 1
                if found == median_idx + 1:
                    results.append(s)
                    break
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
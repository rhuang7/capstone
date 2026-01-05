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
        banned = set()
        for __ in range(n):
            s = data[idx]
            banned.add(s)
            idx += 1
        # Generate all binary strings of length m
        all_strings = []
        for i in range(2**m):
            s = bin(i)[2:].zfill(m)
            if s not in banned:
                all_strings.append(s)
        k = len(all_strings)
        median_idx = (k-1) // 2
        results.append(all_strings[median_idx])
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
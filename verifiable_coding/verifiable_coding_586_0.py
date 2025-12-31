import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        while idx < len(data) and data[idx].strip() == b'':
            idx += 1
        if idx >= len(data):
            break
        N, R = map(int, data[idx].split())
        idx += 1
        teams = []
        for _ in range(R):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            t, p = data[idx].split(b' ')
            p = int(p)
            teams.append((t, p))
            idx += 1
        for _ in range(N - R):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            t, p = data[idx].split(b' ')
            p = int(p)
            teams.append((t, p))
            idx += 1
        # Process teams
        # Create a key for sorting: (-score, name)
        processed = []
        for t, p in teams:
            # Create a sorted tuple of character counts
            counts = sorted(t)
            key = (tuple(counts), t)
            processed.append((key, p))
        # Sort by score descending, then name ascending
        processed.sort(key=lambda x: (-x[1], x[0][1]))
        # Prepare output
        output = []
        for key, p in processed:
            name = key[1]
            output.append(f"{name} {p}")
        results.append('\n'.join(output))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
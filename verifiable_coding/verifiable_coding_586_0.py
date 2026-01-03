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
        # Create a canonical form for each team name
        # Sort by score (descending), then lex order (ascending)
        processed = []
        for t, p in teams:
            # Create a sorted tuple of character counts
            count = {}
            for c in t:
                count[c] = count.get(c, 0) + 1
            canonical = tuple(sorted(count.items()))
            processed.append((canonical, p, t))
        # Sort by score descending, then name lex order ascending
        processed.sort(key=lambda x: (-x[1], x[2]))
        # Prepare output
        output = []
        for canonical, p, t in processed:
            output.append(f"{t} {p}")
        results.append("\n".join(output))
    print("\n".join(results))
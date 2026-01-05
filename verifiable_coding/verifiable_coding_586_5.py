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
        teams = {}
        for _ in range(R):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            parts = data[idx].split()
            idx += 1
            name = parts[0]
            points = int(parts[1])
            key = tuple(sorted(name))
            teams[key] = teams.get(key, 0) + points
        for _ in range(N - R):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            name = data[idx].split()[0]
            idx += 1
            key = tuple(sorted(name))
            teams[key] = teams.get(key, 0) + points
        sorted_teams = sorted(teams.items(), key=lambda x: (-x[1], x[0]))
        for name, points in sorted_teams:
            results.append(f"{name} {points}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
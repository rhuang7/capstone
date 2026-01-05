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
            parts = data[idx].split()
            idx += 1
            name = parts[0]
            points = int(parts[1])
            teams.append((name, points))
        for _ in range(N - R):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            parts = data[idx].split()
            idx += 1
            name = parts[0]
            points = int(parts[1])
            # Normalize the name to a canonical form
            freq = {}
            for c in name:
                freq[c] = freq.get(c, 0) + 1
            key = tuple(sorted(freq.items()))
            # Check if this team already exists in the list
            found = False
            for i in range(len(teams)):
                t_name, t_points = teams[i]
                t_freq = {}
                for c in t_name:
                    t_freq[c] = t_freq.get(c, 0) + 1
                t_key = tuple(sorted(t_freq.items()))
                if t_key == key:
                    teams[i] = (t_name, t_points + points)
                    found = True
                    break
            if not found:
                teams.append((name, points))
        # Sort the teams by score descending, then name lex order
        teams.sort(key=lambda x: (-x[1], x[0]))
        for name, points in teams:
            results.append(f"{name} {points}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
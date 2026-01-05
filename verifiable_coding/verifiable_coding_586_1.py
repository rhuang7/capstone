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
        team_data = []
        for _ in range(R):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            parts = data[idx].split()
            idx += 1
            team_data.append((parts[0], int(parts[1])))
        for _ in range(N - R):
            while idx < len(data) and data[idx].strip() == b'':
                idx += 1
            if idx >= len(data):
                break
            parts = data[idx].split()
            idx += 1
            team_data.append((parts[0], int(parts[1])))
        # Process team data
        # Create a canonical form for each team (sorted characters)
        from collections import defaultdict
        score_dict = defaultdict(int)
        for name, points in team_data:
            # Create canonical form by sorting the characters
            canonical = ''.join(sorted(name))
            score_dict[canonical] += points
        # Sort the teams by score (descending), then lex order (ascending)
        sorted_teams = sorted(score_dict.items(), key=lambda x: (-x[1], x[0]))
        # Prepare output
        output = []
        for name, points in sorted_teams:
            output.append(f"{name} {points}")
        results.append('\n'.join(output))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
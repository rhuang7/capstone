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
        # Create a dictionary to store the total points for each team
        # Use the sorted character count as the key
        from collections import defaultdict
        import sys
        import string
        def get_key(team_name):
            return tuple(sorted(team_name))
        total_points = defaultdict(int)
        for team, points in team_data:
            key = get_key(team)
            total_points[key] += points
        # Create a list of (total_points, team_name) tuples
        scoreboard = []
        for key in total_points:
            team_name = ''.join(key)
            scoreboard.append((total_points[key], team_name))
        # Sort by score descending, then lex order ascending
        scoreboard.sort(key=lambda x: (-x[0], x[1]))
        # Prepare output
        for score, name in scoreboard:
            results.append(f"{name} {score}")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
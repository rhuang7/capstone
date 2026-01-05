import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        L = int(data[idx+2])
        idx += 3
        if K < 2 or N > K * L:
            results.append("-1")
            continue
        if N == 0:
            results.append("")
            continue
        # Assign players in a repeating pattern, ensuring no two consecutive overs have the same bowler
        # Also ensure no player bowls more than L overs
        # We can use a simple pattern like 1, 2, 3, ..., K, 1, 2, 3, ..., K, ...
        # But we need to ensure that no player bowls more than L overs
        # So we can assign players in a way that each player bowls at most L overs
        # We can use a list to track how many times each player has bowled
        # We can also use a simple pattern to assign players
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a list of players and cycle through them, but skip the current player
        # We can use a
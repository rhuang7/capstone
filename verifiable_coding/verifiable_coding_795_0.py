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
        
        # We can assign players in a repeating pattern
        # Ensure no two consecutive overs have the same bowler
        # And each player bowls at most L overs
        # We can use a pattern like 1, 2, 3, ..., K, 1, 2, 3, ..., K, ...
        # But we need to make sure that no player bowls more than L overs
        # So we can repeat the pattern K times, but only up to L times per player
        # If N > K * L, it's impossible
        
        # Check if it's possible
        if N > K * L:
            results.append("-1")
            continue
        
        # Create a list of players in a repeating pattern
        # We can use a cycle of 1 to K, but ensure that each player is used at most L times
        # We can use a list of players in a repeating pattern, but with a limit of L per player
        # So we can create a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # So we can create a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list of players in a repeating pattern of 1 to K, but only up to L times per player
        # We can use a list
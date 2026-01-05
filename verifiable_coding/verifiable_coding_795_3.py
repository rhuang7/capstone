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
        
        if K < 2 or L < 1:
            results.append("-1")
            continue
        
        # Check if it's possible to assign bowlers
        # Each player can bowl at most L overs, and no two consecutive overs can have the same bowler
        # The minimum number of players needed is 2, and the maximum number of overs a player can bowl is L
        # So, if N > K * L, it's impossible
        if N > K * L:
            results.append("-1")
            continue
        
        # Assign bowlers in a repeating pattern
        # We can alternate between players 1 and 2, then 3, etc.
        # But we need to make sure that no player bowls more than L overs
        # So, we can assign players in a cycle of 1, 2, 3, ..., K, 1, 2, 3, ..., K, ...
        # And track how many times each player has bowled
        # If a player has bowled L times, we skip them in the next assignment
        # We can use a list to track the number of times each player has bowled
        # And a list to track the current bowler for each over
        bowlers = [0] * K
        result = []
        current_bowler = 0
        
        for i in range(N):
            # Find the next available bowler
            for j in range(K):
                if bowlers[j] < L:
                    current_bowler = j
                    break
            result.append(current_bowler + 1)
            bowlers[current_bowler] += 1
        
        results.append(' '.join(map(str, result)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
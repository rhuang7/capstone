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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # We need to determine if Vanja can force |V| >= K
        # Since players play optimally, we can use dynamic programming
        # dp[i][v] = True if the current player can force the absolute value to be >= K from position i with value v
        # However, since N can be up to 3e4, we need a more efficient approach
        
        # We can use a greedy approach since the players are trying to maximize/minimize the absolute value
        # The key observation is that the optimal play will always result in the maximum possible absolute value
        # So we can simulate the game and track the possible values
        
        # Initialize the possible values
        possible = {0}
        for i in range(N):
            new_possible = set()
            for val in possible:
                # Add the current bit
                new_val = val + A[i]
                new_possible.add(new_val)
                # Subtract the current bit
                new_val = val - A[i]
                new_possible.add(new_val)
            possible = new_possible
        
        # Check if any value in possible has absolute value >= K
        if any(abs(v) >= K for v in possible):
            results.append(1)
        else:
            results.append(2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
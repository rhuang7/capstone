import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    q = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        boards = []
        for _ in range(n):
            a = int(data[idx])
            b = int(data[idx + 1])
            boards.append((a, b))
            idx += 2
        
        # If there's only one board, no changes needed
        if n == 1:
            results.append(0)
            continue
        
        # For each board, keep track of the possible heights and their costs
        # We'll use a dynamic programming approach where dp[i][h] represents the minimum cost to make the first i boards great with the i-th board having height h
        # Since each board can be increased by any number of times, we can consider only the three possible heights for each board: original, original + 1, original + 2
        # Because if two adjacent boards have the same height, we need to change one of them, and changing by more than 2 is unnecessary as we can always adjust to a height that is different from the previous one
        
        # Initialize dp array
        dp = [{} for _ in range(n)]
        
        # First board
        a, b = boards[0]
        dp[0][a] = 0
        dp[0][a + 1] = b
        dp[0][a + 2] = 2 * b
        
        # Fill dp for the rest of the boards
        for i in range(1, n):
            a_i, b_i = boards[i]
            prev = dp[i - 1]
            curr = {}
            
            # For each possible height of the current board
            for h in [a_i, a_i + 1, a_i + 2]:
                cost = 0
                # Try to make the current board's height different from the previous board's height
                for prev_h in prev:
                    if prev_h != h:
                        cost = prev[prev_h] + (h - a_i) * b_i
                        if h in curr:
                            curr[h] = min(curr[h], cost)
                        else:
                            curr[h] = cost
            dp[i] = curr
        
        # The answer is the minimum value in the last dp entry
        results.append(min(dp[n - 1].values()))
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()
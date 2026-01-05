import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    cases = data[1:T+1]
    
    for s in cases:
        # Convert the string to a list of characters
        s_list = list(s)
        # Group consecutive characters
        groups = []
        i = 0
        while i < len(s_list):
            current = s_list[i]
            count = 1
            while i + 1 < len(s_list) and s_list[i+1] == current:
                i += 1
                count += 1
            groups.append((current, count))
            i += 1
        
        # Calculate the total number of 1s
        total_ones = sum(count for char, count in groups if char == '1')
        
        # If there are no 1s, Alice's score is 0
        if total_ones == 0:
            print(0)
            continue
        
        # Alice and Bob take turns, trying to maximize their own score
        # We simulate the game by considering each group of 1s and 0s
        # The game is similar to a game of taking turns picking from a list of values
        # We can use dynamic programming to find the optimal play
        
        # We create a list of the counts of 1s in each group
        ones_groups = [count for char, count in groups if char == '1']
        
        # Use dynamic programming to find the optimal score for Alice
        n = len(ones_groups)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n, 0, -1):
            for j in range(i, 0, -1):
                # If it's Alice's turn, she takes the current group
                if i == j:
                    dp[i][j] = ones_groups[i-1]
                else:
                    # Alice can take the first or last group
                    # Bob will then take the optimal choice
                    take_first = ones_groups[i-1] + dp[i+1][j]
                    take_last = ones_groups[j-1] + dp[i][j-1]
                    dp[i][j] = max(take_first, take_last)
        
        # The result is the value for the full list of 1s groups
        print(dp[1][n])

if __name__ == '__main__':
    solve()
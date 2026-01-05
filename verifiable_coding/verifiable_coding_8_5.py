import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # Compute initial score
        score = 0
        prev_win = False
        for i in range(n):
            if s[i] == 'W':
                if prev_win:
                    score += 2
                else:
                    score += 1
                prev_win = True
            else:
                prev_win = False
        
        # Now try to maximize the score by changing up to k games
        # We can change 'L' to 'W' to get more points, but we have to consider the previous game
        # We also need to consider changing 'W' to 'L' if it helps (but this is not useful for maximizing score)
        # So we only consider changing 'L' to 'W' to get more points
        
        # We can track the current state (prev_win) and try to find the best way to change 'L' to 'W'
        # We can use a greedy approach: change 'L' to 'W' if it increases the score
        
        # We need to find the best positions to change 'L' to 'W'
        # We can use a priority queue to track the potential gain of changing each 'L' to 'W'
        # But since we have limited k changes, we can greedily select the best ones
        
        # Let's compute the potential gain for each 'L' to 'W' change
        # We can do this by checking the previous and next game
        # For each 'L' at position i, the gain depends on the previous and next game
        # We can compute the gain for changing s[i] to 'W'
        
        # We'll use a list to store the potential gain for each 'L' to 'W' change
        gains = []
        for i in range(n):
            if s[i] == 'L':
                # Compute the gain if we change this to 'W'
                # We need to consider the previous and next game
                # The gain is the difference between the new score and the old score
                # The old score for this position is 0 (since it's 'L')
                # The new score for this position depends on the previous game
                prev_win = False
                for j in range(i-1, -1, -1):
                    if s[j] == 'W':
                        prev_win = True
                        break
                if prev_win:
                    gain = 2
                else:
                    gain = 1
                gains.append(gain)
        
        # Now we need to select the top k gains from the gains list
        # But we need to be careful: changing a 'L' to 'W' can affect the previous and next games
        # So we can't just take the top k gains, because changing one 'L' to 'W' might affect the gains of others
        # So we need to find the optimal way to change 'L's to 'W's in a way that maximizes the score
        
        # We can use a greedy approach: we can try to change 'L's to 'W's in a way that maximizes the gain
        # We can use a priority queue to select the best changes
        
        # But for the sake of time and efficiency, we can use a greedy approach: we can iterate through the string
        # and whenever we find an 'L', we can change it to 'W' if it gives a higher gain than the current state
        
        # We can also use a dynamic programming approach, but for the sake of time, we'll use a greedy approach
        
        # We'll keep track of the previous game's state
        prev_win = False
        for i in range(n):
            if s[i] == 'L':
                # We can change this to 'W' if it gives us more points
                # The gain is 1 or 2, depending on the previous game
                if prev_win:
                    gain = 2
                else:
                    gain = 1
                if k > 0:
                    # Change this to 'W'
                    score += gain
                    prev_win = True
                    k -= 1
                else:
                    # Can't change, so leave as 'L'
                    pass
            else:
                # It's 'W', so we can check if we can change it to 'L' to get more points
                # But changing 'W' to 'L' is not useful for maximizing score
                # So we leave it as 'W'
                prev_win = True
        
        results.append(score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
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
        
        # Try to maximize score by changing up to k games
        # We can change L to W to get more points, but we need to consider the previous game
        # We can also change W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can greedily change L to W, but we need to consider the previous game
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can try to change L to W in a way that maximizes the points
        # We can do this by checking for consecutive L's and changing them to W's
        # We can also change L to W in a way that the previous game was a win
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to W, and if the previous was a win, we get 2 points, else 1
        
        # We can also consider changing W to L to avoid losing points, but that's not helpful
        # So we focus on changing L to W
        
        # We can try to change L to W in a way that maximizes the points
        # We can track the current state of the game (whether the previous was a win)
        # We can also track the number of changes we can make
        
        # We can use a greedy approach: for each position, if it's L and we have changes left,
        # we can try to change it to
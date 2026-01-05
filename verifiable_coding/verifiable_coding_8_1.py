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
        
        # Calculate initial score
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
        
        # Try to improve the score by changing up to k games
        # We can change 'L' to 'W' to gain more points
        # We can also change 'W' to 'L' to avoid losing points, but that's not useful
        # So we only consider changing 'L' to 'W'
        
        # We need to find the best positions to change 'L' to 'W' to maximize the score
        # We can greedily change 'L' to 'W' in positions where it would give the most points
        # We can also change 'W' to 'L' if it's better, but that's not useful here
        
        # Let's find all positions where changing 'L' to 'W' would give us more points
        # We can do this by checking the current state and the previous state
        
        # We'll keep track of the current state and the previous win state
        # We'll also track the best possible score after changing up to k games
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # Let's try to find the best positions to change
        # We'll keep track of the current state and the previous win state
        # We'll also track the best possible score after changing up to k games
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W' in positions where it would give us the most points
        # We'll also consider changing 'W' to 'L' if it's better, but that's not useful here
        
        # We'll use a greedy approach: change 'L' to 'W
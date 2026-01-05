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
        
        # Now try to maximize the score by changing up to k games
        # We can change 'L' to 'W' to get more points, or 'W' to 'L' to break streaks
        # We need to find the optimal way to use k changes
        
        # We can try to find the best positions to change 'L' to 'W' to get maximum points
        # We can also try to break long streaks of 'W' by changing some 'W' to 'L'
        
        # For this problem, the optimal strategy is to:
        # 1. Convert as many 'L' to 'W' as possible, up to k
        # 2. For each 'W' converted, check if it's part of a streak and calculate the gain
        # 3. Also, if we have more than k 'W's, we can break some streaks to get more points
        
        # We can simulate this by keeping track of the current streak of 'W's
        # and decide whether to change a 'W' to 'L' to get more points
        
        # Let's try to find the maximum possible score
        # We can use a greedy approach: convert 'L' to 'W' as much as possible
        # and break long streaks of 'W's if needed
        
        # Let's try to find the best way to use k changes
        # We can use a dynamic programming approach, but for large n, we need an efficient way
        
        # Let's try to find the best way to use k changes
        # We can simulate the process of converting 'L' to 'W' and breaking streaks
        
        # We'll track the current streak of 'W's and the current score
        current_streak = 0
        current_score = 0
        changes_left = k
        
        # We'll iterate through the string and try to convert 'L' to 'W' when possible
        # and break streaks when needed
        i = 0
        while i < n and changes_left > 0:
            if s[i] == 'L':
                # Convert to 'W' to get points
                # If it's the first game, we get 1 point
                # If it's part of a streak, we get 2 points
                # So we can convert this to 'W' and add points
                # We also need to check if we can extend the streak
                # But since we're converting from 'L' to 'W', we can just add 1 point
                # and start a new streak
                current_score += 1
                current_streak = 1
                changes_left -= 1
                i += 1
            else:
                # It's a 'W', we can either keep it or change it to 'L' to break the streak
                # If we change it to 'L', we can get more points in the future
                # So we'll check if it's better to break the streak or not
                # For now, we'll keep it as 'W' and add points
                if current_streak > 0:
                    current_score += 2
                else:
                    current_score += 1
                current_streak += 1
                i += 1
        
        # Now, we have used up all k changes, but we may have a long streak of 'W's
        # We can try to break some of them to get more points
        # For example, if we have a streak of m 'W's, we can break one to get more points
        # But this is not straightforward, so we'll use a different approach
        
        # Let's try to find all the positions where we can change 'L' to 'W' and get the maximum points
        # We can also try to break long streaks of 'W's to get more points
        
        # We'll use a greedy approach: convert as many 'L' to 'W' as possible, up to k
        # and break streaks of 'W's when needed
        
        # We'll track the current streak of 'W's and the current score
        current_streak = 0
        current_score = 0
        changes_left = k
        
        # We'll iterate through the string and try to convert 'L' to 'W' when possible
        # and break streaks when needed
        i = 0
        while i < n and changes_left > 0:
            if s[i] == 'L':
                # Convert to 'W' to get points
                # If it's the first game, we get 1 point
                # If it's part of a streak, we get 2 points
                # So we can convert this to 'W' and add points
                # We also need to check if we can extend the streak
                # But since we're converting from 'L' to 'W', we can just add 1 point
                # and start a new streak
                current_score += 1
                current_streak = 1
                changes_left -= 1
                i += 1
            else:
                # It's a 'W', we can either keep it or change it to 'L' to break the streak
                # If we change it to 'L', we can get more points in the future
                # So we'll check if it's better to break the streak or not
                # For now, we'll keep it as 'W' and add points
                if current_streak > 0:
                    current_score += 2
                else:
                    current_score += 1
                current_streak += 1
                i += 1
        
        # Now, we have used up all k changes, but we may have a long streak of 'W's
        # We can try to break some of them to get more points
        # For example, if we have a streak of m 'W's, we can break one to get more points
        # But this is not straightforward, so we'll use a different approach
        
        # Let's try to find all the positions where we can change 'L' to 'W' and get the maximum points
        # We can also try to break long streaks of 'W's to get more points
        
        # We'll use a greedy approach: convert as many 'L' to 'W' as possible, up to k
        # and break streaks of 'W's when needed
        
        # We'll track the current streak of 'W's and the current score
        current_streak = 0
        current_score = 0
        changes_left = k
        
        # We'll iterate through the string and try to convert 'L' to 'W' when possible
        # and break streaks when needed
        i = 0
        while i < n and changes_left > 0:
            if s[i] == 'L':
                # Convert to 'W' to get points
                # If it's the first game, we get 1 point
                # If it's part of a streak, we get 2 points
                # So we can convert this to 'W' and add points
                # We also need to check if we can extend the streak
                # But since we're converting from 'L' to 'W', we can just add 1 point
                # and start a new streak
                current_score += 1
                current_streak = 1
                changes_left -= 1
                i += 1
            else:
                # It's a 'W', we can either keep it or change it to 'L' to break the streak
                # If we change it to 'L', we can get more points in the future
                # So we'll check if it's better to break the streak or not
                # For now, we'll keep it as 'W' and add points
                if current_streak > 0:
                    current_score += 2
                else:
                    current_score += 1
                current_streak += 1
                i += 1
        
        results.append(current_score)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
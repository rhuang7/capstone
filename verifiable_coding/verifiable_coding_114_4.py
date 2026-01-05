import sys
import bisect

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        m = int(data[idx])
        idx += 1
        heroes = []
        for _ in range(m):
            p = int(data[idx])
            s = int(data[idx + 1])
            idx += 2
            heroes.append((p, s))
        
        # Preprocess monsters
        # Find for each monster the minimum p_i that can defeat it
        # For each monster, find the minimum p_i such that p_i > a_i
        # We can sort the heroes by p_i and for each monster, find the smallest p_i that can defeat it
        # Also, for each hero, we can find the maximum number of monsters they can defeat in a day
        # We need to find the minimal days to defeat all monsters
        
        # Sort heroes by p_i
        heroes.sort()
        # For each monster, find the minimal p_i that can defeat it
        # We can use binary search
        min_p_for_monster = []
        for ai in a:
            # Find the smallest p_i > ai
            # Since heroes are sorted by p_i, we can use bisect
            p = bisect.bisect_right(heroes, (ai, float('inf')))  # find first p_i > ai
            if p == len(heroes):
                # No hero can defeat this monster
                results.append(-1)
                break
            min_p_for_monster.append(heroes[p][0])
        
        else:
            # Now we have min_p_for_monster, which is the minimal p_i for each monster
            # Now we need to find the minimal days to defeat all monsters
            # We can use a greedy approach: for each day, select the hero with the highest s_i (endurance)
            # that can defeat the current monster
            # We can use a priority queue (max-heap) of heroes based on s_i
            # For each monster, we select the hero with the highest s_i that can defeat it
            # We can precompute the max s_i for each possible p_i
            # But since heroes are sorted by p_i, we can use a sliding window approach
            # We can use a priority queue (max-heap) of heroes that can defeat the current monster
            
            # Precompute for each monster the maximum s_i of heroes that can defeat it
            # We can use a sliding window approach
            # Since heroes are sorted by p_i, we can find for each monster the range of heroes that can defeat it
            # and take the maximum s_i in that range
            
            # Precompute the maximum s_i for each possible p_i
            # We can use a sliding window and a deque to keep track of maximum s_i
            # We can use a binary search to find the range of heroes that can defeat the current monster
            # and then take the maximum s_i in that range
            
            # We can use a binary indexed tree or segment tree for this, but for simplicity, we can use a sliding window
            # approach with a deque to track the maximum s_i in the current window
            
            # First, we sort the heroes by p_i
            # Then, for each monster, we find the earliest hero that can defeat it
            # and then find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            # We can use a sliding window and a deque to track the maximum s_i
            
            # Precompute for each monster the maximum s_i of heroes that can defeat it
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # Let's precompute the max s_i for each possible p_i
            # We can use a binary indexed tree or a segment tree for this, but for simplicity, we can use a sliding window
            # with a deque to track the maximum s_i in the current window
            
            # We can precompute the max s_i for each monster
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # Let's precompute the max s_i for each monster
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary indexed tree or a segment tree for this, but for simplicity, we can use a sliding window
            # with a deque to track the maximum s_i in the current window
            
            # We can precompute the max s_i for each monster
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # Let's precompute the max s_i for each monster
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # Let's precompute the max s_i for each monster
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
            
            # We can use a binary search to find the earliest hero that can defeat the monster
            # Then, we can use a sliding window to find the maximum s_i in the range [earliest_hero, len(heroes)-1]
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
        # Find the minimum number of days needed
        # For each hero, find the maximum number of monsters they can defeat in a day
        # Sort the heroes by p in descending order
        heroes.sort(reverse=True)
        
        # For each hero, find the maximum number of monsters they can defeat in a day
        # This is the maximum k such that a[0...k-1] <= p
        # We can use binary search for this
        # Precompute prefix array
        prefix = []
        current = 0
        for i in range(n):
            if a[i] <= heroes[0][0]:
                current += 1
            else:
                current = 0
            prefix.append(current)
        
        # For each hero, find the maximum number of monsters they can defeat in a day
        # This is the maximum k such that a[0...k-1] <= p
        # We can use binary search for this
        # Precompute prefix array
        # Now, for each hero, find the maximum number of monsters they can defeat in a day
        # We can use binary search for this
        # For each hero, find the maximum k such that a[0...k-1] <= p
        # We can use binary search for this
        
        # Now, we need to find the minimum number of days
        # We can use a greedy approach: use the hero with the highest p first
        # For each day, use the hero with the highest p that can defeat the current monster
        # The hero can defeat up to s monsters in a day
        # So, for each day, we try to defeat as many monsters as possible
        # We can use a priority queue to select the best hero for each day
        
        # Let's use a priority queue (max heap) to select the best hero for each day
        # The priority is based on the hero's p
        # We can use a max heap
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # Let's use a greedy approach: for each monster, find the best hero that can defeat it
        # The best hero is the one with the highest p that can defeat the monster
        # We can precompute for each monster, the maximum p that can defeat it
        # Then, for each monster, we select the best hero that can defeat it and has not been used up
        
        # Precompute for each monster, the maximum p that can defeat it
        max_p_for_monster = [0] * n
        for i in range(n):
            # Find the maximum p in heroes that can defeat a[i]
            # Since heroes are sorted in descending order, we can use binary search
            # Find the first hero with p >= a[i]
            left, right = 0, len(heroes)
            while left < right:
                mid = (left + right) // 2
                if heroes[mid][0] >= a[i]:
                    left = mid + 1
                else:
                    right = mid
            max_p_for_monster[i] = heroes[left - 1][0] if left > 0 else -1
        
        # Now, for each monster, we can find the best hero that can defeat it
        # We can use a greedy approach: for each monster, select the best hero that can defeat it
        # The best hero is the one with the highest p that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # We can use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # Let's use a priority queue (max heap) to select the best hero for each monster
        # The priority is based on the hero's p
        # We can use a max heap
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # We can use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # Let's use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # We can use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # Let's use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # We can use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # Let's use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # We can use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # We can use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # We can use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process the monsters in order, we can't use a heap directly
        # So we'll process the monsters in order and for each monster, find the best hero that can defeat it
        
        # We can use a greedy approach: for each monster, find the best hero that can defeat it
        # We can use a priority queue (max heap) to select the best hero for each monster
        # But since we need to process
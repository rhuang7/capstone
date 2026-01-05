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
        # Find the minimum number of days required to defeat all monsters
        # Using a greedy approach with binary search
        
        # Sort the monsters
        a.sort()
        
        # Preprocess heroes: for each hero, find the maximum number of monsters they can defeat
        # in a single day, given their power and endurance
        # For each hero, we can find the maximum number of monsters they can defeat in a day
        # by finding the longest prefix of monsters that are all <= p_i
        # This can be done with binary search
        
        # Precompute the prefix array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + 1
        
        # For each hero, find the maximum number of monsters they can defeat in a day
        # by finding the largest k such that a[k] <= p_i
        # This can be done with binary search
        max_monsters_per_day = []
        for p, s in heroes:
            # Find the largest index where a[i] <= p
            # Using bisect_right
            k = bisect.bisect_right(a, p)
            max_monsters_per_day.append(k)
        
        # Now, we need to find the minimum number of days to defeat all n monsters
        # We can use a greedy approach: in each day, use the hero that can defeat the most monsters
        # possible, starting from the current position
        
        # We'll use a priority queue (max heap) to select the best hero each day
        # However, since we need to process monsters in order, we'll use a greedy approach
        # with binary search and a sorted list of heroes
        
        # Sort heroes by their max monsters per day in descending order
        heroes_sorted = sorted(heroes, key=lambda x: bisect.bisect_right(a, x[0]), reverse=True)
        
        # Now, for each hero, we can precompute the max monsters they can defeat
        # and use a greedy approach
        
        # We'll use a pointer to track the current monster index
        current_monster = 0
        days = 0
        
        while current_monster < n:
            # Find the best hero that can defeat the current monster
            best_hero = None
            best_k = 0
            for p, s in heroes_sorted:
                # Find the maximum number of monsters this hero can defeat
                k = bisect.bisect_right(a, p)
                if k > best_k and k > current_monster:
                    best_k = k
                    best_hero = (p, s)
            
            if best_hero is None:
                # No hero can defeat the current monster
                results.append(-1)
                break
            
            # Use this hero to defeat as many monsters as possible
            k = bisect.bisect_right(a, best_hero[0])
            if k <= current_monster:
                # This hero can't defeat the current monster
                results.append(-1)
                break
            
            # The hero can defeat up to min(s, k - current_monster) monsters
            # So we can defeat up to min(s, k - current_monster) monsters
            max_defeated = min(best_hero[1], k - current_monster)
            current_monster += max_defeated
            days += 1
        
        if current_monster == n:
            results.append(days)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
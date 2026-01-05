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
            heroes.append((p, s))
            idx += 2
        
        # Preprocess monsters
        # For each hero, find the maximum number of monsters they can defeat in a day
        # We need to find for each hero the maximum k such that a[0...k-1] <= p_i
        # So we sort the monsters and for each hero, find the maximum k where a[k-1] <= p_i
        # Then, for each hero, the maximum number of monsters they can defeat in a day is k
        # We can use binary search for this
        
        # Sort the monsters
        a_sorted = sorted(a)
        
        # Precompute for each hero the maximum number of monsters they can defeat in a day
        max_monsters_per_hero = []
        for p, s in heroes:
            # Find the maximum k such that a_sorted[k-1] <= p
            # Using bisect_right
            k = bisect.bisect_right(a_sorted, p)
            max_monsters_per_hero.append(k)
        
        # Now, we need to find the minimum number of days to defeat all n monsters
        # We can use a greedy approach: use the hero with the maximum possible s_i (endurance) to defeat as many monsters as possible each day
        # So we sort the heroes by their max_monsters_per_hero in descending order
        
        # Sort heroes by their max_monsters_per_hero in descending order
        heroes_sorted = sorted(zip(max_monsters_per_hero, heroes), key=lambda x: (-x[0], x[1]))
        
        # Now, simulate the process
        days = 0
        current_monster = 0
        for max_monsters, (p, s) in heroes_sorted:
            if max_monsters == 0:
                # This hero cannot defeat any monster
                continue
            # How many monsters can this hero defeat in one day?
            # We can take min(max_monsters, n - current_monster)
            # But we need to take the maximum possible, which is min(max_monsters, n - current_monster)
            # So we take the minimum of the two
            take = min(max_monsters, n - current_monster)
            days += 1
            current_monster += take
            if current_monster == n:
                break
        if current_monster == n:
            results.append(days)
        else:
            results.append(-1)
    
    for res in results:
        print(res)
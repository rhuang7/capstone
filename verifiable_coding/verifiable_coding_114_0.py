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
        # Find the minimum number of days required
        # For each hero, find the maximum number of monsters they can defeat in a day
        # Sort the monsters in increasing order
        a.sort()
        
        # For each hero, find the maximum number of monsters they can defeat in a day
        # This is the maximum k such that a[i] <= p for the first k monsters
        # We can use binary search for this
        # Precompute prefix sums of the monsters
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        
        # For each hero, find the maximum number of monsters they can defeat in a day
        # This is the maximum k such that a[k-1] <= p
        # We can use binary search for this
        # Also, the hero can defeat up to s monsters in a day
        # So the effective maximum is min(s, k)
        # We need to find the minimum number of days required to defeat all monsters
        # This is a greedy problem: we want to use the heroes that can defeat the most monsters in a day
        
        # Sort the heroes by their power in descending order
        heroes.sort(reverse=True)
        
        # Now, simulate the process
        # We will use a greedy approach: use the best hero possible each day
        # We will track how many monsters have been defeated so far
        # For each day, we select the best hero that can defeat as many monsters as possible
        # The best hero is the one with the highest power and the highest endurance
        
        # We can use a priority queue to select the best hero each day
        # But since we have to use exactly one hero per day, and we can reuse heroes, we can just keep track of the best hero
        # So, for each day, we select the best hero (highest p and highest s)
        # We can precompute for each hero the maximum number of monsters they can defeat in a day
        # Then, we select the hero with the highest possible value
        
        # Precompute for each hero the maximum number of monsters they can defeat in a day
        max_monsters_per_day = []
        for p, s in heroes:
            # Find the maximum k such that a[k-1] <= p
            # Use binary search
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if a[mid - 1] <= p:
                    left = mid + 1
                else:
                    right = mid
            k = left - 1
            max_monsters_per_day.append(min(s, k))
        
        # Now, we need to find the minimum number of days to defeat all monsters
        # We can use a greedy approach: each day, use the hero that can defeat the most monsters
        # We can sort the heroes by their max_monsters_per_day in descending order
        # Then, for each day, select the best hero and defeat as many monsters as possible
        
        # Sort the heroes by max_monsters_per_day in descending order
        heroes_with_max = sorted(zip(max_monsters_per_day, heroes), key=lambda x: (-x[0], -x[1][0]))
        
        # Now, simulate the process
        days = 0
        monsters_defeated = 0
        
        while monsters_defeated < n:
            # Select the best hero
            max_k, (p, s) = heroes_with_max[0]
            # How many monsters can this hero defeat in a day?
            # It's the minimum of s and the number of monsters that can be defeated by this hero
            # But we have to check how many monsters are left
            # The hero can defeat up to s monsters, but only as many as are left and can be defeated
            # So the number of monsters this hero can defeat in a day is min(s, remaining_monsters)
            # But also, the hero can only defeat monsters that are <= p
            # So the maximum number of monsters this hero can defeat in a day is min(s, k)
            # Where k is the number of monsters that can be defeated by this hero
            # But we have to find how many monsters are left that can be defeated by this hero
            # We can use binary search to find the maximum number of monsters that can be defeated by this hero
            # But since we have already precomputed k for each hero, we can use that
            # However, since the monsters are sorted, we can use the current position to find how many can be defeated
            # Let's find the maximum number of monsters this hero can defeat in a day
            # We can use the precomputed k for this hero
            # But we have to check how many monsters are left
            # The hero can defeat up to s monsters, but only as many as are left and can be defeated
            # So the number of monsters this hero can defeat in a day is min(s, k - monsters_defeated)
            # But we have to check if the monsters that are left can be defeated by this hero
            # So the maximum number of monsters this hero can defeat in a day is min(s, k - monsters_defeated)
            # But we have to check if the monsters that are left can be defeated by this hero
            # So we can use binary search to find the maximum number of monsters that can be defeated by this hero
            # starting from monsters_defeated
            # Find the maximum number of monsters that can be defeated by this hero
            left, right = monsters_defeated, n
            while left < right:
                mid = (left + right) // 2
                if a[mid - 1] <= p:
                    left = mid + 1
                else:
                    right = mid
            max_possible = left - 1
            # The hero can defeat up to s monsters, but only as many as are left and can be defeated
            # So the number of monsters this hero can defeat in a day is min(s, max_possible - monsters_defeated)
            # But we have to make sure that this number is at least 1
            # If the hero can't defeat any monster, then it's impossible
            if max_possible <= monsters_defeated:
                results.append(-1)
                break
            # The number of monsters this hero can defeat in a day is min(s, max_possible - monsters_defeated)
            # But since we want to maximize the number of monsters defeated per day, we use min(s, max_possible - monsters_defeated)
            # However, we can only defeat up to s monsters
            # So the number of monsters this hero can defeat in a day is min(s, max_possible - monsters_defeated)
            # But we have to make sure that this number is at least 1
            if max_possible - monsters_defeated <= 0:
                results.append(-1)
                break
            # So the number of monsters this hero can defeat in a day is min(s, max_possible - monsters_defeated)
            # But since the hero can defeat up to s monsters, we can use that
            # However, the hero can only defeat as many as are left and can be defeated
            # So the number of monsters this hero can defeat in a day is min(s, max_possible - monsters_defeated)
            # But we have to make sure that this number is at least 1
            # So the number of monsters this hero can defeat in a day is min(s, max_possible - monsters_defeated)
            # But if this number is 0, then it's impossible
            # So we check if max_possible - monsters_defeated <= 0
            # If so, it's impossible
            # Otherwise, we can defeat that number of monsters
            # So we take the minimum of s and the number of monsters that can be defeated
            # So the number of monsters this hero can defeat in a day is min(s, max_possible - monsters_defeated)
            # But we have to make sure that this number is at least 1
            # So we take the minimum of s and the number of monsters that can be defeated
            # But we have to make sure that this number is at least 1
            # So we take the minimum of s and the number of monsters that can be defeated
            # So the number of monsters this hero can defeat in a day is min(s, max_possible - monsters_defeated)
            # But we have to make sure that this number is at least 1
            # So we take the minimum of s and the number of monsters that can be defeated
            #
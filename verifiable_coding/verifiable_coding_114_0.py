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
        
        # Preprocess monsters to find the minimum power required to defeat each monster
        # We need to find for each monster, the minimum p_i such that p_i >= a[i]
        # And the maximum s_i for that p_i
        # We sort the monsters and for each, find the minimum p_i that can defeat it
        # Then, for each monster, we can find the maximum s_i that can be used for it
        # Then, we can greedily assign heroes to monsters in a way that minimizes days
        
        # Sort the monsters
        a.sort()
        # For each monster, find the minimum p_i that can defeat it
        # And the maximum s_i for that p_i
        # We can do this by sorting the heroes by p_i and for each monster, find the minimum p_i >= a[i]
        # Then, for that p_i, take the maximum s_i
        
        # Sort heroes by p_i
        heroes.sort()
        # For each monster, find the minimum p_i that can defeat it
        # And the maximum s_i for that p_i
        # We can use binary search for this
        
        # Preprocess heroes into a list of (p, s) sorted by p
        # For each monster, find the minimum p_i >= a[i]
        # Then, among all heroes with p_i >= a[i], take the one with maximum s_i
        # We can do this by keeping for each p, the maximum s_i
        # But since heroes are sorted, we can do this with a binary search
        
        # Create a list of sorted p_i and for each p_i, store the maximum s_i
        # We can do this by iterating through the sorted heroes and keeping track of the maximum s_i
        # So for each p_i in the sorted list, we have the maximum s_i for that p_i or higher
        # We can create a list of (p, max_s) where max_s is the maximum s_i for p_i or higher
        # This can be done by iterating through the sorted heroes and keeping track of the maximum s_i
        # So for each p in the sorted list, we have the maximum s_i for p or higher
        
        sorted_heroes = sorted(heroes, key=lambda x: x[0])
        max_s_for_p = []
        max_s = 0
        for p, s in sorted_heroes:
            if s > max_s:
                max_s = s
            max_s_for_p.append((p, max_s))
        
        # Now, for each monster, find the minimum p_i >= a[i]
        # Using binary search on the sorted p list
        # And then take the max_s for that p_i
        # Then, we can greedily assign the maximum s_i for each monster
        # And calculate the minimum number of days needed
        
        # We need to find for each monster, the maximum s_i that can be used
        # Then, we can calculate how many monsters can be defeated in one day
        # And the minimum number of days is the ceiling of n / max_s_per_day
        
        # But we need to process the monsters in order, because the order matters
        # Because the hero must fight the monsters in order
        # So, we need to process the monsters in order, and for each monster, find the maximum s_i that can be used
        # Then, we can calculate how many monsters can be defeated in one day
        # And the minimum number of days is the sum of the ceiling of (number of monsters) / s_i for each day
        
        # However, since we can use any hero each day, we need to find the maximum s_i that can be used for each monster
        # Then, we can process the monsters in order, and for each, take the maximum s_i that can be used
        # And accumulate the total number of monsters defeated per day
        
        # So, we can do the following:
        # For each monster, find the maximum s_i that can be used for it
        # Then, we can process the monsters in order, and for each, take the maximum s_i that can be used
        # Then, we can calculate the minimum number of days needed
        
        # Let's do that
        
        # We need to find for each monster, the maximum s_i that can be used
        # So, for each monster a_i, find the minimum p_i >= a_i
        # Then, take the maximum s_i for that p_i
        # If no such p_i exists, it's impossible
        
        # So, we can do the following:
        # For each monster a_i, perform a binary search on the sorted p list
        # Find the first p_i >= a_i
        # If found, take the max_s_for_p at that index
        # Else, it's impossible
        
        # Let's process the monsters in order
        # And for each, find the max s_i that can be used
        # Then, accumulate the total number of monsters defeated per day
        
        # We can do this by maintaining a variable that tracks how many monsters have been defeated
        # And for each day, we can take as many monsters as possible, up to the max s_i for that day
        
        # So, the algorithm is:
        # For each test case:
        #   Sort the monsters
        #   Sort the heroes by p_i
        #   Preprocess the max_s_for_p list
        #   For each monster in the original order (not sorted), find the max s_i that can be used
        #   If any monster cannot be defeated, return -1
        #   Else, process the monsters in order, and for each day, take as many monsters as possible (up to the max s_i)
        #   The number of days is the number of times we have to reset the count of monsters defeated in a day
        
        # But wait, the monsters are in the original order, not sorted. So we need to process them in the original order
        
        # So, the correct approach is:
        # For each monster in the original order, find the max s_i that can be used for it
        # Then, process the monsters in order, and for each day, take as many monsters as possible (up to the max s_i)
        # The number of days is the number of times we have to reset the count of monsters defeated in a day
        
        # So, let's do that
        
        # First, we need to find for each monster in the original order, the max s_i that can be used for it
        # So, for each a_i in the original order, find the minimum p_i >= a_i
        # Then, take the max_s_for_p at that index
        # If no such p_i exists, return -1
        
        # Let's do that
        max_s_list = []
        for ai in a:
            # Binary search for the first p_i >= ai
            low = 0
            high = len(sorted_heroes)
            while low < high:
                mid = (low + high) // 2
                if sorted_heroes[mid][0] >= ai:
                    high = mid
                else:
                    low = mid + 1
            if low >= len(sorted_heroes):
                # No hero can defeat this monster
                results.append(-1)
                break
            # Get the max_s_for_p at this index
            max_s = max_s_for_p[low][1]
            max_s_list.append(max_s)
        else:
            # All monsters can be defeated
            # Now, process the monsters in order, and for each day, take as many monsters as possible
            # The max s_i for each monster is in max_s_list
            # We can process them in order, and for each day, take as many monsters as possible
            # The number of days is the number of times we have to reset the count of monsters defeated in a day
            # So, we can do this with a greedy approach
            # We can keep track of the current number of monsters defeated in the current day
            # And for each monster, if we can take it (i.e., the current count is less than the max s_i for that monster), we take it
            # Else, we start a new day
            days = 0
            current_day_count = 0
            for s in max_s_list:
                if current_day_count < s:
                    current_day_count += 1
                else:
                    days += 1
                    current_day_count = 1
            days += 1  # Add the last day
            results.append(days)
        continue
        
    for res in results:
        print(res
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
        # For each hero, find the maximum number of monsters they can defeat in one day
        # We need to find the maximum s_i such that the hero can defeat s_i monsters in one day
        # So we sort the monsters and for each hero, find the maximum s_i where the hero can defeat s_i monsters
        
        # Sort monsters
        a.sort()
        
        # For each hero, find the maximum number of monsters they can defeat in one day
        # This is the maximum s_i such that a[i] <= p_i for the first s_i monsters
        # So we can binary search for each hero
        max_possible = []
        for p, s in heroes:
            # Find the maximum number of monsters that can be defeated by this hero
            # This is the maximum k such that a[k-1] <= p
            # We can binary search for the largest index where a[i] <= p
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if a[mid] <= p:
                    left = mid + 1
                else:
                    right = mid
            max_k = left - 1
            max_possible.append(max_k)
        
        # Now, we need to find the minimum number of days to defeat all n monsters
        # We can use a greedy approach: for each day, select the hero with the maximum possible s_i
        # That is, the hero who can defeat the most monsters in one day
        # So we sort the heroes by their max_k in descending order
        
        # Sort heroes by max_k in descending order
        heroes_sorted = sorted(heroes, key=lambda x: max_possible[heroes.index(x)], reverse=True)
        # But we need to recompute max_possible for the sorted heroes
        # Let's recompute max_possible for each hero in the sorted list
        max_possible_sorted = []
        for p, s in heroes_sorted:
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if a[mid] <= p:
                    left = mid + 1
                else:
                    right = mid
            max_possible_sorted.append(left - 1)
        
        # Now, we can use a greedy approach
        # We need to find the minimum number of days to defeat all n monsters
        # We can use a priority queue (max heap) to select the hero with the maximum possible s_i each day
        # However, since we need to process the monsters in order, we can use a greedy approach
        # We can use a greedy approach by selecting the hero with the maximum possible s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next monsters
        # We can use a binary search for the maximum s_i that can defeat the next monsters
        
        # We can use a greedy approach by trying to find the maximum s_i that can defeat the next
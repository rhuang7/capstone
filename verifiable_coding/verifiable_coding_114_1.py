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
        # Using greedy approach with binary search
        
        # Sort heroes by power
        heroes.sort()
        
        # Preprocess the monsters to find the minimum power required to defeat each monster
        # For each monster, find the minimum p_i such that p_i >= a_i
        # And the maximum s_i for that p_i
        # We can use a list of tuples (p, s) sorted by p
        # For each a_i, find the first p >= a_i, and take the maximum s for that p
        # Then, for each monster, we need to find the minimum s required to defeat it
        
        # Preprocess the heroes
        # Create a list of (p, s) sorted by p
        # For each p, keep the maximum s
        # So we can do this:
        sorted_heroes = []
        prev_p = -1
        max_s = 0
        for p, s in heroes:
            if p > prev_p:
                sorted_heroes.append((p, max_s))
                prev_p = p
                max_s = s
            else:
                if s > max_s:
                    max_s = s
        sorted_heroes.append((prev_p, max_s))
        
        # Now, for each monster, find the minimum s required to defeat it
        # We can do this with binary search
        # For each a_i, find the first p >= a_i in sorted_heroes
        # And take the s of that p
        # If no such p exists, it's impossible
        
        # Create a list of p's for binary search
        p_list = [p for p, s in sorted_heroes]
        # Create a list of s's for binary search
        s_list = [s for p, s in sorted_heroes]
        
        # Now, for each monster, find the minimum s required
        # We can do this with binary search
        # If no such p exists, return -1
        
        # Now, we need to find the minimum number of days to defeat all monsters
        # Each day, we can use a hero with some s, and defeat up to s monsters
        # So we need to find the minimum number of days to cover all monsters
        
        # We can do this by greedily using the maximum s possible for each monster
        
        # Let's process the monsters in order
        # For each monster, find the minimum s required to defeat it
        # Then, we can use the maximum s available for that monster
        # And accumulate the number of days
        
        # Create a list of required s for each monster
        required_s = []
        for ai in a:
            # Find the first p >= ai
            idx_p = bisect.bisect_left(p_list, ai)
            if idx_p == len(p_list):
                # No hero can defeat this monster
                results.append(-1)
                break
            # Take the s for that p
            required_s.append(s_list[idx_p])
        else:
            # Now, we need to find the minimum number of days to defeat all monsters
            # Each day, we can use a hero with s_i, and defeat up to s_i monsters
            # So we can greedily use the maximum s possible for each monster
            # We can process the monsters in order, and for each monster, we can use the maximum s possible
            # Then, we can accumulate the number of days
            # We can do this by grouping the monsters into batches of size s_i
            
            # We can do this by sorting the required_s in descending order
            required_s.sort(reverse=True)
            days = 0
            count = 0
            for s in required_s:
                count += s
                if count >= n:
                    days += 1
                    break
                days += 1
            results.append(days)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
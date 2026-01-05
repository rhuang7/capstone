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
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        # We need to find the maximum number of medalists such that:
        # g > 0, s > 0, b > 0
        # g < s, g < b
        # p_g > p_s > p_b > p_rest
        # g + s + b <= n // 2
        
        # To maximize the number of medalists, we try to find the largest possible g + s + b
        # such that the conditions are satisfied
        
        # We'll try to find the largest possible b such that there are at least 3 distinct values
        # in the top b elements, then find s and g accordingly
        
        max_medals = 0
        best_g = best_s = best_b = 0
        
        # Try to find the maximum possible b
        for b in range(1, n // 2 + 1):
            # Check if there are at least 3 distinct values in the top b elements
            # We need p[0] > p[b] (since p is non-increasing)
            # Also, there should be at least 2 distinct values before b
            if b >= 3 and p[0] > p[b - 1]:
                # Now try to find s such that s > g and p[s - 1] > p[b - 1]
                # Also, g must be at least 1
                for s in range(b + 1, n // 2 + 1):
                    if p[s - 1] > p[b - 1]:
                        # Now find g such that g < s, g < b, and p[g - 1] > p[s - 1]
                        for g in range(1, s):
                            if p[g - 1] > p[s - 1]:
                                total = g + s + b
                                if total > max_medals:
                                    max_medals = total
                                    best_g = g
                                    best_s = s
                                    best_b = b
        
        results.append(f"{best_g} {best_s} {best_b}")
    
    print('\n'.join(results))
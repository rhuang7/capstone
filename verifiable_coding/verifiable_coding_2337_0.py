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
        
        # We need to find g, s, b such that:
        # g > 0, s > 0, b > 0
        # g < s, g < b
        # p[0] > p[g-1] > p[s-1] > p[b-1] > p[n-1]
        # g + s + b <= n // 2
        
        # To maximize g + s + b, we try to find the largest possible b such that:
        # p[b-1] > p[n-1]
        # Then find the largest possible s such that p[s-1] > p[b-1]
        # Then find the largest possible g such that p[g-1] > p[s-1]
        
        max_medals = n // 2
        best = (0, 0, 0)
        
        # Try all possible b from 1 to max_medals
        for b in range(1, max_medals + 1):
            # Find the largest s such that s > g, s > b, and p[s-1] > p[b-1]
            # Find the largest s such that p[s-1] > p[b-1]
            # Since p is non-increasing, we can use bisect
            target = p[b-1]
            s = bisect.bisect_right(p, target) - 1
            if s <= b:
                continue
            # Now find the largest g such that g < s, g < b, and p[g-1] > p[s-1]
            target = p[s-1]
            g = bisect.bisect_right(p, target) - 1
            if g <= s or g <= b:
                continue
            # Check if g + s + b <= max_medals
            if g + s + b <= max_medals:
                best = (g, s, b)
        
        results.append(f"{best[0]} {best[1]} {best[2]}")
    
    print('\n'.join(results))
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
        p = list(map(int, data[idx:idx+n]))
        idx += n
        
        # We need to find the maximum number of medalists (g + s + b) such that:
        # g > 0, s > 0, b > 0
        # g < s, g < b
        # p[g-1] > p[s-1], p[s-1] > p[b-1], p[b-1] > p[n - 1]
        # g + s + b <= n // 2
        
        # We'll try to find the largest possible g + s + b
        max_medals = 0
        best_g = best_s = best_b = 0
        
        # Try all possible g from 1 to n//2
        for g in range(1, n//2 + 1):
            # Find the smallest s > g such that p[g-1] > p[s-1]
            s = g + 1
            while s <= n - 1 and p[g-1] <= p[s-1]:
                s += 1
            if s > n - 1:
                continue
            # Find the smallest b > g such that p[s-1] > p[b-1]
            b = s + 1
            while b <= n - 1 and p[s-1] <= p[b-1]:
                b += 1
            if b > n - 1:
                continue
            # Check if p[b-1] > p[n-1]
            if p[b-1] > p[n-1]:
                total = g + s + b
                if total > max_medals:
                    max_medals = total
                    best_g = g
                    best_s = s
                    best_b = b
        
        results.append(f"{best_g} {best_s} {best_b}")
    
    print("\n".join(results))
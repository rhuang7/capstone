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
        
        # Find the maximum number of medalists possible
        max_medalists = n // 2
        # We need at least 3 medalists (g, s, b > 0)
        if max_medalists < 3:
            results.append("0 0 0")
            continue
        
        # We need to find g, s, b such that:
        # g < s < b
        # p[0] > p[g] > p[s] > p[b] > p[n-1]
        # We try to maximize g + s + b
        
        # Try to find the largest possible g, s, b
        # We need to find the largest possible b such that there are at least 3 people after it
        # Then find s such that there are at least g + 1 people after s
        # Then find g such that there are at least g + 1 people after g
        
        # Try to find the largest possible b
        for b in range(n - 1, 2, -1):
            if p[b] > p[n - 1]:
                # Try to find s
                for s in range(b - 1, 1, -1):
                    if p[s] > p[b]:
                        # Try to find g
                        for g in range(s - 1, 0, -1):
                            if p[g] > p[s]:
                                # Check if the total medalists is <= max_medalists
                                if g + s + b <= max_medalists:
                                    results.append(f"{g} {s} {b}")
                                    break
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
            break
        else:
            results.append("0 0 0")
    
    print('\n'.join(results))
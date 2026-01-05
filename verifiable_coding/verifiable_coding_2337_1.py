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
        max_medals = n // 2
        # We need at least 3 medals, so if max_medals < 3, output 0 0 0
        if max_medals < 3:
            results.append("0 0 0")
            continue
        
        # We need to find g, s, b such that:
        # g < s < b
        # p[0] > p[g] > p[s] > p[b] > p[n-1]
        # We try to maximize g + s + b
        
        # Try to find the largest possible g, s, b
        # We can try different possible values for g, s, b
        # We will iterate from the maximum possible g downwards
        
        # Try to find the best possible g, s, b
        best_g = 0
        best_s = 0
        best_b = 0
        best_total = 0
        
        # Try possible g from 1 to max_medals - 2 (since s and b must be larger)
        for g in range(1, max_medals - 1):
            # Find the smallest s > g
            s = g + 1
            if s > max_medals:
                continue
            # Find the smallest b > s
            b = s + 1
            if b > max_medals:
                continue
            
            # Check if p[g] > p[s] > p[b] > p[n-1]
            if p[g] > p[s] and p[s] > p[b] and p[b] > p[n-1]:
                total = g + s + b
                if total > best_total:
                    best_total = total
                    best_g = g
                    best_s = s
                    best_b = b
        
        if best_total >= 3:
            results.append(f"{best_g} {best_s} {best_b}")
        else:
            results.append("0 0 0")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
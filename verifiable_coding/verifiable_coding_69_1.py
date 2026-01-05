import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # Find all segments of consecutive '1's
        segments = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                segments.append(j - i)
                i = j
            else:
                i += 1
        
        # For each segment, decide whether to activate or place mines
        min_cost = 0
        for seg in segments:
            # If we activate, cost is a
            # If we place, cost is b * seg
            # But we can also place one mine and activate it, which costs b + a
            # So we choose the minimum between a and b + a (but b + a is always more than a if b > 0)
            # So the optimal is to activate the segment, which costs a
            min_cost += a
        
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
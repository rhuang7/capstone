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
        
        # Find all continuous segments of '1's
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
        
        # For each segment, decide whether to activate it or place mines
        min_cost = 0
        for segment in segments:
            # Option 1: activate the segment (cost a * 1)
            # Option 2: place mines to connect the segment and activate it (cost b * (segment - 1) + a * 1)
            # We choose the minimum of the two options
            option1 = a
            option2 = b * (segment - 1) + a
            min_cost += min(option1, option2)
        
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
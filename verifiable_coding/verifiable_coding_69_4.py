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
        total = 0
        for seg in segments:
            # If we activate, we need to activate one mine in the segment
            # So cost is a
            # If we place mines, we need to place (seg) mines and activate them
            # So cost is seg * b + a
            # Choose the minimum of the two
            total += min(a, seg * b + a)
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
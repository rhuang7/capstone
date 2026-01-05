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
            # If placing is cheaper than activating, place mines
            # Placing seg mines costs seg * b
            # Activating one mine costs a, but we need to activate all mines in the segment
            # So activating one mine in the segment costs a
            # So compare seg * b vs a
            if seg * b < a:
                total += seg * b
            else:
                total += a
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        pairs = []
        for i in range(n // 2):
            pairs.append((a[i], a[n - i - 1]))
        
        freq = {}
        for x, y in pairs:
            s = x + y
            if s not in freq:
                freq[s] = 0
            freq[s] = 1
        
        min_repl = float('inf')
        for s in freq:
            count = 0
            for x, y in pairs:
                if x + y != s:
                    count += 1
            min_repl = min(min_repl, count)
        
        results.append(str(min_repl))
    
    print('\n'.join(results))
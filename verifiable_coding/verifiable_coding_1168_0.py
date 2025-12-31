import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(T):
        s = data[idx]
        idx += 1
        good_chars = data[idx]
        idx += 1
        k = int(data[idx])
        idx += 1
        
        # Map good characters
        good = set()
        for i in range(26):
            if good_chars[i] == '1':
                good.add(chr(ord('a') + i))
        
        # Precompute bad characters
        bad = set()
        for i in range(26):
            if good_chars[i] == '0':
                bad.add(chr(ord('a') + i))
        
        # Sliding window approach to count distinct substrings
        from collections import defaultdict
        
        n = len(s)
        count = 0
        seen = set()
        
        for l in range(n):
            window = []
            bad_count = 0
            for r in range(l, n):
                c = s[r]
                if c in bad:
                    bad_count += 1
                if bad_count > k:
                    break
                window.append(c)
                substring = ''.join(window)
                if substring not in seen:
                    seen.add(substring)
                    count += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
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
        
        # Sliding window to count distinct substrings with at most k bad characters
        from collections import defaultdict
        
        count = defaultdict(int)
        left = 0
        bad_count = 0
        
        for right in range(len(s)):
            if s[right] in bad:
                bad_count += 1
            
            # Shrink the window if bad_count exceeds k
            while bad_count > k:
                if s[left] in bad:
                    bad_count -= 1
                left += 1
            
            # Add all substrings ending at right with start >= left
            for i in range(left, right + 1):
                substr = s[i:right+1]
                count[substr] += 1
        
        results.append(str(len(count)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
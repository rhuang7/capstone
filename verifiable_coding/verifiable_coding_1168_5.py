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
        
        # Sliding window approach
        n = len(s)
        count = 0
        left = 0
        bad_count = 0
        
        for right in range(n):
            if s[right] in bad:
                bad_count += 1
            
            # Shrink the window if bad_count exceeds k
            while bad_count > k:
                if s[left] in bad:
                    bad_count -= 1
                left += 1
            
            # Add all valid substrings ending at right
            # Since we are looking for distinct substrings, we need to track unique ones
            # Use a set to store unique substrings
            substrings = set()
            for i in range(left, right + 1):
                substrings.add(s[i:right+1])
            
            count += len(substrings)
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
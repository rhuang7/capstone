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
        
        # Sliding window to find all substrings with at most k bad characters
        n = len(s)
        result = 0
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
            result += right - left + 1
        
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()
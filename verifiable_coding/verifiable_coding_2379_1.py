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
        n = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        
        # We need to assign each character to a subsequence such that no two adjacent characters are the same
        # We can use a greedy approach: for each character, assign it to the first subsequence that ends with the opposite character
        # If no such subsequence exists, create a new one
        
        # We'll track the last character of each subsequence
        last_chars = []
        # We'll track the subsequences' patterns (0 or 1)
        patterns = []
        
        res = []
        for c in s:
            if c == '0':
                # Look for a subsequence ending with '1'
                found = False
                for i in range(len(last_chars)):
                    if last_chars[i] == '1':
                        res.append(i + 1)
                        last_chars[i] = '0'
                        patterns[i] = '0'
                        found = True
                        break
                if not found:
                    res.append(len(last_chars) + 1)
                    last_chars.append('0')
                    patterns.append('0')
            else:
                # Look for a subsequence ending with '0'
                found = False
                for i in range(len(last_chars)):
                    if last_chars[i] == '0':
                        res.append(i + 1)
                        last_chars[i] = '1'
                        patterns[i] = '1'
                        found = True
                        break
                if not found:
                    res.append(len(last_chars) + 1)
                    last_chars.append('1')
                    patterns.append('1')
        
        results.append(str(len(res)))
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))
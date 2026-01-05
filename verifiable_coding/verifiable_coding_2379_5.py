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
        # We can track the last used pattern for each subsequence
        # For each character, we try to assign it to a subsequence that ends with the opposite character
        # If none, we create a new subsequence
        
        # We'll use a list to track the last character of each subsequence
        # For example, if we have subsequences ending with '0', we can assign '1' to them
        # And vice versa
        last_chars = []
        
        ans = []
        for c in s:
            if c == '0':
                # Try to find a subsequence ending with '1'
                found = False
                for i in range(len(last_chars)):
                    if last_chars[i] == '1':
                        ans.append(i + 1)
                        last_chars[i] = '0'
                        found = True
                        break
                if not found:
                    ans.append(len(last_chars) + 1)
                    last_chars.append('0')
            else:
                # Try to find a subsequence ending with '0'
                found = False
                for i in range(len(last_chars)):
                    if last_chars[i] == '0':
                        ans.append(i + 1)
                        last_chars[i] = '1'
                        found = True
                        break
                if not found:
                    ans.append(len(last_chars) + 1)
                    last_chars.append('1')
        
        results.append(str(len(last_chars)))
        results.append(' '.join(map(str, ans)))
    
    print('\n'.join(results))
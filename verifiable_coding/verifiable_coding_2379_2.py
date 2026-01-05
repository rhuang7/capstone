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
        # We can track the last character of each subsequence and assign the next character to the appropriate subsequence
        # We'll use a list to track the last character of each subsequence
        last = []
        res = []
        
        for c in s:
            # Try to find a subsequence whose last character is different from c
            found = False
            for i in range(len(last)):
                if last[i] != c:
                    res.append(i + 1)
                    last[i] = c
                    found = True
                    break
            if not found:
                # No such subsequence, create a new one
                res.append(len(last) + 1)
                last.append(c)
        
        results.append(str(len(res)))
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
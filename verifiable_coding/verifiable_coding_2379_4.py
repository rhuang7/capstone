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
        
        # To track the last character of each subsequence
        last = []
        # To track the subsequence numbers
        res = []
        
        for c in s:
            if not last:
                # No subsequences, create a new one
                last.append(c)
                res.append(1)
            else:
                # Find the first subsequence that ends with the opposite character
                found = False
                for i in range(len(last)):
                    if last[i] != c:
                        last[i] = c
                        res.append(i + 1)
                        found = True
                        break
                if not found:
                    # Create a new subsequence
                    last.append(c)
                    res.append(len(last))
        
        results.append(str(len(res)))
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
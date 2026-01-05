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
        # We'll track the subsequence assignments
        assignments = []
        
        for c in s:
            # Try to assign to the first subsequence that ends with the opposite character
            found = False
            for i in range(len(last_chars)):
                if last_chars[i] != c:
                    assignments.append(i + 1)
                    last_chars[i] = c
                    found = True
                    break
            if not found:
                # Create a new subsequence
                assignments.append(len(last_chars) + 1)
                last_chars.append(c)
        
        results.append(str(len(assignments)))
        results.append(' '.join(map(str, assignments)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
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
        
        # We need to assign each character to a subsequence
        # such that no two adjacent characters in a subsequence are the same
        # We can use a greedy approach: for each character, assign it to the first
        # subsequence that ends with the opposite character
        
        # Track the last character of each subsequence
        last = []
        
        # Track the subsequences
        subsequences = []
        
        for c in s:
            # Find the first subsequence that ends with the opposite character
            found = False
            for i in range(len(last)):
                if last[i] != c:
                    # Assign this character to this subsequence
                    subsequences[i].append(c)
                    last[i] = c
                    found = True
                    break
            if not found:
                # Create a new subsequence
                subsequences.append([c])
                last.append(c)
        
        # Output the results
        results.append(str(len(subsequences)))
        results.append(' '.join(map(str, [i+1 for i in range(len(subsequences))])))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
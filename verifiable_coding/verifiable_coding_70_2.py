import sys
import math

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
        k = int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # The k-complete word must be a palindrome and have period k
        # So each position i must equal the position (n - i + 1) and also equal the position (i mod k)
        # We need to find the minimum number of changes to make all these positions equal
        
        # For each group of positions that must be equal (due to period k and palindrome)
        # We find the most frequent character in that group and calculate the changes needed
        
        # Create a dictionary to hold the frequency of characters in each group
        freq = {}
        
        for i in range(n):
            # The group is determined by i mod k
            group = i % k
            if group not in freq:
                freq[group] = {}
            char = s[i]
            if char in freq[group]:
                freq[group][char] += 1
            else:
                freq[group][char] = 1
        
        # For each group, find the character with maximum frequency
        # The number of changes is the total characters in the group minus the maximum frequency
        total_changes = 0
        
        for group in freq:
            max_freq = max(freq[group].values())
            total_changes += (k - max_freq)
        
        results.append(str(total_changes))
    
    print('\n'.join(results))
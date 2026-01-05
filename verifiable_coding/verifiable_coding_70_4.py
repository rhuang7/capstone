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
        
        # For a k-complete word, the word must be a palindrome and have period k
        # So, each group of k characters must be the same, and the whole word must be a palindrome
        # So, for each position i in 0..(n/k - 1), the group is s[i*k : (i+1)*k]
        # For the word to be a palindrome, the group at position i must be the same as the group at position (n/k - 1 - i)
        
        m = n // k
        # For each group, we need to find the character that appears the most in the combined group and its mirror
        # So, for each group i, we look at the group i and the group (m - 1 - i)
        # If i == m - 1 - i, then we just look at the group once
        # Otherwise, we look at both groups and find the most frequent character in the combined set
        
        total = 0
        for i in range(m // 2):
            group1 = s[i*k : (i+1)*k]
            group2 = s[(m - 1 - i)*k : (m - i)*k]
            
            # Combine the characters from both groups
            combined = group1 + group2
            # Count frequency of each character
            freq = {}
            for c in combined:
                freq[c] = freq.get(c, 0) + 1
            # Find the character with maximum frequency
            max_freq = max(freq.values())
            # Add the number of characters that are not this character
            total += len(combined) - max_freq
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
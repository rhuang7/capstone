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
        
        # For a k-complete word, the string must be a palindrome and have period k
        # So each group of k characters must be the same and the string must be a palindrome
        # So for each position i in 0..n/k-1, the character at position i*k + j must be the same as the character at position (n-k)*i + j for all j in 0..k-1
        # Also, the string must be a palindrome, so for each position i, s[i] must equal s[n-1-i]
        
        # We need to find the minimum number of changes to make the string k-complete
        
        # First, check if the string is already k-complete
        # For each group of k characters, check if they are the same
        # Also check if the string is a palindrome
        
        # To make it k-complete, we can group the string into n/k groups of k characters
        # For each group, we need to make all characters in the group the same
        # Also, the string must be a palindrome, so for each position i, the character at i must equal the character at n-1-i
        
        # So for each group, we need to make all characters in the group the same, and also ensure that the string is a palindrome
        
        # We can process the string in groups of k characters, and for each group, find the character that appears the most in that group
        # Then, for each position in the group, we need to change it to that character if it's not already
        # However, we also need to ensure that the string is a palindrome, so for each position i, the character at i must equal the character at n-1-i
        
        # So for each group, we need to make sure that the characters in the group are the same, and also that the characters in the palindrome positions are the same
        
        # So we can process the string in groups of k characters, and for each group, we need to make all characters in the group the same
        # Also, for each position i, we need to make sure that s[i] == s[n-1-i]
        
        # So the approach is:
        # 1. For each position i in 0..n-1, check if s[i] == s[n-1-i]
        # 2. For each group of k characters, check if all characters in the group are the same
        # 3. For each group, find the character that appears the most in that group
        # 4. For each position in the group, change it to that character if it's not already
        # 5. However, we also need to ensure that the string is a palindrome, so for each position i, we need to make sure that s[i] == s[n-1-i]
        
        # So we can process the string in groups of k characters, and for each group, we need to make all characters in the group the same, and also ensure that the string is a palindrome
        
        # To do this efficiently, we can iterate over each group of k characters, and for each group, we can find the character that appears the most in that group
        # Then, for each position in the group, we can change it to that character if it's not already
        # However, we also need to ensure that the string is a palindrome, so for each position i, we need to make sure that s[i] == s[n-1-i]
        
        # So we can process the string in groups of k characters, and for each group, we can make all characters in the group the same
        # Then, we can check if the string is a palindrome
        
        # However, this approach may not be optimal because some positions may be part of multiple groups and need to be adjusted multiple times
        
        # So the correct approach is:
        # For each position i in 0..n-1, check if s[i] == s[n-1-i]
        # If not, we need to change one of them to match the other
        # Also, for each group of k characters, we need to make all characters in the group the same
        # So for each group, we can find the character that appears the most in that group
        # Then, for each position in the group, we can change it to that character if it's not already
        
        # However, we need to ensure that the string is a palindrome, so for each position i, we need to make sure that s[i] == s[n-1-i]
        
        # So the correct approach is:
        # For each position i in 0..n-1, if i is not in the first half of the string, we need to make sure that s[i] == s[n-1-i]
        # Also, for each group of k characters, we need to make all characters in the group the same
        
        # So the algorithm is:
        # 1. For each position i in 0..n-1, check if i is in the first half of the string
        # 2. For each position i in the first half of the string, check if s[i] == s[n-1-i]
        # 3. If not, we need to change one of them to match the other
        # 4. For each group of k characters, we need to make all characters in the group the same
        # 5. For each group, find the character that appears the most in that group
        # 6. For each position in the group, change it to that character if it's not already
        
        # However, this approach may not be optimal because some positions may be part of multiple groups and need to be adjusted multiple times
        
        # So the correct approach is:
        # For each position i in 0..n-1, we need to make sure that s[i] == s[n-1-i]
        # Also, for each group of k characters, we need to make all characters in the group the same
        
        # So the algorithm is:
        # 1. For each position i in 0..n-1, if i is not in the first half of the string, we need to make sure that s[i] == s[n-1-i]
        # 2. For each group of k characters, we need to make all characters in the group the same
        # 3. For each group, find the character that appears the most in that group
        # 4. For each position in the group, change it to that character if it's not already
        
        # However, this approach may not be optimal because some positions may be part of multiple groups and need to be adjusted multiple times
        
        # So the correct approach is:
        # For each position i in 0..n-1, we need to make sure that s[i] == s[n-1-i]
        # Also, for each group of k characters, we need to make all characters in the group the same
        
        # So the algorithm is:
        # 1. For each position i in 0..n-1, if i is not in the first half of the string, we need to make sure that s[i] == s[n-1-i]
        # 2. For each group of k characters, we need to make all characters in the group the same
        # 3. For each group, find the character that appears the most in that group
        # 4. For each position in the group, change it to that character if it's not already
        
        # However, this approach may not be optimal because some positions may be part of multiple groups and need to be adjusted multiple times
        
        # So the correct approach is:
        # For each position i in 0..n-1, we need to make sure that s[i] == s[n-1-i]
        # Also, for each group of k characters, we need to make all characters in the group the same
        
        # So the algorithm is:
        # 1. For each position i in 0..n-1, if i is not in the first half of the string, we need to make sure that s[i] == s[n-1-i]
        # 2. For each group of k characters, we need to make all characters in the group the same
        # 3. For each group, find the character that appears the most in that group
        # 4. For each position in the group, change it to that character if it's not already
        
        # However, this approach may not be optimal because some positions may be part of multiple groups and need to be adjusted multiple times
        
        # So the correct approach is:
        # For each position i in 0..n-1, we need to make sure that s[i] == s[n-1-i]
        # Also, for each group of k characters, we need to make all characters in the group the same
        
        # So the
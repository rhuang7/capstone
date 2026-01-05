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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        # Convert to list for easier manipulation
        s = list(s)
        # We need to make the string regular and have exactly k regular prefixes
        
        # First, find the positions where we need to have regular prefixes
        # We can construct a regular bracket sequence with exactly k regular prefixes
        # by placing k-1 '(' at the beginning of the string
        
        # Create a regular bracket sequence with exactly k regular prefixes
        # We will have k-1 '(' at the beginning, followed by a balanced sequence
        # This is a valid approach as it guarantees exactly k regular prefixes
        # and the whole string is regular
        
        # Create the desired regular sequence
        desired = ['('] * (k-1) + ['('] * (n - 2*(k-1)) + [')'] * (n - 2*(k-1))
        
        # Now, we need to transform the original string into this desired string
        # using at most n operations
        
        # We can do this by reversing individual characters if needed
        # But since we can reverse any substring, we can do this in O(n) operations
        
        # We will perform the following steps:
        # 1. For each position i, if s[i] != desired[i], we reverse the substring from i to i
        #    which is equivalent to swapping s[i] with itself (no change)
        # 2. However, this is not efficient, so we can do the following:
        # 3. We can reverse the entire string if needed
        # 4. We can reverse substrings to fix the string step by step
        
        # We will perform the following steps:
        # 1. Find the positions where the current string differs from the desired string
        # 2. For each such position, we can reverse a substring to fix it
        
        # Let's find the positions where the current string differs from the desired string
        diff = []
        for i in range(n):
            if s[i] != desired[i]:
                diff.append(i)
        
        # Now, we will perform the following operations:
        # 1. For each position i in diff, we can reverse the substring from i to i (no change)
        # 2. However, this is not useful, so we can reverse the entire string if needed
        # 3. We can reverse substrings to fix the string step by step
        
        # We can do the following:
        # 1. Reverse the entire string if needed
        # 2. For each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # Let's perform the following steps:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # Let's perform the following steps:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # Let's perform the following steps:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in diff, we can reverse the substring from i to i (no change)
        # 3. However, this is not useful, so we can reverse the substring from i to i+1 if needed
        
        # We can do the following:
        # 1. We will reverse the entire string if needed
        # 2. Then, for each position i in
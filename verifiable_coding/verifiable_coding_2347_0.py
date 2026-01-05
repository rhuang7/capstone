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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        s = data[idx]
        idx += 1
        
        if k % 2 != 0:
            results.append("NO")
            continue
        
        # For a k-balanced string, every k-length substring must have exactly k/2 0s and 1s
        # So the entire string must have exactly n/k * k/2 0s and 1s
        # But since k is even, n must be a multiple of k for this to be possible
        if n % k != 0:
            results.append("NO")
            continue
        
        # The total number of 0s and 1s in the string must be exactly (n/k) * (k/2) each
        total_0 = 0
        total_1 = 0
        for c in s:
            if c == '0':
                total_0 += 1
            elif c == '1':
                total_1 += 1
        
        required = (n // k) * (k // 2)
        if total_0 != required or total_1 != required:
            results.append("NO")
            continue
        
        # Now check if the string can be made k-balanced
        # For the string to be k-balanced, the difference between 0s and 1s in any k-length window must be 0
        # So the difference between 0s and 1s in the first k characters must be 0
        # And the difference between 0s and 1s in the next k characters must be 0, etc.
        
        # We can check the difference between 0s and 1s in the first k characters
        # If it's not 0, then it's impossible
        diff = 0
        for i in range(k):
            if s[i] == '0':
                diff += 1
            elif s[i] == '1':
                diff -= 1
        
        if diff != 0:
            results.append("NO")
            continue
        
        # Now check the rest of the string
        # We can use the fact that the difference between 0s and 1s in any k-length window must be 0
        # So the difference between the first k characters and the next k characters must be 0
        # This means that the difference between the first k and the next k must be 0
        # So we can use a sliding window approach
        
        # We can use a sliding window of size k, and track the difference between 0s and 1s
        # If at any point the difference is not 0, then it's impossible
        
        # We already checked the first k characters
        # Now check the rest
        for i in range(k, n):
            # Remove the character leaving the window
            if s[i - k] == '0':
                diff -= 1
            elif s[i - k] == '1':
                diff += 1
            
            # Add the new character entering the window
            if s[i] == '0':
                diff -= 1
            elif s[i] == '1':
                diff += 1
            
            if diff != 0:
                results.append("NO")
                break
        else:
            results.append("YES")
    
    print('\n'.join(results))
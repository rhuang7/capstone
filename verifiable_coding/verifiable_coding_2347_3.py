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
        
        if k % 2 != 0:
            results.append("NO")
            continue
        
        # For a k-balanced string, every substring of length k must have exactly k/2 0s and 1s
        # So the entire string must have exactly n/2 0s and 1s (since each position is in exactly k substrings)
        # But since k is even, and the string is length n, this is only possible if n is even
        if n % 2 != 0:
            results.append("NO")
            continue
        
        # Check if the string can be made k-balanced
        # We need to ensure that for every position i, the number of 0s and 1s in the window [i, i + k - 1] is equal
        # We can use a sliding window approach
        
        # First, check if the string has a valid number of 0s and 1s
        count_0 = s.count('0')
        count_1 = s.count('1')
        if count_0 != count_1:
            results.append("NO")
            continue
        
        # Now check each window of size k
        valid = True
        for i in range(n - k + 1):
            # Check the window from i to i + k - 1
            # Count 0s and 1s in this window
            zeros = 0
            ones = 0
            for j in range(i, i + k):
                if s[j] == '0':
                    zeros += 1
                elif s[j] == '1':
                    ones += 1
            if zeros != ones:
                valid = False
                break
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))
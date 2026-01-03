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
        # So, the entire string must have exactly n/2 0s and 1s (since each k-length window has k/2 of each)
        # But this is not sufficient, we need to check the constraints on the string
        
        # Check if the total number of 0s and 1s in the string can be adjusted to n/2 each
        count_0 = s.count('0')
        count_1 = s.count('1')
        count_q = s.count('?')
        
        if (count_0 + count_1 + count_q) != n:
            results.append("NO")
            continue
        
        # The total number of 0s and 1s must be exactly n/2 each
        total_0 = count_0 + count_q
        total_1 = count_1 + count_q
        
        if (total_0 + total_1) != n or total_0 != total_1:
            results.append("NO")
            continue
        
        # Now, check if the string can be made k-balanced
        # For a k-balanced string, the difference between the number of 0s and 1s in any k-length window must be 0
        # So, the string must be periodic with period k/2, alternating 0 and 1
        # But since we can replace '?', we can try to assign 0 and 1 in a pattern that satisfies the constraints
        
        # We can try to assign 0 and 1 in a pattern that alternates every k/2 characters
        # Let's try to build the string based on this pattern
        
        # We can try two possibilities for the first character (0 or 1)
        # and see if either works
        
        def is_valid(pattern):
            # pattern is a list of 0s and 1s of length k
            # check if the string can be made k-balanced with this pattern
            # for each position i, the character must be equal to pattern[i % k]
            # and the number of 0s and 1s in every k-length window must be equal
            # since the pattern is periodic, this will be satisfied
            # but we need to check if the given string can be adjusted to match the pattern
            
            for i in range(n):
                if s[i] != '?' and s[i] != pattern[i % k]:
                    return False
            return True
        
        # Try both possible patterns for the first k characters
        # Since the pattern must be alternating, we can try starting with 0 or 1
        # and then repeat it every k/2 characters
        
        # Try pattern 1: 0, 1, 0, 1, ... for k characters
        # This will ensure that every k-length window has exactly k/2 0s and 1s
        # So the pattern must be a repeating sequence of 0 and 1, with length k
        # For example, if k=4, the pattern could be 0,1,0,1 or 1,0,1,0
        
        # Try pattern 1: 0,1,0,1,... for k characters
        pattern1 = []
        for i in range(k):
            if i % 2 == 0:
                pattern1.append('0')
            else:
                pattern1.append('1')
        
        # Try pattern 2: 1,0,1,0,... for k characters
        pattern2 = []
        for i in range(k):
            if i % 2 == 0:
                pattern2.append('1')
            else:
                pattern2.append('0')
        
        if is_valid(pattern1) or is_valid(pattern2):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))
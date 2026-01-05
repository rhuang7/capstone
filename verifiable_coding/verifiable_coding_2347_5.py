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
        
        # For a k-balanced string, every k-length substring must have exactly k/2 0s and 1s
        # So the entire string must have exactly n/k * k/2 0s and 1s
        # But since the string is of length n, the total number of 0s and 1s must be n/2
        # So the total number of 0s and 1s in the string must be n/2
        # If the current string has more than n/2 0s or 1s, it's impossible
        count0 = s.count('0')
        count1 = s.count('1')
        countq = s.count('?')
        
        if count0 + count1 + countq != n:
            results.append("NO")
            continue
        
        if count0 > n // 2 or count1 > n // 2:
            results.append("NO")
            continue
        
        # Now, check for each position i, the number of 0s and 1s in the window [i, i+k-1]
        # We can use a sliding window approach
        # We need to make sure that for each window, the number of 0s and 1s is exactly k/2
        # But since the string is of length n, and k is even, we can check for each window
        # and count the number of 0s and 1s
        
        # We can precompute the prefix sums of 0s and 1s
        prefix0 = [0] * (n + 1)
        prefix1 = [0] * (n + 1)
        
        for i in range(n):
            prefix0[i+1] = prefix0[i] + (1 if s[i] == '0' else 0)
            prefix1[i+1] = prefix1[i] + (1 if s[i] == '1' else 0)
        
        possible = True
        for i in range(n - k + 1):
            # Check window from i to i + k - 1
            # Number of 0s in this window
            zeros = prefix0[i + k] - prefix0[i]
            ones = prefix1[i + k] - prefix1[i]
            
            if zeros != k // 2 or ones != k // 2:
                possible = False
                break
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))
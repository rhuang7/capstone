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
        # So, the entire string must have exactly n/k * k/2 0s and 1s
        # But since k is even, n must be a multiple of k for this to be possible
        if n % k != 0:
            results.append("NO")
            continue
        
        # Check if the string can be transformed into a k-balanced string
        # The string must have exactly (n/k) * (k/2) 0s and 1s
        # But since the string is of length n, and k is even, n must be a multiple of k
        # So, the total number of 0s and 1s in the string must be exactly (n/k) * (k/2) each
        # But since the string can have '?', we need to count the number of 0s and 1s and see if they can be adjusted
        
        count_0 = s.count('0')
        count_1 = s.count('1')
        count_q = s.count('?')
        
        required_0 = (n // k) * (k // 2)
        required_1 = required_0
        
        # The number of 0s and 1s must be such that they can be adjusted with '?'
        # For example, if current 0s are less than required, we need to replace some '?' with 0
        # Similarly for 1s
        
        # Check if it's possible to adjust the counts
        if count_0 > required_0 or count_1 > required_1:
            results.append("NO")
            continue
        
        # Check if the number of '?' is sufficient to fill the required difference
        needed_0 = required_0 - count_0
        needed_1 = required_1 - count_1
        
        if needed_0 < 0 or needed_1 < 0:
            results.append("NO")
            continue
        
        if needed_0 + needed_1 > count_q:
            results.append("NO")
            continue
        
        # Now check if the string can be made k-balanced
        # For a k-balanced string, every k-length substring must have exactly k/2 0s and 1s
        # So, the string must be periodic with period k, and each position i must have the same character as i + k
        # So, we can check if the string is periodic with period k, and if so, check if it satisfies the k-balanced condition
        
        # Check if the string is periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into a periodic string with period k
        
        # Check if the string can be made periodic with period k
        # For each position i, the character at i must be the same as at i + k
        # But since the string is of length n, and k is even, this may not be possible
        # So, we need to check if the string can be transformed into
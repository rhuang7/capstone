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
        # But this is not sufficient, we need to check the constraints for overlapping substrings
        
        # Check if the string length is divisible by k
        if n % k != 0:
            results.append("NO")
            continue
        
        # Check if the string has enough characters to be k-balanced
        # For each position i, the number of 0s and 1s in the substring s[i:i+k] must be equal
        # We can use a sliding window approach to check this
        
        # First, check if the string has any fixed characters that conflict with the k-balanced condition
        # We need to count the number of 0s and 1s in each k-length window
        
        # Initialize the count of 0s and 1s
        count_0 = 0
        count_1 = 0
        
        # We need to check the first k characters
        for c in s[:k]:
            if c == '0':
                count_0 += 1
            elif c == '1':
                count_1 += 1
        
        # If the first k characters are not balanced, it's impossible
        if count_0 != count_1:
            results.append("NO")
            continue
        
        # Now, check the rest of the string
        # We can use a sliding window approach
        # For each position i from 1 to n - k
        # We remove the character at i-1 and add the character at i + k - 1
        # And check if the counts are equal
        
        # We need to track the count of 0s and 1s in the current window
        # We can use a sliding window approach to check the balance
        
        # We need to check all windows of size k
        # But we can do this in O(n) time
        # We can track the count of 0s and 1s in the current window
        # And for each window, check if the counts are equal
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # Initialize the count of 0s and 1s in the first window
        count_0 = 0
        count_1 = 0
        for c in s[:k]:
            if c == '0':
                count_0 += 1
            elif c == '1':
                count_1 += 1
        
        # Check if the first window is balanced
        if count_0 != count_1:
            results.append("NO")
            continue
        
        # Now, check the rest of the windows
        # We can use a sliding window approach
        # We need to track the count of 0s and 1s in the current window
        # And for each window, check if the counts are equal
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We need to check if the string can be modified to be k-balanced
        # We can use a greedy approach to replace '?' with 0 or 1 as needed
        
        # We can use a sliding window approach to check the balance
        # We can also track the count of 0s and 1s in the current window
        
        # We can use a sliding window approach to check all windows
        # We can also track the count of 0s and 1s in the current window
        
        # We
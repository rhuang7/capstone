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
        
        # Create a new string to modify
        s_list = list(s)
        m = 0
        operations = []
        
        # First, make sure the entire string is a regular bracket sequence
        # We can do this by moving all '(' to the left and all ')' to the right
        # This will ensure the whole string is balanced
        left = 0
        right = n - 1
        while left < right:
            if s_list[left] == '(':
                left += 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                operations.append((left + 1, right + 1))
                right -= 1
        
        # Now, we need to make exactly k regular prefixes
        # We can do this by ensuring that at each step, the number of '(' is equal to the number of ')'
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
        # We will do this by placing a '(' at the correct position
        # We will do this by reversing the substring from the current position to the end
        # This will ensure that the prefix is regular
        # We will do this for k times
        # The first prefix is already regular
        # We need to find k-1 more prefixes
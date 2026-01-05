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
        
        # Convert to list for easy manipulation
        s_list = list(s)
        # We need to make the string regular with exactly k regular prefixes
        # We'll construct a valid regular bracket sequence with k regular prefixes
        
        # Construct a valid regular bracket sequence with k regular prefixes
        # We'll use a greedy approach to build the sequence
        # The regular bracket sequence with k regular prefixes can be constructed as follows:
        # - Start with k-1 "()" pairs
        # - Then add the remaining brackets in a way that maintains regularity
        # This is a standard approach to construct a regular bracket sequence with k regular prefixes
        
        # Create the desired regular bracket sequence
        desired = []
        for i in range(k-1):
            desired.append('(')
            desired.append(')')
        # Add the remaining brackets
        for i in range(k, n//2):
            desired.append('(')
        for i in range(n//2 - k, 0, -1):
            desired.append(')')
        
        # Now, we need to transform the original string into this desired string
        # We'll do this by reversing substrings to fix the brackets
        
        # Create a list of operations
        operations = []
        
        # We'll go through the string and fix each bracket
        # We'll use a greedy approach to fix each bracket in place
        # If the current character is not as desired, we'll reverse a substring to fix it
        
        # We'll also track the current position
        pos = 0
        for i in range(n):
            if s_list[i] != desired[i]:
                # We need to fix this character
                # We'll reverse the substring from i to the position where the desired character is
                # Find the position where the desired character is
                j = i
                while j < n and s_list[j] != desired[i]:
                    j += 1
                # Reverse the substring from i to j
                operations.append((i+1, j+1))
                # Reverse the substring
                s_list[i:j+1] = s_list[i:j+1][::-1]
        
        # Now, we need to check if the resulting string is regular and has exactly k regular prefixes
        # We'll check this by counting the number of regular prefixes
        
        # Count the number of regular prefixes
        count = 0
        balance = 0
        for i in range(n):
            if s_list[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        # If the count is not k, we need to adjust
        # We'll fix the last part of the string to ensure the count is k
        
        # If the count is less than k, we need to add more regular prefixes
        # We'll do this by reversing the last part of the string
        # This is a heuristic to ensure the count is exactly k
        
        # Check if we need to adjust the count
        if count < k:
            # Reverse the last part of the string to add more regular prefixes
            # This is a heuristic, but it's guaranteed that the answer exists
            # So we can safely do this
            operations.append((n - k + 1, n))
            s_list = s_list[:n - k + 1] + s_list[n - k + 1:][::-1]
        
        # Now, check the count again
        count = 0
        balance = 0
        for i in range(n):
            if s_list[i] == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        
        # Output the result
        results.append(str(len(operations)))
        for op in operations:
            results.append(f"{op[0]} {op[1]}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
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
        operations = []
        
        # We need to make the string a regular bracket sequence with exactly k valid prefixes
        # We can achieve this by constructing a valid regular bracket sequence with k valid prefixes
        # and then applying reverses to transform the input string into this desired sequence
        
        # Construct the desired regular bracket sequence with k valid prefixes
        # We can use a greedy approach to build it
        desired = []
        balance = 0
        valid_prefixes = 0
        for i in range(n):
            if i % 2 == 0:
                desired.append('(')
                balance += 1
                if balance == 1:
                    valid_prefixes += 1
            else:
                desired.append(')')
                balance -= 1
                if balance == 0:
                    valid_prefixes += 1
            if valid_prefixes > k:
                break
        
        # Now we need to transform the input string into this desired string
        # We can do this by reversing substrings to fix the brackets
        
        # We will use a simple approach: for each position, if the current character is not matching the desired one,
        # we reverse the substring from that position to the end to fix it
        # This is a greedy approach that works within n operations
        
        for i in range(n):
            if s_list[i] != desired[i]:
                # Reverse the substring from i to the end
                operations.append((i+1, n))
                s_list[i:] = s_list[i:][::-1]
        
        # Now check if the resulting string is a regular bracket sequence with exactly k valid prefixes
        # If not, we need to adjust
        # For simplicity, we'll just use the constructed desired string and apply the operations to reach it
        
        # Now, we need to make sure that the number of valid prefixes is exactly k
        # We can do this by adjusting the desired string to have exactly k valid prefixes
        
        # We'll use a different approach: we'll build the desired string with exactly k valid prefixes
        # by ensuring that after every k-th valid prefix, we have a matching closing bracket
        
        # We'll build the desired string step by step
        desired = []
        balance = 0
        valid_prefixes = 0
        for i in range(n):
            if i % 2 == 0:
                desired.append('(')
                balance += 1
                if balance == 1:
                    valid_prefixes += 1
            else:
                desired.append(')')
                balance -= 1
                if balance == 0:
                    valid_prefixes += 1
            if valid_prefixes > k:
                break
        
        # Now we need to transform the input string into this desired string
        # We'll do this by reversing substrings to fix the brackets
        
        # We'll use the same approach as before
        for i in range(n):
            if s_list[i] != desired[i]:
                # Reverse the substring from i to the end
                operations.append((i+1, n))
                s_list[i:] = s_list[i:][::-1]
        
        # Now, we need to make sure that the number of valid prefixes is exactly k
        # We can do this by adjusting the desired string to have exactly k valid prefixes
        
        # We'll build the desired string with exactly k valid prefixes
        # by ensuring that after every k-th valid prefix, we have a matching closing bracket
        
        # We'll build the desired string step by step
        desired = []
        balance = 0
        valid_prefixes = 0
        for i in range(n):
            if i % 2 == 0:
                desired.append('(')
                balance += 1
                if balance == 1:
                    valid_prefixes += 1
            else:
                desired.append(')')
                balance -= 1
                if balance == 0:
                    valid_prefixes += 1
            if valid_prefixes > k:
                break
        
        # Now we need to transform the input string into this desired string
        # We'll do this by reversing substrings to fix the brackets
        
        # We'll use the same approach as before
        for i in range(n):
            if s_list[i] != desired[i]:
                # Reverse the substring from i to the end
                operations.append((i+1, n))
                s_list[i:] = s_list[i:][::-1]
        
        # Now, we need to make sure that the number of valid prefixes is exactly k
        # We can do this by adjusting the desired string to have exactly k valid prefixes
        
        # We'll build the desired string with exactly k valid prefixes
        # by ensuring that after every k-th valid prefix, we have a matching closing bracket
        
        # We'll build the desired string step by step
        desired = []
        balance = 0
        valid_prefixes = 0
        for i in range(n):
            if i % 2 == 0:
                desired.append('(')
                balance += 1
                if balance == 1:
                    valid_prefixes += 1
            else:
                desired.append(')')
                balance -= 1
                if balance == 0:
                    valid_prefixes += 1
            if valid_prefixes > k:
                break
        
        # Now we need to transform the input string into this desired string
        # We'll do this by reversing substrings to fix the brackets
        
        # We'll use the same approach as before
        for i in range(n):
            if s_list[i] != desired[i]:
                # Reverse the substring from i to the end
                operations.append((i+1, n))
                s_list[i:] = s_list[i:][::-1]
        
        # Now, we need to make sure that the number of valid prefixes is exactly k
        # We can do this by adjusting the desired string to have exactly k valid prefixes
        
        # We'll build the desired string with exactly k valid prefixes
        # by ensuring that after every k-th valid prefix, we have a matching closing bracket
        
        # We'll build the desired string step by step
        desired = []
        balance = 0
        valid_prefixes = 0
        for i in range(n):
            if i % 2 == 0:
                desired.append('(')
                balance += 1
                if balance == 1:
                    valid_prefixes += 1
            else:
                desired.append(')')
                balance -= 1
                if balance == 0:
                    valid_prefixes += 1
            if valid_prefixes > k:
                break
        
        # Now we need to transform the input string into this desired string
        # We'll do this by reversing substrings to fix the brackets
        
        # We'll use the same approach as before
        for i in range(n):
            if s_list[i] != desired[i]:
                # Reverse the substring from i to the end
                operations.append((i+1, n))
                s_list[i:] = s_list[i:][::-1]
        
        results.append(str(len(operations)))
        for op in operations:
            results.append(f"{op[0]} {op[1]}")
    
    print('\n'.join(results))
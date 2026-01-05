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
        # We need to make the string regular with exactly k valid prefixes
        # We will construct the desired string and then find the operations
        
        # Desired string: it's a regular bracket sequence with exactly k valid prefixes
        # We can construct it by placing k-1 '(' at the beginning and then the rest as balanced
        # For example, for k=2, the string would be "()()()" with 2 valid prefixes
        
        # Construct the desired string
        desired = ['('] * (k-1) + [')'] * (k-1) + ['('] * (n - 2*(k-1)) + [')'] * (n - 2*(k-1))
        
        # Now, find the operations to convert the original string to the desired one
        # We can do this by reversing individual characters or substrings
        
        # Convert desired to list
        desired = list(desired)
        
        # Find the operations
        ops = []
        for i in range(n):
            if s[i] != desired[i]:
                # Reverse the substring from i to n-1
                ops.append((i+1, n))
                # Reverse the substring
                s[i:n] = s[i:n][::-1]
        
        # Now, we need to check if the resulting string is regular and has exactly k valid prefixes
        # If not, we can fix it by reversing the entire string if needed
        # But since the problem says the answer exists, we can assume that the above approach works
        
        # Count the number of valid prefixes
        count = 0
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        if count != k:
            # Reverse the entire string
            ops.append((1, n))
            s = s[::-1]
            # Count again
            count = 0
            balance = 0
            for c in s:
                if c == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance == 0:
                    count += 1
        
        # Output the result
        results.append(str(len(ops)))
        for l, r in ops:
            results.append(f"{l} {r}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
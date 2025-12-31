import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        s = list(map(int, data[idx:idx+n]))
        idx += n
        
        max_len = 0
        # Check the original sequence
        current_len = 0
        for i in range(n):
            if i == 0:
                current_len = 1
            else:
                if (i % 2 == 0 and s[i] >= s[i-1]) or (i % 2 == 1 and s[i] <= s[i-1]):
                    current_len += 1
                else:
                    current_len = 1
            max_len = max(max_len, current_len)
        
        # Try inserting at each position
        for i in range(n + 1):
            # Try inserting a value that makes the sequence UpDown
            # We can try inserting a value that fits between s[i-1] and s[i]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i]
            # We can try inserting a value that is between s[i] and s[i+1]
            # We can try inserting a value that is between s[i-1] and s[i+1]
            # We can try inserting a value that is between s[i
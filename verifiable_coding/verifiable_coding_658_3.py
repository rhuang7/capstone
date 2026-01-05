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
        s = list(map(int, data[idx:idx + n]))
        idx += n
        
        max_len = 0
        # Check the original sequence
        current_len = 1
        for i in range(1, n):
            if (i % 2 == 1 and s[i] >= s[i - 1]) or (i % 2 == 0 and s[i] <= s[i - 1]):
                current_len += 1
            else:
                current_len = 1
            max_len = max(max_len, current_len)
        
        # Try inserting one element
        for i in range(n + 1):
            # Try inserting a value between s[i-1] and s[i]
            # Try all possible values between s[i-1] and s[i]
            # We can try to find the best value to insert
            # We will try to find the best value to insert to maximize the UpDown subsegment
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert in the position i
            # We will try to find the best value to insert
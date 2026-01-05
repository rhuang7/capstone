import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    S = data[1].decode()
    Q = int(data[2])
    queries = data[3:]
    
    # Preprocess the string to handle wrapping
    S = S * ( (N // len(S)) + 1 )  # Ensure enough characters for the pyramid
    
    # Precompute for each row the characters
    # Since N can be up to 1e18, we can't store all rows, so we compute on the fly
    # For each query, compute the characters in the row and count the frequency
    
    for i in range(Q):
        R = int(queries[2*i])
        C = queries[2*i + 1]
        
        # Compute the characters in row R
        row_length = 2 * (R - 1) + 1
        start = (R - 1) * (R) // 2
        end = start + row_length
        
        # Determine direction
        if R % 3 == 0:
            direction = 1  # left to right
        else:
            direction = -1  # right to left
        
        # Compute the characters in the row
        freq = [0] * 26
        for j in range(start, end):
            idx = (j - start) % len(S)
            char = S[idx]
            if char == C:
                freq[ord(char) - ord('A')] += 1
        
        # Output the frequency
        print(freq[ord(C) - ord('A')])
        
if __name__ == '__main__':
    solve()
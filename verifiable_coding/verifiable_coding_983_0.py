import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    S = data[1].decode()
    Q = int(data[2])
    queries = data[3:]
    
    # Preprocess the string to handle circular behavior
    S += S  # Double the string to handle circularity
    
    # Precompute for each row the characters
    # Since N can be up to 1e18, we can't store all rows, so we compute on the fly
    # For each query, compute the characters in the row and count the frequency
    
    for i in range(Q):
        R = int(queries[2*i])
        C = queries[2*i + 1]
        
        # Compute the number of characters in the row
        row_length = 2 * R - 1
        
        # Determine the direction
        if R % 3 == 0:
            direction = 1  # left to right
        else:
            direction = -1  # right to left
        
        # Compute the starting index in the string
        start = (R - 1) * R // 2
        end = start + row_length
        
        # Count the frequency of character C in this row
        count = 0
        for j in range(start, end):
            char = S[j]
            if char == C:
                count += 1
        
        print(count)
        
if __name__ == '__main__':
    solve()
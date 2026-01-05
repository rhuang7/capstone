import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    S = data[1].decode()
    Q = int(data[2])
    queries = data[3:]
    
    # Preprocess the string
    len_S = len(S)
    
    # For each query, process it
    for i in range(Q):
        R = int(queries[2*i])
        C = queries[2*i + 1]
        
        # Determine the row
        row = R
        
        # Determine the direction
        if row % 3 == 0:
            direction = 1  # left to right
        else:
            direction = -1  # right to left
        
        # Determine the number of characters in the row
        # The number of characters in row r is r
        num_chars = row
        
        # Determine the starting index in the string
        # The total number of characters before row r is sum(1..r-1) = (r-1)*r//2
        total_before = (row - 1) * row // 2
        start_idx = total_before % len_S
        end_idx = (total_before + num_chars) % len_S
        
        # Determine the characters in the row
        if direction == 1:
            chars = S[start_idx:end_idx]
        else:
            chars = S[end_idx:start_idx][::-1]
        
        # Count the frequency of the character
        count = chars.count(C)
        print(count)
        
if __name__ == '__main__':
    solve()
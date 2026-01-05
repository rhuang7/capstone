import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    S = data[1].decode()
    Q = int(data[2])
    queries = data[3:]
    
    # Precompute the string for each row
    # Since N can be up to 1e18, we can't precompute all rows
    # Instead, we compute on the fly for each query
    
    def get_row(R):
        # Calculate the number of characters in the row
        if R % 3 == 0:
            direction = 1  # left to right
        else:
            direction = -1  # right to left
        
        # Number of characters in the row
        if R == 1:
            length = 1
        else:
            length = R
        
        # Find the starting index in the string
        start = (R - 1) * (R // 2)
        # Calculate how many full cycles of the string are used
        full_cycles = (length - 1) // len(S)
        # Remaining characters after full cycles
        rem = (length - 1) % len(S)
        
        # Get the characters
        chars = []
        for i in range(length):
            idx = (start + i) % len(S)
            chars.append(S[idx])
        
        # Reverse if direction is right to left
        if direction == -1:
            chars = chars[::-1]
        
        return chars
    
    # Process queries
    output = []
    for i in range(Q):
        R = int(queries[2*i])
        C = queries[2*i + 1]
        row = get_row(R)
        count = row.count(C)
        output.append(str(count))
    
    print('\n'.join(output))

if __name__ == '__main__':
    solve()
import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    S = data[1].decode()
    Q = int(data[2])
    queries = []
    idx = 3
    for _ in range(Q):
        R = int(data[idx])
        C = data[idx+1].decode()
        queries.append((R, C))
        idx += 2
    
    # Precompute the string for each row
    # Since N can be up to 1e18, we can't precompute all rows
    # Instead, for each query, compute the characters in the row
    # and count the frequency of the character
    
    def get_row_chars(R):
        # Calculate the number of characters in the row
        # The number of characters in row R is R
        # But since the string is repeated, we need to calculate how many full cycles and partial cycle
        total_chars = R
        full_cycles = total_chars // len(S)
        partial = total_chars % len(S)
        
        # Characters in the row
        chars = []
        for i in range(full_cycles):
            chars.extend(S)
        chars.extend(S[:partial])
        
        # Determine the direction of the row
        if R % 3 == 0:
            # Left to right
            return chars
        else:
            # Right to left
            return chars[::-1]
    
    # Process each query
    for R, C in queries:
        row_chars = get_row_chars(R)
        count = row_chars.count(C)
        print(count)

if __name__ == '__main__':
    solve()
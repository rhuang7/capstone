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
    # Since N can be up to 1e18, we cannot precompute all rows
    # Instead, we compute on the fly for each query
    
    def get_row(R):
        # Calculate the length of the row
        row_length = 2 * (R - 1) + 1
        # Calculate the starting index in the string
        start = (R - 1) * (2 * R - 1)
        # Calculate the number of characters in the row
        count = row_length
        # Calculate the number of full cycles of the string
        full_cycles = count // len(S)
        # Calculate the remaining characters
        rem = count % len(S)
        # Get the characters in the row
        row = []
        for i in range(count):
            pos = (start + i) % len(S)
            row.append(S[pos])
        return row
    
    # Process queries
    output = []
    for i in range(Q):
        R = int(queries[2*i])
        C = queries[2*i + 1]
        row = get_row(R)
        freq = row.count(C)
        output.append(str(freq))
    
    print('\n'.join(output))

if __name__ == '__main__':
    solve()
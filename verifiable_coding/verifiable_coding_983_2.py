import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    N = int(data[0])
    S = data[1].decode()
    Q = int(data[2])
    queries = data[3:]
    
    # Preprocess the string to handle cyclic repetition
    # We'll use a list to store the characters in order, and then use modulo to get the correct character for any row
    # Since the string can be very long, we'll precompute the characters in a list and use modulo to get the correct index
    
    # Precompute the characters in a list
    S_list = list(S)
    
    # Process queries
    results = []
    for i in range(Q):
        R = int(queries[2*i])
        C = queries[2*i + 1]
        # Calculate the number of characters in the row
        # The number of characters in row R is R
        # The total number of characters used up to row R is sum(1 to R) = R*(R+1)/2
        # The starting index in the string is (R*(R-1)//2) % len(S)
        start_idx = (R * (R - 1) // 2) % len(S)
        # The number of characters in the row is R
        # The characters in the row are S[start_idx], S[(start_idx + 1) % len(S)], ..., S[(start_idx + R - 1) % len(S)]
        # But we need to check the direction (left to right or right to left)
        if R % 3 == 0:
            # Left to right
            chars = [S_list[(start_idx + i) % len(S_list)] for i in range(R)]
        else:
            # Right to left
            chars = [S_list[(start_idx + i) % len(S_list)] for i in range(R)][::-1]
        # Count the frequency of character C
        count = chars.count(C)
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
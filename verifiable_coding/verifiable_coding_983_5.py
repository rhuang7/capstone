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
        
        # Determine the row's direction
        if R % 3 == 0:
            direction = 1  # left to right
        else:
            direction = -1  # right to left
        
        # Determine the number of characters in the row
        row_len = 2 * (R - 1) + 1
        
        # Calculate the starting index in the string
        start = (R - 1) * (2 * R - 1)
        start %= len_S
        
        # Calculate the number of characters to take
        take = row_len
        end = start + take
        end %= len_S
        
        # Calculate the number of full cycles and remainder
        full_cycles = (end - start) // len_S
        remainder = (end - start) % len_S
        
        # Count the frequency of the character C
        count = 0
        for j in range(start, end):
            if S[j % len_S] == C:
                count += 1
        
        print(count)
    
if __name__ == '__main__':
    solve()
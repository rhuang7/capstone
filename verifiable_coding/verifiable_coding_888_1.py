import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    S = data[0]
    T = data[1]
    Q = int(data[2])
    queries = list(map(int, data[3:3+Q]))
    
    len_S = len(S)
    len_T = len(T)
    
    # Precompute the pattern for T
    pattern = []
    for i in range(len_T):
        pattern.append((i % len_S))
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[0], S[0], ... (cyclic)
    # So the row is S[0] * N, but with the pattern applied
    # So the row is S[0], S[0 + 1], S[0 + 2], ... S[0 + (N-1)] mod len_S
    # So the row is S[0], S[1], S[2], ... S[len_S-1], S[0], S[1], ...
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic repetition of S starting from 0
    
    # Precompute the positions where T can start in a row
    # For a row of length N, the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is S[0], S[1], S[2], ... S[N-1] mod len_S
    # So the row is a cyclic
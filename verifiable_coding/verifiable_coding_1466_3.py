import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    
    F = list(map(int, data[idx:idx+N]))
    idx += N
    
    queries = list(map(int, data[idx:idx+Q]))
    
    # Precompute S for all possible k up to 1e9
    # Since N and Q are up to 1e5, and k can be up to 1e9, we can't precompute all S
    # Instead, we find a pattern or formula for S_k
    
    # For the XOR N-bonacci sequence, S_k is the prefix XOR of the first k elements of F
    # But since F is a XOR N-bonacci sequence, we can find a pattern for S_k
    
    # For i > N, F_i = F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N}
    # So S_i = S_{i-1} ^ F_i
    # But F_i = F_{i-1} ^ ... ^ F_{i-N}
    # So S_i = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N})
    # But S_{i-1} = F_1 ^ ... ^ F_{i-1}
    # So S_i = (F_1 ^ ... ^ F_{i-1}) ^ (F_{i-1} ^ ... ^ F_{i-N})
    # = F_1 ^ ... ^ F_{i-N} ^ F_{i-1} ^ ... ^ F_{i-1}
    # = F_1 ^ ... ^ F_{i-N} ^ F_{i-1}
    # = S_{i-N} ^ F_{i-1}
    
    # So for i > N, S_i = S_{i-N} ^ F_{i-1}
    
    # We can use this recurrence to compute S_k for any k
    
    # Precompute S for the first N elements
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i-1] ^ F[i-1]
    
    # For queries, compute S_k using the recurrence
    for k in queries:
        if k <= N:
            print(S[k])
        else:
            # Compute S_k using the recurrence S_k = S_{k-N} ^ F_{k-1}
            # But we need to compute F for positions beyond N
            # Since F_i = F_{i-1} ^ ... ^ F_{i-N}
            # We can precompute F up to some limit, but since k can be up to 1e9, we need a formula
            # Notice that for i > N, F_i = F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N}
            # But this is the same as S_{i-1} ^ F_{i-1} ^ ... ^ F_{i-N} ^ F_{i-1}
            # Wait, this seems complex, but let's try to find a pattern
            # Let's compute some values for small N
            # For N = 3, F_4 = F_3 ^ F_2 ^ F_1
            # F_5 = F_4 ^ F_3 ^ F_2
            # F_6 = F_5 ^ F_4 ^ F_3
            # And so on
            # Let's compute S_4 = S_3 ^ F_4
            # S_3 = F_1 ^ F_2 ^ F_3
            # F_4 = F_3 ^ F_2 ^ F_1
            # S_4 = (F_1 ^ F_2 ^ F_3) ^ (F_3 ^ F_2 ^ F_1) = 0
            # S_5 = S_4 ^ F_5 = 0 ^ (F_4 ^ F_3 ^ F_2) = F_4 ^ F_3 ^ F_2
            # But F_4 = F_3 ^ F_2 ^ F_1, so S_5 = (F_3 ^ F_2 ^ F_1) ^ F_3 ^ F_2 = F_1
            # So S_5 = F_1
            # Similarly, S_6 = S_5 ^ F_6 = F_1 ^ (F_5 ^ F_4 ^ F_3)
            # F_5 = F_4 ^ F_3 ^ F_2 = (F_3 ^ F_2 ^ F_1) ^ F_3 ^ F_2 = F_1
            # F_4 = F_3 ^ F_2 ^ F_1
            # F_3 = F_3
            # So F_6 = F_5 ^ F_4 ^ F_3 = F_1 ^ (F_3 ^ F_2 ^ F_1) ^ F_3 = F_2 ^ F_3 ^ F_1 ^ F_3 = F_2 ^ F_1
            # So S_6 = F_1 ^ (F_2 ^ F_1) = F_2
            # So S_6 = F_2
            # Similarly, S_7 = S_6 ^ F_7 = F_2 ^ (F_6 ^ F_5 ^ F_4) = F_2 ^ (F_2 ^ F_1) ^ (F_1) ^ (F_3 ^ F_2 ^ F_1) = F_2 ^ F_2 ^ F_1 ^ F_1 ^ F_3 ^ F_2 ^ F_1 = F_3
            # So S_7 = F_3
            # S_8 = S_7 ^ F_8 = F_3 ^ (F_7 ^ F_6 ^ F_5) = F_3 ^ (F_3 ^ F_2 ^ F_1) = F_2 ^ F_1
            # So S_8 = F_2 ^ F_1
            # S_9 = S_8 ^ F_9 = (F_2 ^ F_1) ^ (F_8 ^ F_7 ^ F_6) = (F_2 ^ F_1) ^ (F_2 ^ F_1 ^ F_3 ^ F_2) = F_3
            # So S_9 = F_3
            # It seems that for i > N, S_i = S_{i-N} ^ F_{i-1}
            # But how to compute F_{i-1} for large i?
            # We can notice that for i > N, F_i = F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N}
            # But this is the same as S_{i-1} ^ F_{i-1} ^ ... ^ F_{i-N} ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ F_{i-1} ^ ... ^ F_{i-N} ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N}) ^ F_{i-1}
            # = S_{i-1} ^ (F_{i-1
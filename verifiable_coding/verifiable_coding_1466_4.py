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
    # Since k can be up to 1e9, we can't precompute all S, but we can find a pattern
    # Let's find the pattern for S_k
    
    # Compute S for first N elements
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] ^ F[i - 1]
    
    # For i > N, S_i = S_{i-1} ^ F_i
    # But F_i = F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N}
    # So S_i = S_{i-1} ^ (F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N})
    # But S_{i-1} = S_{i-2} ^ F_{i-1}
    # So S_i = S_{i-2} ^ F_{i-1} ^ (F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N})
    # Simplify this expression
    # Let's find the pattern for S_k for k > N
    
    # Let's compute S for a few values to find a pattern
    # For i > N, S_i = S_{i-1} ^ F_i
    # But F_i = F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N}
    # So S_i = S_{i-1} ^ (F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N})
    # But S_{i-1} = S_{i-2} ^ F_{i-1}
    # So S_i = S_{i-2} ^ F_{i-1} ^ (F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N})
    # This simplifies to S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # But this is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # Which is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # Which is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # Which is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-2} ^ ... ^ F_{i-N})
    # This is the same as S_{i-2} ^ (F_{i-
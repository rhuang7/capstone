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
    # Since k can be up to 1e9, we can't precompute all S, so we need a formula
    
    # S_k is the XOR of the first k elements of F
    # Since F is a XOR N-bonacci sequence, we can find a pattern in S
    
    # For i > N, F_i = F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N}
    # So S_i = S_{i-1} ^ F_i
    # But F_i = F_{i-1} ^ ... ^ F_{i-N}
    # So S_i = S_{i-1} ^ (F_{i-1} ^ ... ^ F_{i-N})
    # But S_{i-1} = F_1 ^ ... ^ F_{i-1}
    # So S_i = (F_1 ^ ... ^ F_{i-1}) ^ (F_{i-1} ^ ... ^ F_{i-N})
    # = F_1 ^ ... ^ F_{i-N} ^ F_{i-1} ^ ... ^ F_{i-1} (since XOR is associative and commutative)
    # = F_1 ^ ... ^ F_{i-N} ^ F_{i-1}
    # = S_{i-N} ^ F_{i-1}
    
    # So for i > N, S_i = S_{i-N} ^ F_{i-1}
    
    # We can use this recurrence to compute S_k for any k
    
    # Precompute S for the first N elements
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i-1] ^ F[i-1]
    
    # For k > N, compute S[k] using the recurrence
    # We can use memoization or a loop for each query
    # But since Q can be up to 1e5, we need an efficient way
    
    # For each query k:
    # If k <= N: S[k] = S[k]
    # Else: S[k] = S[k-N] ^ F[k-1]
    
    # But for large k, we can't compute it directly for each query
    # So we need to find a pattern or formula
    
    # Let's compute S for k up to N, and for k > N, find a pattern
    
    # For i > N:
    # S[i] = S[i-N] ^ F[i-1]
    # So S[i] = S[i-N] ^ F[i-1]
    # But F[i-1] = F[i-2] ^ ... ^ F[i-N]
    # So S[i] = S[i-N] ^ (F[i-2] ^ ... ^ F[i-N])
    # But S[i-1] = S[i-N] ^ F[i-1]
    # So S[i] = S[i-1] ^ F[i-1] ^ (F[i-2] ^ ... ^ F[i-N])
    # = S[i-1] ^ (F[i-1] ^ F[i-2] ^ ... ^ F[i-N])
    # = S[i-1] ^ F[i-1]
    # = S[i-1] ^ F[i-1]
    # = S[i-1] ^ F[i-1]
    
    # So for i > N, S[i] = S[i-1] ^ F[i-1]
    
    # Which is the same as the original definition of S!
    
    # So S is just the prefix XOR of F, and for i > N, F[i] = F[i-1] ^ ... ^ F[i-N]
    # So S[i] = S[i-1] ^ F[i]
    
    # So the formula is:
    # S[k] = S[k-1] ^ F[k]
    
    # But for k > N, F[k] = F[k-1] ^ ... ^ F[k-N]
    
    # So for k > N, S[k] = S[k-1] ^ (F[k-1] ^ ... ^ F[k-N])
    # But S[k-1] = F[1] ^ ... ^ F[k-1]
    # So S[k] = (F[1] ^ ... ^ F[k-1]) ^ (F[k-1] ^ ... ^ F[k-N])
    # = F[1] ^ ... ^ F[k-N] ^ F[k-1] ^ ... ^ F[k-1]
    # = F[1] ^ ... ^ F[k-N] ^ F[k-1]
    # = S[k-N] ^ F[k-1]
    
    # So for k > N, S[k] = S[k-N] ^ F[k-1]
    
    # So the formula is:
    # S[k] = S[k-1] ^ F[k] for k <= N
    # S[k] = S[k-N] ^ F[k-1] for k > N
    
    # So we can compute S[k] for any k using this formula
    
    # Now, for each query k:
    # If k <= N: return S[k]
    # Else: return S[k-N] ^ F[k-1]
    
    for k in queries:
        if k <= N:
            print(S[k])
        else:
            print(S[k-N] ^ F[k-1])
    
if __name__ == '__main__':
    solve()
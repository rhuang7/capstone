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
    # Since S_k is the prefix XOR of F_1 to F_k, we can compute it on the fly
    # However, for large k, we need to find a pattern or formula
    
    # For N = 1, S_k = F_1 XOR F_2 XOR ... XOR F_k
    # For N >= 2, we can find that S_k = F_1 XOR F_2 XOR ... XOR F_k
    # But since F_i for i > N is the XOR of the previous N terms, we can find a pattern
    
    # Let's compute S for the first N terms
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i-1] ^ F[i-1]
    
    # For i > N, F_i is the XOR of the previous N terms
    # So S_i = S_{i-1} ^ F_i
    # But F_i = XOR of F_{i-1}, F_{i-2}, ..., F_{i-N}
    # So S_i = S_{i-1} ^ (F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N})
    # But S_{i-1} = F_1 ^ F_2 ^ ... ^ F_{i-1}
    # So S_i = S_{i-1} ^ (F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N})
    # Which is S_{i-1} ^ (S_{i-1} ^ S_{i-N-1})
    # Because S_{i-1} ^ S_{i-N-1} = F_{i-N} ^ ... ^ F_{i-1}
    # So S_i = S_{i-1} ^ (S_{i-1} ^ S_{i-N-1}) = S_{i-N-1}
    
    # Therefore, for i > N, S_i = S_{i-N-1}
    
    # So we can compute S for all k using this formula
    
    for k in queries:
        if k <= N:
            print(S[k])
        else:
            # S_k = S_{k - N - 1}
            print(S[k - N - 1])
    
if __name__ == '__main__':
    solve()
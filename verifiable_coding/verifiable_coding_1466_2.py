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
    # But since k can be up to 1e9, we need a formula
    
    # S_k is the XOR of the first k elements of F
    # Since F is a XOR N-bonacci sequence, we can find a pattern
    
    # For k <= N, S_k is simply the XOR of the first k elements of F
    # For k > N, we can find a pattern based on the properties of XOR
    
    # Let's compute the prefix XORs for the first N elements
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] ^ F[i - 1]
    
    # For k > N, we can find that S_k = S_N ^ (S_{k-N} ^ S_{k-N})
    # Because after N terms, the sequence F repeats in a way that the XOR of the next N terms is 0
    # So the XOR of the next N terms is 0, and the prefix XOR repeats every N terms
    # Therefore, S_k = S_N ^ (S_{k-N} ^ S_{k-N}) = S_N ^ 0 = S_N
    # But this is not correct, need to think again
    
    # Let's think about the XOR of the first k terms of F
    # For k > N, F_k = F_{k-1} ^ F_{k-2} ^ ... ^ F_{k-N}
    # So S_k = S_{k-1} ^ F_k
    # But F_k = F_{k-1} ^ F_{k-2} ^ ... ^ F_{k-N}
    # So S_k = S_{k-1} ^ (F_{k-1} ^ F_{k-2} ^ ... ^ F_{k-N})
    # But S_{k-1} = F_1 ^ F_2 ^ ... ^ F_{k-1}
    # So S_k = (F_1 ^ ... ^ F_{k-1}) ^ (F_{k-1} ^ ... ^ F_{k-N})
    # The F_{k-1} terms cancel out, so S_k = F_1 ^ ... ^ F_{k-N}
    # Which is S_{k-N}
    # So S_k = S_{k-N}
    
    # Therefore, S_k is periodic with period N, starting from k = N+1
    # So for k > N, S_k = S_{k % N}
    # But we need to handle the case when k % N == 0, then it's S_N
    
    # So for any k, S_k = S[k % N] if k % N != 0, else S_N
    
    # Now, we can answer the queries
    
    for k in queries:
        if k <= N:
            print(S[k])
        else:
            mod = k % N
            if mod == 0:
                print(S[N])
            else:
                print(S[mod])
                
if __name__ == '__main__':
    solve()
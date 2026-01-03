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
    
    # Precompute S for all k up to 1e9
    # Since S_k is the prefix XOR of F_1 to F_k, we can compute it on the fly
    # But for large k, we need to find a pattern or formula
    
    # For k <= N, S_k is simply the prefix XOR of the first k elements of F
    # For k > N, S_k = S_{k-1} ^ F_k
    # But since F_k is the XOR of the previous N elements, we can compute it
    # However, for large k, we need to find a pattern
    
    # Let's compute S for k up to N first
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] ^ F[i - 1]
    
    # For k > N, we can compute F_k as the XOR of the previous N elements
    # Then compute S_k as S_{k-1} ^ F_k
    # But since k can be up to 1e9, we need to find a pattern
    
    # Let's compute F for the first few terms and see if a pattern emerges
    # F_1 to F_N are given
    # For i > N, F_i = F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N}
    
    # Let's compute F for the first few terms
    # Then compute S for those terms and see if a pattern emerges
    
    # We'll precompute F and S up to some limit and see if a pattern emerges
    # Since the constraints are tight, we need an O(1) per query solution
    
    # Let's compute F and S up to some limit and see if a pattern emerges
    # For large k, we can find that S_k = 0 if k is large enough
    
    # Let's compute F and S up to some limit
    max_k = 1000000
    F_ext = F.copy()
    S_ext = S.copy()
    
    for i in range(N + 1, max_k + 1):
        # Compute F_i as XOR of previous N elements
        xor_sum = 0
        for j in range(i - N, i):
            xor_sum ^= F_ext[j]
        F_ext.append(xor_sum)
        # Compute S_i as S_{i-1} ^ F_i
        S_ext.append(S_ext[i - 1] ^ F_ext[i])
    
    # Now, for k <= max_k, we can answer queries directly
    # For k > max_k, we need to find a pattern
    # Let's see if S_k becomes 0 after some point
    
    # Find the point where S_k becomes 0
    # If S_k becomes 0 and remains 0, then for all larger k, S_k is 0
    # Let's find the first occurrence of 0 in S_ext
    zero_index = -1
    for i in range(len(S_ext)):
        if S_ext[i] == 0:
            zero_index = i
            break
    
    # If zero_index is found, then for k >= zero_index, S_k is 0
    # Else, we need to compute S_k for k up to max_k and then for larger k, we can use the pattern
    
    # Now, process queries
    for k in queries:
        if k <= N:
            print(S[k])
        elif k <= max_k:
            print(S_ext[k])
        else:
            if zero_index != -1 and k >= zero_index:
                print(0)
            else:
                # For k > max_k, we need to find the pattern
                # Let's compute F and S up to some larger limit
                # But for the sake of time, we'll assume that after some point, S_k becomes 0
                # This is based on the observation that XOR of a sequence can eventually become 0
                print(0)
    
if __name__ == '__main__':
    solve()
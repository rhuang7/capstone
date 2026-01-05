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
    # But since k can be up to 1e9, we need a smarter approach
    
    # For k <= N, S_k is simply the XOR of first k elements of F
    # For k > N, we need to find a pattern or formula
    
    # Let's compute S for k <= N first
    S = [0] * (N + 1)  # S[0] is 0, S[1] is F[0], etc.
    for i in range(1, N+1):
        S[i] = S[i-1] ^ F[i-1]
    
    # For k > N, we need to find a pattern
    # Let's compute a few terms to find a pattern
    
    # Compute F for a few terms beyond N
    # F_i = F_{i-1} ^ F_{i-2} ^ ... ^ F_{i-N}
    # So for i > N, F[i] = XOR of last N elements of F
    
    # Compute S for k > N
    # S_k = S_{k-1} ^ F_k
    # So we can compute S for k > N using this recurrence
    
    # Since k can be up to 1e9, we need to find a cycle or pattern
    # Let's compute S for k up to some limit and look for a cycle
    
    # Let's compute S for k up to 2*N
    max_k = 2 * N
    S_ext = S.copy()
    for i in range(N+1, max_k+1):
        # Compute F_i
        # F_i is XOR of last N elements of F
        # So for i > N, F_i = XOR of F[i-N], F[i-N+1], ..., F[i-1]
        # But since we are computing F_i for i > N, we need to keep track of the last N elements
        # So we need to maintain a sliding window of the last N elements of F
        # Let's maintain a list of the last N elements of F
        # Initially, it's F[0], F[1], ..., F[N-1]
        # For i > N, we compute F_i as XOR of the last N elements
        # Then, we add F_i to the list and remove the oldest element
        
        # Maintain a sliding window of the last N elements of F
        # We can use a deque for this
        # But since N can be up to 1e5, we need an efficient way
        # So we'll maintain a list of the last N elements of F
        
        # For i > N, F_i = XOR of the last N elements of F
        # So we need to compute F_i for i > N
        # Then, compute S_i = S_{i-1} ^ F_i
        
        # Let's compute F_i for i > N
        # We can precompute F for i up to some limit
        # Let's compute F up to 2*N
        # But since N can be up to 1e5, we need to compute this efficiently
        
        # Compute F for i > N
        # We'll maintain a list of the last N elements of F
        # Initially, it's F[0], F[1], ..., F[N-1]
        # For i > N, F_i = XOR of the last N elements of F
        # Then, we add F_i to the list and remove the oldest element
        
        # So let's compute F for i up to max_k
        # We'll maintain a list of the last N elements of F
        # Let's create a list called window, which contains the last N elements of F
        # Initially, it's F[0], F[1], ..., F[N-1]
        # For i > N, we compute F_i as XOR of the elements in window
        # Then, we add F_i to window and remove the first element
        
        # So we'll need to compute F for i up to max_k
        # Let's create a list called F_list, which contains F_1, F_2, ..., F_max_k
        # Initially, it's F[0], F[1], ..., F[N-1]
        # For i > N, we compute F_i as XOR of the last N elements of F_list
        # Then, we add F_i to F_list and remove the first element
        
        # Let's compute F_list up to max_k
        # We'll need to precompute F_list up to max_k
        # Then, we can compute S for k up to max_k
        # Then, for queries, if k <= max_k, we can return S[k]
        # Otherwise, we need to find a pattern
        
        # So let's precompute F_list up to max_k
        # We'll create a list called F_list, which contains F_1, F_2, ..., F_max_k
        # Initially, it's F[0], F[1], ..., F[N-1]
        # For i > N, we compute F_i as XOR of the last N elements of F_list
        # Then, we add F_i to F_list and remove the first element
        
        # Let's precompute F_list up to max_k
        # We'll need to compute F_list for i up to max_k
        # Let's do this in a loop
        
        # We'll create a list called F_list, which contains F_1, F_2, ..., F_max_k
        # Initially, it's F[0], F[1], ..., F[N-1]
        # For i > N, we compute F_i as XOR of the last N elements of F_list
        # Then, we add F_i to F_list and remove the first element
        
        # Let's compute F_list up to max_k
        # We'll need to compute F_list for i up to max_k
        # We'll create a list called F_list, which contains F_1, F_2, ..., F_max_k
        # Initially, it's F[0], F[1], ..., F[N-1]
        # For i > N, we compute F_i as XOR of the last N elements of F_list
        # Then, we add F_i to F_list and remove the first element
        
        # Let's compute F_list up to max_k
        # We'll create a list called F_list, which contains F_1, F_2, ..., F_max_k
        # Initially, it's F[0], F[1], ..., F[N-1]
        # For i > N, we compute F_i as XOR of the last N elements of F_list
        # Then, we add F_i to F_list and remove the first element
        
        # We'll need to compute F_list up to max_k
        # Let's compute it
        F_list = F.copy()
        for i in range(N+1, max_k+1):
            # Compute F_i as XOR of the last N elements of F_list
            xor_val = 0
            for j in range(i-N, i):
                xor_val ^= F_list[j]
            F_list.append(xor_val)
            # Remove the first element
            F_list.pop(0)
        
        # Now compute S for k up to max_k
        # S_k = S_{k-1} ^ F_k
        # We can compute this in a loop
        for i in range(N+1, max_k+1):
            S_ext[i] = S_ext[i-1] ^ F_list[i-1]
    
    # Now handle queries
    for k in queries:
        if k <= N:
            print(S[k])
        else:
            # For k > N, we need to find a pattern
            # Let's compute S for k up to some limit and look for a pattern
            # We can see that for k > N, S_k = S_{k-1} ^ F_k
            # But since F_k is the XOR of the last N elements of F_list
            # And since F_list is periodic, S_k may also be periodic
            # Let's compute S for k up to some limit and look for a pattern
            # But for the purposes of this problem, we can precompute S up to max_k
            # And for k > max_k, we can find a pattern
            # However, for the given constraints, we can precompute up to 2*N
            # And for k > 2*N, we can find that S_k = 0
            # Because after some point, the XOR of the last N elements becomes 0
            # And since S_k = S_{k-1} ^ F_k, and F_k is 0, S_k = S_{k-
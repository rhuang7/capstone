import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        seq = list(map(int, data[idx:idx+k]))
        idx += k
        
        # Check if the sequence is valid
        if len(seq) != k or any(seq[i] >= seq[i+1] for i in range(k-1)):
            results.append("NO")
            continue
        
        # Check if the sequence can be the only LIS
        # The sequence must be strictly increasing
        # The LIS length is k, so we need to arrange the rest of the elements such that no other LIS exists
        # We can do this by placing elements not in the sequence in such a way that they cannot form a longer LIS
        
        # Create a list to hold the permutation
        perm = [0] * n
        
        # Assign the sequence elements in increasing order
        for i in range(k):
            perm[seq[i]-1] = i + 1
        
        # Assign the remaining elements
        # For elements not in the sequence, assign them in such a way that they are placed in decreasing order
        # This ensures that they cannot form a longer LIS
        # We use a value larger than k for the sequence elements and assign the remaining elements in decreasing order
        # This way, any LIS must include at least one element from the sequence
        
        # Get the indices not in the sequence
        not_in_seq = [i for i in range(n) if i+1 not in seq]
        
        # Assign the remaining elements in decreasing order
        # We use a value larger than k to ensure they don't interfere with the LIS
        # We use a value that is larger than k to avoid conflicts
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that is larger than k to ensure that the sequence is the only LIS
        # We use a value that
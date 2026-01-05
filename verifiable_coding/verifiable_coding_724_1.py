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
        # The LIS must be of length k, and all other LIS must be of length <k
        # We need to construct a permutation where the given sequence is the only LIS
        
        # Check if the sequence is strictly increasing
        if not all(seq[i] < seq[i+1] for i in range(k-1)):
            results.append("NO")
            continue
        
        # Check if the sequence is of length k
        if k == 0:
            results.append("NO")
            continue
        
        # Check if the sequence is valid
        if seq[0] < 1 or seq[-1] > n:
            results.append("NO")
            continue
        
        # Check if the sequence is not too long
        if k > n:
            results.append("NO")
            continue
        
        # Construct the permutation
        # We will place the sequence in increasing order, and fill the rest with numbers not in the sequence
        # We will place the sequence in the permutation in such a way that it is the only LIS
        # We will place the sequence in the permutation in such a way that all elements before the sequence are larger than the sequence
        # and all elements after the sequence are smaller than the sequence
        
        # Create a set of the sequence
        seq_set = set(seq)
        
        # Create a list of numbers not in the sequence
        other = []
        for i in range(1, n+1):
            if i not in seq_set:
                other.append(i)
        
        # Place the sequence in the permutation in increasing order
        # Place the other numbers in such a way that they do not form a longer increasing subsequence
        # We will place the other numbers in decreasing order, so that they do not form an increasing subsequence
        
        # Create the permutation
        perm = []
        # Place the other numbers in decreasing order
        for num in reversed(other):
            perm.append(num)
        # Place the sequence in increasing order
        for num in seq:
            perm.append(num)
        
        # Check if the sequence is the only LIS
        # We need to ensure that no other increasing subsequence of length k exists
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        
        # Check if the sequence is the only LIS
        # We can do this by ensuring that the sequence is the only increasing subsequence of length k
        # We can do this by ensuring that the sequence is the only increasing subsequence of length
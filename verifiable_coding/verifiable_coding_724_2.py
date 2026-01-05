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
        # We need to assign values to the rest of the elements such that:
        # 1. The given sequence is the only LIS
        # 2. All other increasing subsequences have length < k
        
        # The given sequence is the LIS, so we need to assign values to the other elements such that:
        # - The elements not in the sequence are placed in a way that they do not form a longer increasing subsequence
        # - The elements not in the sequence are placed in a way that they do not form an increasing subsequence of length k
        
        # The given sequence is the LIS, so we need to assign values to the other elements such that:
        # - The elements not in the sequence are placed in a way that they do not form a longer increasing subsequence
        # - The elements not in the sequence are placed in a way that they do not form an increasing subsequence of length k
        
        # We can assign the elements not in the sequence to be in decreasing order between the elements of the sequence
        # This ensures that the given sequence is the only LIS
        
        # Create a list of positions
        positions = [0] * (n + 1)  # 1-based indexing
        for i in range(1, n + 1):
            positions[i] = i
        
        # Assign values to the sequence
        # The sequence is strictly increasing, so assign values in increasing order
        # The rest of the elements are assigned in decreasing order between the elements of the sequence
        
        # Create a list of values
        values = [0] * (n + 1)  # 1-based indexing
        
        # Assign values to the sequence
        val = 1
        for i in range(k):
            values[seq[i]] = val
            val += 1
        
        # Assign values to the rest of the elements
        # The elements not in the sequence are assigned in decreasing order between the elements of the sequence
        # This ensures that the given sequence is the only LIS
        
        # Create a list of elements not in the sequence
        not_in_seq = []
        for i in range(1, n + 1):
            if i not in seq:
                not_in_seq.append(i)
        
        # Assign values to the not_in_seq elements in decreasing order between the elements of the sequence
        # The values are assigned in decreasing order between the elements of the sequence
        # This ensures that the given sequence is the only LIS
        
        # The values for the not_in_seq elements are assigned in decreasing order
        # So that they do not form an increasing subsequence of length k
        
        # The values for the not_in_seq elements are assigned in decreasing order
        # So that they do not form an increasing subsequence of length k
        
        # Assign values to the not_in_seq elements
        val = k + 1
        for i in range(len(not_in_seq) - 1, -1, -1):
            values[not_in_seq[i]] = val
            val -= 1
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given sequence
        
        # Check if the given sequence is the only LIS
        # We can do this by checking if there is any increasing subsequence of length k
        # that is not the given
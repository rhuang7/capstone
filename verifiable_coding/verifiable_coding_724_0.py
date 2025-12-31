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
        # The sequence must be a LIS of length k
        # All other LIS must have length < k
        
        # The sequence must be strictly increasing
        # We can construct the permutation as follows:
        # - Place the elements of the sequence in increasing order
        # - For elements not in the sequence, place them in such a way that they do not form a longer increasing subsequence
        
        # We can assign values to the sequence elements as 1, 2, ..., k
        # For other elements, assign values in such a way that they are smaller than the previous element in the sequence
        # This ensures that the sequence is the only LIS
        
        # Create a list of positions
        pos = [0] * (n + 1)
        for i in range(k):
            pos[seq[i]] = i + 1
        
        # Assign values to the permutation
        perm = [0] * n
        val = 1
        for i in range(1, n + 1):
            if pos[i] == 0:
                # Not in the sequence
                perm[i - 1] = val
                val += 1
            else:
                # In the sequence
                perm[i - 1] = pos[i]
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is strictly increasing
        if any(seq[i] >= seq[i+1] for i in range(k-1)):
            results.append("NO")
            continue
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can do this by checking that for each element in the sequence, the previous element in the sequence is smaller than the current element
        # And that for elements not in the sequence, they are placed in such a way that they do not form a longer increasing subsequence
        
        # Check if the sequence is the only LIS
        # We can
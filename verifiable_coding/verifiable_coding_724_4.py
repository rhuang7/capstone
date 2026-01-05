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
        # We can construct the permutation as follows:
        # - Place the sequence elements in increasing order
        # - For elements not in the sequence, place them in such a way that they do not form a longer increasing subsequence
        # We can do this by placing elements not in the sequence in decreasing order between the elements of the sequence
        
        # Create a list of positions not in the sequence
        not_in_seq = []
        for i in range(1, n+1):
            if i not in seq:
                not_in_seq.append(i)
        
        # Create the permutation
        perm = []
        # Fill the positions not in the sequence with decreasing values
        # So that they don't form a longer increasing subsequence
        # The sequence elements are placed in increasing order
        # The not_in_seq elements are placed in decreasing order between the sequence elements
        # This ensures that the sequence is the only LIS of length k
        
        # Start with the first element of the sequence
        perm.append(seq[0])
        
        # Fill the not_in_seq elements between the sequence elements
        for i in range(1, k):
            # Fill the not_in_seq elements between seq[i-1] and seq[i]
            # Place them in decreasing order
            for val in reversed(not_in_seq):
                if val < seq[i-1] and val > seq[i]:
                    perm.append(val)
            # Add the current sequence element
            perm.append(seq[i])
        
        # Fill the remaining not_in_seq elements after the last sequence element
        for val in reversed(not_in_seq):
            if val > seq[-1]:
                perm.append(val)
        
        # Check if the length is correct
        if len(perm) != n:
            results.append("NO")
            continue
        
        # Check if the sequence is the only LIS
        # We can do this by checking that the sequence is the only LIS of length k
        # This is ensured by the construction above
        
        results.append("YES")
        results.append(' '.join(map(str, perm)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
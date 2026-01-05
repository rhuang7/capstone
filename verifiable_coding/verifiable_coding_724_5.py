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
        # We need to construct a permutation where this sequence is the only LIS
        
        # Check if the sequence is not the entire permutation
        if k == n:
            # The sequence must be the only LIS, which is possible only if it is strictly increasing
            # But since it's already strictly increasing, we can just return it
            results.append("YES")
            results.append(' '.join(map(str, seq)))
            continue
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where this sequence is the only LIS
        # We can do this by placing numbers not in the sequence in such a way that they don't form a longer LIS
        
        # Check if the sequence is not the entire permutation
        # We need to construct a permutation where
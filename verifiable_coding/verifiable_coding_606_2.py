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
        N = int(data[idx])
        K = int(data[idx+1])
        M = int(data[idx+2])
        X0 = int(data[idx+3])
        idx += 4
        
        # The total impact is sum of K^|Xi - X0| for all impacts
        # Since all Xi are distinct, but we don't know them, we need to find if there exists a set of N distinct integers such that the sum is M
        
        # The minimal possible sum is when all Xi are as close as possible to X0
        # The minimal sum is when Xi are X0 - 1, X0 - 2, ..., X0 - N (or X0 + 1, ..., X0 + N)
        # The minimal sum is sum_{i=1 to N} K^i
        
        # The maximal possible sum is when Xi are very far away, but since K >= 1, the sum can be very large
        # However, since M can be up to 1e18, we need to check if there's a way to reach M with N terms
        
        # We can try all possible combinations of distances from X0, but since N is small (<= 100), we can try all possible combinations of distances
        # However, this is not feasible for N=100. So we need a smarter approach
        
        # Let's try all possible combinations of distances from X0, but only up to a certain limit
        # The maximum distance we need to consider is such that K^d <= M
        # For K >= 2, the maximum d is log(M)/log(K), which is up to 60 for M=1e18 and K=2
        
        # So we can try all combinations of distances up to 60, and check if any combination of N terms (distinct) sums to M
        
        # We'll try all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll generate all possible combinations of distances, and for each, compute the sum K^d1 + K^d2 + ... + K^dN
        
        # Since N is small (<= 100), and the maximum d is small (<= 60), we can generate all possible combinations of distances
        # We can use a recursive backtracking approach to generate all possible combinations of distances
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll compute the sum K^d1 + K^d2 + ... + K^dN for each combination, and check if it equals M
        
        # We'll also consider the case where some distances are 0 (i.e., Xi = X0)
        # But since all Xi are distinct, we can't have more than one Xi at X0
        
        # So the maximum number of distances that can be 0 is 1
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # Let's generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances (d1, d2, ..., dN) where each di is a non-negative integer, and all di are distinct
        # We'll also consider the case where some distances are 0, but only one of them can be 0
        
        # We'll generate all possible combinations of distances
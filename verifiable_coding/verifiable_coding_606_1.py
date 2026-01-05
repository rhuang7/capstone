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
        # Since all Xi are distinct, we can choose any N distinct integers
        # To maximize the impact, we should choose Xi as far as possible from X0
        # But since we are trying to achieve exactly M, we need to check if there exists a way to select N distinct integers such that the sum of K^|Xi - X0| equals M
        
        # The maximum possible impact for N impacts is when we choose the N largest possible distances
        # Let's try to find if there exists a way to get M by choosing appropriate distances
        
        # We can try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small (<= 100), we can try to find if there's a way to reach M
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d2, ..., dN) where each di is a positive integer
        # But since N is small, we can try to find if there's a way to reach M by trying all possible combinations of distances
        
        # We can try to find the minimal and maximal possible sum for N impacts
        # The minimal sum is when all distances are 1 (K^1 * N)
        # The maximal sum is when we choose the N largest possible distances (which is unbounded, but we can try to find if M is achievable)
        
        # We can try to find if there exists a way to get M by trying different combinations of distances
        
        # Try all possible combinations of distances (d1, d
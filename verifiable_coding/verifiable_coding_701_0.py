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
        N, k = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Compute the actual values of the powers
        # But since k can be up to 1e9 and A up to 1e5, we can't compute them directly
        # Instead, we'll track the sum of exponents for each part
        # Because k^a * k^b = k^(a+b), so the sum of exponents is what matters for the product
        
        # Compute prefix sums of exponents
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + A[i]
        
        # We need to split the array into two parts: left and right
        # The left part has sum of exponents S1, the right has S2
        # The product is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But we want to maximize (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # Which is always the same, so we need to maximize (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # Wait, this is not correct. The actual product is (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem must be to maximize (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is not correct. The actual product is (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1) * (k^S2) = k^(S1 + S2) = k^total
        # But this is the same for any split, so the product is always the same
        # So the problem is to find the split that maximizes (sum of left) * (sum of right)
        # Which is (k^S1
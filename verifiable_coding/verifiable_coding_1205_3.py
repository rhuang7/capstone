import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    idx = 1
    for _ in range(T):
        S = data[idx]
        idx += 1
        
        n = len(S)
        total = 0
        
        # Precompute the original string as a list for easy manipulation
        original = [c for c in S]
        
        # For each possible L and R, compute F(S, L, R)
        # But we need an efficient way to calculate the total
        # Let's think about the contribution of each pair (i, i+1)
        
        # Initialize the total with the original string's adjacent equal pairs
        original_equal = 0
        for i in range(n - 1):
            if original[i] == original[i + 1]:
                original_equal += 1
        
        # Now, for each possible L and R, we need to flip the bits in [L, R]
        # and count the number of equal adjacent pairs
        # But instead of simulating each flip, we can find the contribution of each flip
        
        # For each position i, how many times does flipping it affect the adjacent pairs?
        # Flipping a bit at position i affects the pairs (i-1, i) and (i, i+1)
        
        # We'll keep track of the number of flips for each position
        flip_count = [0] * (n + 2)  # 1-based indexing
        
        # For each possible L and R, we flip the bits in [L, R]
        # We can use a prefix sum approach to calculate the number of flips for each position
        
        # For each position i, the number of times it is flipped is equal to the number of intervals [L, R] that include i
        # The number of such intervals is (i) * (n - i + 1)
        # But we need to calculate the contribution of each flip to the equal pairs
        
        # For each position i, the number of times it is flipped is the number of intervals [L, R] that include i
        # So we can compute for each i the number of intervals that include it and then calculate the effect on the equal pairs
        
        # Let's compute the contribution of each flip to the equal pairs
        # For each position i, flipping it changes the pairs (i-1, i) and (i, i+1)
        
        # We'll calculate the contribution of each flip to the equal pairs
        # For each position i, we calculate how many times it is flipped and then compute the effect on the equal pairs
        
        # We can use a prefix sum approach to calculate the number of flips for each position
        # But since we need to consider all possible intervals [L, R], we can precompute the number of times each position is flipped
        
        # For each position i, the number of intervals [L, R] that include i is i * (n - i + 1)
        # But we need to calculate the contribution of each flip to the equal pairs
        
        # For each position i, the number of times it is flipped is the number of intervals [L, R] that include i
        # So we can precompute the number of flips for each position
        
        # We'll calculate the number of intervals [L, R] that include each position i
        # This is equal to i * (n - i + 1)
        
        # Now, for each position i, we can calculate the contribution of flipping it to the equal pairs
        # Flipping it affects the pairs (i-1, i) and (i, i+1)
        # So for each flip at position i, the contribution to the equal pairs is:
        # - If original[i-1] == original[i], then flipping i will change this pair
        # - If original[i] == original[i+1], then flipping i will change this pair
        
        # So for each position i, the contribution of flipping it once is:
        # - If original[i-1] == original[i], then it contributes -1 (if flipped)
        # - If original[i] == original[i+1], then it contributes -1 (if flipped)
        # So the total contribution is -2 if both pairs are equal, 0 if one is equal, and +2 if neither is equal
        
        # But since we are flipping it multiple times, we need to calculate the total contribution for all flips
        
        # We'll precompute the contribution of each flip for each position i
        # Then, multiply by the number of times it is flipped
        
        # Let's precompute the contribution of each flip for each position i
        # For each position i, we calculate the contribution of flipping it once
        # Then multiply by the number of times it is flipped
        
        # Precompute the contribution of each flip for each position i
        contribution = [0] * (n + 2)  # 1-based indexing
        
        for i in range(1, n + 1):
            # Contribution of flipping position i once
            c = 0
            if i > 1 and original[i - 1] == original[i]:
                c -= 1
            if i < n and original[i] == original[i + 1]:
                c -= 1
            contribution[i] = c
        
        # Now, for each position i, we calculate the number of times it is flipped
        # Which is the number of intervals [L, R] that include i
        # Which is i * (n - i + 1)
        
        # Now, calculate the total contribution
        total = original_equal
        for i in range(1, n + 1):
            count = i * (n - i + 1)
            total += contribution[i] * count
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
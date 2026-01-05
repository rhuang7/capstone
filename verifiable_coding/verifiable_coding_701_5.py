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
        
        # Compute the actual values of k^A_i
        # Since k can be up to 1e9 and A_i up to 1e5, we need to handle large exponents
        # But since we need to compute sums, we'll use logarithms to avoid overflow
        # However, for the purpose of this problem, we can compute the actual values
        # because the product of sums is maximized when the sums are as large as possible
        # So we can compute the actual values and sum them
        
        # Compute the actual values of k^A_i
        # Since k can be large and A_i can be large, we need to compute them carefully
        # We'll use Python's built-in pow with large exponents, but since Python handles big integers well, it's okay
        # However, for very large exponents, this might be slow. But given the constraints, it's manageable
        
        # Precompute the values
        values = [pow(k, a) for a in A]
        
        # Compute prefix sums
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + values[i]
        
        # Try all possible splits
        max_product = 0
        best_split = 0
        
        for i in range(1, N):
            left_sum = prefix[i]
            right_sum = prefix[N] - prefix[i]
            product = left_sum * right_sum
            if product > max_product or (product == max_product and i < best_split):
                max_product = product
                best_split = i
        
        results.append(str(best_split))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
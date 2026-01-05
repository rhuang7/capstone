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
        # Since k can be up to 1e9 and A up to 1e5, we need to handle large exponents
        # But since we're only interested in the sum of the left and right parts, we can compute them as follows:
        # For each element, compute k^A, but since k^A can be very large, we need to use logarithms to avoid overflow
        # However, since we're dealing with products of sums, we can use the logarithm of the product to avoid overflow
        # But since we need to find the maximum product, we can use the logarithm of the product to compare
        
        # Compute the total sum of all elements
        total_sum = 0
        for a in A:
            total_sum += k ** a
        
        # Compute prefix sums of the actual values
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i + 1] = prefix[i] + k ** A[i]
        
        # Find the best split
        max_product = 0
        best_pos = 0
        for i in range(1, N):
            left_sum = prefix[i]
            right_sum = total_sum - left_sum
            product = left_sum * right_sum
            if product > max_product or (product == max_product and i < best_pos):
                max_product = product
                best_pos = i
        
        results.append(str(best_pos))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
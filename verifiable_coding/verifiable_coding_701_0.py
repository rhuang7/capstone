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
        # Since k can be large and A_i can be large, we need to handle this carefully
        # We'll use logarithms to avoid overflow
        # But since we need to compute the sum of the left and right parts, we'll need to compute the actual values
        # However, for large k and A_i, this may not be feasible directly, so we'll use logarithms
        # We'll compute the sum of logs of the elements, then split the array into two parts and compute the product of the sums of the elements in each part
        
        # Compute the log of the product of all elements
        log_total = 0.0
        for a in A:
            log_total += a * (float(k) if k != 1 else 1.0)
        
        # Compute the prefix sums of logs
        prefix = [0.0] * (N + 1)
        for i in range(1, N + 1):
            a = A[i - 1]
            prefix[i] = prefix[i - 1] + a * (float(k) if k != 1 else 1.0)
        
        # Find the best split
        best = 0
        max_product = 0.0
        
        for i in range(1, N):
            left_sum = prefix[i]
            right_sum = log_total - left_sum
            product = left_sum * right_sum
            if product > max_product or (product == max_product and i < best):
                max_product = product
                best = i
        
        results.append(str(best))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
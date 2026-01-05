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
        # Since k can be up to 1e9 and A up to 1e5, we need to handle large numbers
        # However, directly computing k^A is not feasible for large A, so we use logarithms
        # To avoid overflow, we use log(k^A) = A * log(k)
        # But since we need to compare sums, we can't directly use logs
        # So we compute the actual values, but with care to avoid overflow
        # We use Python's arbitrary precision integers
        # However, for large k and A, this may be slow, but given the constraints, it's manageable
        
        # Precompute the actual values of k^A
        powers = []
        for a in A:
            power = 1
            for _ in range(a):
                power *= k
            powers.append(power)
        
        # Compute prefix sums
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + powers[i]
        
        # Find the best split
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
import sys
import math

MOD = 10**9 + 7

def first_digit(x):
    while x >= 10:
        x //= 10
    return x

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    F = list(map(int, data[idx:idx+N]))
    idx += N
    Q = int(data[idx])
    idx += 1
    
    # Precompute log values for fast product calculation
    logF = [0] * (N + 1)
    for i in range(1, N + 1):
        logF[i] = logF[i - 1] + math.log(F[i - 1])
    
    # Precompute powers of 10 for first digit calculation
    pow10 = [1] * (N + 1)
    for i in range(1, N + 1):
        pow10[i] = pow10[i - 1] * 10
    
    # Precompute factorial mod MOD for quick queries
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    # Precompute inverse factorial mod MOD
    inv_fact = [1] * (N + 1)
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # Precompute log values for each possible R
    # This is not feasible for N up to 1e5, so we need a different approach
    
    # Instead, for each query of type 2, we compute the product on the fly
    # But with N up to 1e5 and Q up to 1e5, this would be O(Q*N), which is too slow
    
    # So we need a way to precompute for all possible R
    # But with N up to 1e5, it's not feasible to precompute for all R
    
    # So we will process each query of type 2 on the fly
    
    # To handle updates, we need a way to quickly compute the product for a given R
    # We can use a segment tree or a binary indexed tree, but for this problem, we can't do that
    
    # So we will process each query of type 2 by iterating through the cities in the sequence
    # and multiplying the values
    
    # But with N up to 1e5 and Q up to 1e5, this would be O(Q*N), which is too slow
    
    # So we need a better approach
    
    # We can precompute for each R, the list of cities in the sequence
    # But with N up to 1e5, this would take O(N^2) space, which is not feasible
    
    # So we will process each query of type 2 on the fly, but with some optimizations
    
    # For each query of type 2, we compute the product of the cities in the sequence
    # and also compute the first digit
    
    # To compute the product, we can use logarithms to avoid overflow
    # But we also need to compute the exact product for the modulo part
    
    # So we will use two separate approaches:
    # 1. For the modulo part, we compute the product directly, using modular arithmetic
    # 2. For the first digit, we use logarithms to approximate the value
    
    # But for large numbers, this might not be accurate enough
    
    # So we will use the logarithm approach for the first digit, and the modular approach for the modulo
    
    # Now, let's process the queries
    
    for _ in range(Q):
        type_q = int(data[idx])
        idx += 1
        if type_q == 1:
            p = int(data[idx])
            idx += 1
            f = int(data[idx])
            idx += 1
            F[p - 1] = f
        else:
            R = int(data[idx])
            idx += 1
            # Compute the product of the cities in the sequence
            # The sequence is 1, 1+R, 1+2R, ..., 1+iR
            # So the cities are 1, 1+R, 1+2R, ..., 1 + kR where k is the largest integer such that 1 + kR <= N
            # So the cities are 1, 1+R, 1+2R, ..., 1 + (k)R where k = (N - 1) // R
            k = (N - 1) // R
            # The cities are 1, 1+R, 1+2R, ..., 1 + kR
            # So the indices are 0, R, 2R, ..., kR
            # So the product is F[0] * F[R] * F[2R] * ... * F[kR]
            # We can compute this product directly
            product = 1
            for i in range(k + 1):
                product *= F[i * R]
                product %= MOD
            # Compute the first digit
            # We can use logarithms to approximate the value
            # log(product) = sum(log(F[i * R]))
            # Then, product = 10^(log(product))
            # The first digit is 10^(log(product) - floor(log(product)))
            # But we need to be careful with precision
            # So we can compute the product using logarithms
            log_product = 0.0
            for i in range(k + 1):
                log_product += math.log(F[i * R])
            # Compute the first digit
            first_digit_val = 10 ** (log_product - math.floor(log_product))
            first_digit_val = int(first_digit_val)
            print(first_digit_val, product)
    
solve()
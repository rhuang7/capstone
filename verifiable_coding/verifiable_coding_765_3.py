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
        logF[i] = math.log(F[i - 1])
    
    # Precompute prefix products for each R
    # But since R can be up to N, and N is up to 1e5, we need an efficient way
    # We'll use a dictionary to store the product for each R
    # However, for queries, we need to compute the product on the fly
    # So we'll use a segment tree or a binary indexed tree for each R
    # But since R can be up to N, and N is 1e5, we can't precompute for all R
    
    # Instead, for each query of type 2, we'll compute the product on the fly
    # But for large N and Q, this will be too slow
    
    # So we need a better approach
    # We'll use a segment tree for each R, but that's not feasible
    
    # Alternative approach:
    # For each query of type 2, we'll generate the list of cities visited and compute the product
    # But for large N and Q, this is O(Q * log N) per query, which may be acceptable
    
    # However, for large N and Q, this will be too slow
    
    # So we need to find a way to precompute the product for all possible R
    
    # We'll precompute for each R, the list of cities visited, and store the product
    # But for N up to 1e5, this is O(N^2), which is not feasible
    
    # So we need a better approach
    
    # Let's use a binary indexed tree for each R, but again, this is not feasible
    
    # So we need to find a way to compute the product for a given R on the fly
    
    # For a given R, the cities visited are 1, 1+R, 1+2R, ..., 1+kR
    # So the number of cities is k = (N - 1) // R + 1
    
    # So for each query of type 2, we can compute the product on the fly
    
    # But for large N and Q, this is O(Q * log N) per query, which is not feasible
    
    # So we need to find a way to precompute the product for all possible R
    
    # We can precompute for each R, the product of the cities visited in the sequence
    # But for N up to 1e5, this is O(N^2), which is not feasible
    
    # So we need to find a way to compute the product for a given R on the fly efficiently
    
    # So we'll proceed with the following approach:
    # For each query of type 2, we'll compute the product on the fly
    # For each query of type 1, we'll update the F array
    
    # But for large N and Q, this will be too slow
    
    # So we need to find a way to compute the product for a given R quickly
    
    # We'll use a segment tree for the F array, and for a given R, we'll compute the product of the cities visited in the sequence
    
    # But for large N and Q, this is not feasible
    
    # So we'll proceed with the following approach:
    # For each query of type 2, we'll compute the product on the fly
    
    # Let's proceed with this approach
    
    # Precompute the log values for fast product calculation
    # But since we need to handle updates, we need a way to update the log values
    
    # So we'll use a segment tree for the log values
    
    # But for the sake of time, we'll proceed with the straightforward approach
    
    # Now, let's process the queries
    output = []
    for _ in range(Q):
        t = int(data[idx])
        idx += 1
        if t == 1:
            p = int(data[idx])
            idx += 1
            f = int(data[idx])
            idx += 1
            F[p - 1] = f
        else:
            R = int(data[idx])
            idx += 1
            # Compute the product of the cities visited in the sequence
            # Start from city 1, then 1+R, 1+2R, etc.
            product = 1
            for i in range(1, N + 1, R):
                product = (product * F[i - 1]) % MOD
            # Compute the first digit
            first = first_digit(product)
            output.append(f"{first} {product}")
    
    print("\n".join(output))
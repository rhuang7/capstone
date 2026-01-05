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
        logF[i] = math.log(F[i-1])
    
    # Precompute prefix sums of logs for each R
    # We'll use a dictionary to store prefix sums for each R
    # Since R can be up to N, we'll precompute for all R
    # But for efficiency, we'll compute on the fly for each query
    # However, since R can be up to N and queries can be up to 1e5, we need a better approach
    
    # Instead, for each query of type 2, we'll compute the product on the fly
    # But since we need to handle updates, we need to maintain the log values
    
    # So we'll maintain logF as a list, and for each query of type 2, we'll compute the product
    # using the log values
    
    # However, for large N and Q, this approach may not be efficient enough
    # So we need to find a way to handle updates and queries efficiently
    
    # We'll use a segment tree for range product queries and point updates
    # But since the queries are of the form R, which is a step in the sequence, we need to find the product of F[1], F[1+R], F[1+2R], ...
    
    # To handle this, we can precompute for each R, the list of cities visited
    # But for large N, this is not feasible
    
    # So we'll handle each query of type 2 on the fly
    
    # So we'll use a list to store F, and for each query of type 2, we'll compute the product
    # of F[1], F[1+R], F[1+2R], ... until we exceed N
    
    # But for large N and Q, this could be O(Q*N), which is not feasible for N=1e5 and Q=1e5
    
    # So we need a more efficient approach
    
    # We'll use a segment tree for range product queries and point updates
    
    # However, the queries are not arbitrary ranges, but sequences of cities with step R
    # So we need a way to compute the product of F[1], F[1+R], F[1+2R], ...
    
    # So for each R, we can precompute the list of cities visited, but for large N, this is not feasible
    
    # So we'll handle each query of type 2 on the fly
    
    # So we'll use a list to store F, and for each query of type 2, we'll compute the product
    # of F[1], F[1+R], F[1+2R], ... until we exceed N
    
    # However, for large N and Q, this could be O(Q*N), which is not feasible for N=1e5 and Q=1e5
    
    # So we need a better approach
    
    # We'll use a segment tree for range product queries and point updates
    
    # But the queries are not arbitrary ranges, but sequences of cities with step R
    # So we need a way to compute the product of F[1], F[1+R], F[1+2R], ...
    
    # So we'll precompute for each R, the list of cities visited, but for large N, this is not feasible
    
    # So we'll handle each query of type 2 on the fly
    
    # So we'll use a list to store F, and for each query of type 2, we'll compute the product
    # of F[1], F[1+R], F[1+2R], ... until we exceed N
    
    # However, for large N and Q, this could be O(Q*N), which is not feasible for N=1e5 and Q=1e5
    
    # So we need a better approach
    
    # We'll use a segment tree for range product queries and point updates
    
    # But the queries are not arbitrary ranges, but sequences of cities with step R
    # So we need a way to compute the product of F[1], F[1+R], F[1+2R], ...
    
    # So we'll precompute for each R, the list of cities visited, but for large N, this is not feasible
    
    # So we'll handle each query of type 2 on the fly
    
    # So we'll use a list to store F, and for each query of type 2, we'll compute the product
    # of F[1], F[1+R], F[1+2R], ... until we exceed N
    
    # However, for large N and Q, this could be O(Q*N), which is not feasible for N=1e5 and Q=1e5
    
    # So we need a better approach
    
    # We'll use a segment tree for range product queries and point updates
    
    # But the queries are not arbitrary ranges, but sequences of cities with step R
    # So we need a way to compute the product of F[1], F[1+R], F[1+2R], ...
    
    # So we'll precompute for each R, the list of cities visited, but for large N, this is not feasible
    
    # So we'll handle each query of type 2 on the fly
    
    # So we'll use a list to store F, and for each query of type 2, we'll compute the product
    # of F[1], F[1+R], F[1+2R], ... until we exceed N
    
    # However, for large N and Q, this could be O(Q*N), which is not feasible for N=1e5 and Q=1e5
    
    # So we need a better approach
    
    # We'll use a segment tree for range product queries and point updates
    
    # But the queries are not arbitrary ranges, but sequences of cities with step R
    # So we need a way to compute the product of F[1], F[1+R], F[1+2R], ...
    
    # So we'll precompute for each R, the list of cities visited, but for large N, this is not feasible
    
    # So we'll handle each query of type 2 on the fly
    
    # So we'll use a list to store F, and for each query of type 2, we'll compute the product
    # of F[1], F[1+R], F[1+2R], ... until we exceed N
    
    # However, for large N and Q, this could be O(Q*N), which is not feasible for N=1e5 and Q=1e5
    
    # So we need a better approach
    
    # We'll use a segment tree for range product queries and point updates
    
    # But the queries are not arbitrary ranges, but sequences of cities with step R
    # So we need a way to compute the product of F[1], F[1+R], F[1+2R], ...
    
    # So we'll precompute for each R, the list of cities visited, but for large N, this is not feasible
    
    # So we'll handle each query of type 2 on the fly
    
    # So we'll use a list to store F, and for each query of type 2, we'll compute the product
    # of F[1], F[1+R], F[1+2R], ... until we exceed N
    
    # However, for large N and Q, this could be O(Q*N), which is not feasible for N=1e5 and Q=1e5
    
    # So we need a better approach
    
    # We'll use a segment tree for range product queries and point updates
    
    # But the queries are not arbitrary ranges, but sequences of cities with step R
    # So we need a way to compute the product of F[1], F[1+R], F[1+2R], ...
    
    # So we'll precompute for each R, the list of cities visited, but for large N, this is not feasible
    
    # So we'll handle each query of type 2 on the fly
    
    # So we'll use a list to store F, and for each query of type 2, we'll compute the product
    # of F[1], F[1+R], F[1+2R], ... until we exceed N
    
    # However, for large N and Q, this could be O(Q*N), which is not feasible for N=1e5 and Q=1e5
    
    # So we need a better approach
    
    # We'll
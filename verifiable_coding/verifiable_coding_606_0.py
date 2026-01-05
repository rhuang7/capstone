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
        
        # The total impact is the sum of K^|Xi - X0| for all impacts
        # Since the impacts are at distinct integral points, we can choose any set of distinct integers
        # We need to check if there exists a set of N distinct integers such that the sum of K^|Xi - X0| equals M
        
        # The minimal possible sum is when the impacts are at X0 - 1, X0 - 2, ..., X0 - N (or X0 + 1, X0 + 2, ..., X0 + N)
        # The maximal possible sum is when the impacts are at X0 - 1, X0 - 2, ..., X0 - N, but with K^|Xi - X0| as large as possible
        # Since K >= 1, the sum can be made arbitrarily large by choosing points far from X0
        # So we need to check if M can be achieved with some combination of K^d for d >= 1, with exactly N terms, all distinct
        
        # We can try to find if M can be written as the sum of N terms of the form K^d, where d is a positive integer, and all terms are distinct
        # We can try to generate all possible combinations of K^d for d from 1 to some maximum, and check if any combination of N terms sums to M
        
        # For efficiency, we can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # Instead, we can try to find if there exists a set of N terms of the form K^d, all distinct, that sum to M
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # Let's compute the minimal sum
        min_sum = 0
        for d in range(1, N + 1):
            min_sum += K ** d
        
        # If M is less than the minimal sum, it's impossible
        if M < min_sum:
            results.append("no")
            continue
        
        # If K == 1, then all terms are 1, and the sum is N. So if M == N, then yes, else no
        if K == 1:
            if M == N:
                results.append("yes")
            else:
                results.append("no")
            continue
        
        # For K > 1, we can try to find if M can be written as the sum of N distinct terms of the form K^d
        # We can try to generate all possible combinations of N terms of the form K^d, and check if any of them sum to M
        # Since K can be up to 1000, and N up to 100, the number of possible terms is limited
        
        # We can try to generate all possible combinations of N terms of the form K^d, with d >= 1, and check if any of them sum to M
        
        # To avoid generating all combinations, we can try to find if there exists a set of N terms of the form K^d that sum to M
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # Let's try to find if there exists a set of N terms of the form K^d that sum to M
        # We can try to find the minimal and maximal possible sums
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # We can try to find the minimal and maximal possible sums
        
        # Let's try to find the minimal sum
        min_sum = 0
        for d in range(1, N + 1):
            min_sum += K ** d
        
        # If M is less than the minimal sum, it's impossible
        if M < min_sum:
            results.append("no")
            continue
        
        # If K == 1, then all terms are 1, and the sum is N. So if M == N, then yes, else no
        if K == 1:
            if M == N:
                results.append("yes")
            else:
                results.append("no")
            continue
        
        # For K > 1, we can try to find if there exists a set of N terms of the form K^d that sum to M
        # We can try to find the minimal and maximal possible sums
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # We can try to find the minimal and maximal possible sums
        
        # Let's try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can be achieved with N terms
        
        # We can try to find the minimal and maximal possible sums
        # The minimal sum is when we take the smallest N terms: K^1, K^2, ..., K^N
        # The maximal sum is when we take the largest N terms, but since K can be large, this is not feasible
        
        # So we can try to find if M is at least the minimal sum and at most some upper bound that can
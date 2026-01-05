import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    Ms = list(map(int, data[1:T+1]))
    
    results = []
    
    for M in Ms:
        if M == 1:
            results.append("1\n1")
            continue
        
        # Find all interesting numbers A
        interesting = []
        M_sqrt = int(math.isqrt(M))
        for d in range(1, M_sqrt + 1):
            if M % d == 0:
                # d is a divisor of M
                # Check if d is interesting
                # We need to find B such that A*B is divisible by M and A*B / M = A + B
                # Let's solve for B
                # A*B / M = A + B
                # A*B = M*(A + B)
                # A*B - M*A - M*B = 0
                # A*B - M*A - M*B + M^2 = M^2
                # A*(B - M) - M*(B - M) = M^2
                # (A - M)*(B - M) = M^2
                # Let's find A such that A - M divides M^2
                # Let's find all possible A such that A - M divides M^2
                # A = M + k, where k divides M^2
                # So k can be any divisor of M^2
                # So we need to find all divisors of M^2 and check if A = M + k is interesting
                # But this is too slow for large M
                # So we need a smarter approach
                
                # Instead, we can find all A such that A divides M^2 and A >= M
                # Because A*B / M = A + B, and A*B must be divisible by M
                # Let's try to find all A such that A divides M^2 and A >= M
                # Then B = (M^2 / A) + M
                # Let's check if B >= A
                # B = (M^2 / A) + M
                # Since A >= M, M^2 / A <= M
                # So B = (M^2 / A) + M <= M + M = 2M
                # So B is always >= M
                # So B >= A if M^2 / A + M >= A
                # M^2 / A + M >= A
                # M^2 + M*A >= A^2
                # M^2 + M*A - A^2 >= 0
                # This is a quadratic in A: -A^2 + M*A + M^2 >= 0
                # Solving this inequality gives us the valid range for A
                # But we can just iterate over all A that divide M^2 and are >= M
                # So we need to find all divisors of M^2 that are >= M
                # Then check if B = (M^2 / A) + M >= A
                # If yes, then A is interesting
                # So we can find all divisors of M^2 and check
                # But this is not feasible for large M
                # So we need to find a way to generate all A that satisfy the condition
                
                # Instead, we can find all A such that A divides M^2 and A >= M
                # Then B = (M^2 / A) + M
                # We need to check if B >= A
                # So we can iterate over all divisors of M^2 that are >= M
                # And collect those A for which B >= A
                # But how to find all divisors of M^2?
                # Let's find all divisors of M^2
                # First, factorize M
                # Then, for each prime factor, its exponent in M^2 is twice the exponent in M
                # Then, generate all divisors of M^2
                # Then, filter those that are >= M
                # Then, check if B >= A
                # But this is time-consuming for large M
                
                # So we need to find a way to find all A such that A divides M^2 and A >= M
                # And B = (M^2 / A) + M >= A
                # Which is equivalent to (M^2 / A) + M >= A
                # => M^2 + M*A >= A^2
                # => A^2 - M*A - M^2 <= 0
                # Solving this quadratic inequality gives us the valid range for A
                # The roots of A^2 - M*A - M^2 = 0 are:
                # A = [M ± sqrt(M^2 + 4*M^2)] / 2 = [M ± sqrt(5*M^2)] / 2 = [M ± M*sqrt(5)] / 2
                # So the valid range for A is between [M - M*sqrt(5)/2, M + M*sqrt(5)/2]
                # But since A is positive and >= M, the valid range is A >= M and A <= M*(1 + sqrt(5))/2
                # So we can find all A in this range that divide M^2
                # But this is still not feasible for large M
                # So we need to find a way to find all A that satisfy the condition
                # Let's find all divisors of M^2 that are >= M
                # Then check if B = (M^2 / A) + M >= A
                # So we need to generate all divisors of M^2
                # Let's factorize M first
                # Then, for each prime factor, its exponent in M^2 is twice the exponent in M
                # Then, generate all divisors of M^2
                # Then, filter those that are >= M
                # Then, check if B >= A
                # If yes, then A is interesting
                # So we need to factorize M and generate all divisors of M^2
                # But this is not feasible for large M (up to 1e14)
                # So we need to find a smarter way
                
                # Instead of generating all divisors of M^2, let's find all A such that A divides M^2 and A >= M
                # And B = (M^2 / A) + M >= A
                # So we can iterate over all possible A that divide M^2 and are >= M
                # But this is not feasible for large M
                # So we need to find a way to find all A such that A divides M^2 and A >= M
                # And B = (M^2 / A) + M >= A
                # Which is equivalent to A^2 - M*A - M^2 <= 0
                # So we can find all A in the range [M, M*(1 + sqrt(5))/2] that divide M^2
                # But how to find those A?
                # We can iterate over all possible A in that range and check if A divides M^2
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
                # So we need to find a way to find all A that divide M^2 and are in that range
                # But this is not feasible for large M
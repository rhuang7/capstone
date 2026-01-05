import sys
import math

MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    max_n = max(cases)
    
    # Precompute square roots up to sqrt(1e10)
    sqrt_max = int(math.isqrt(max_n)) + 1
    sqrt_cache = [0] * (sqrt_max + 1)
    for i in range(1, sqrt_max + 1):
        sqrt_cache[i] = int(math.isqrt(i))
    
    # Precompute Möbius function up to sqrt_max
    max_mob = sqrt_max
    mob = [1] * (max_mob + 1)
    is_prime = [True] * (max_mob + 1)
    for i in range(2, max_mob + 1):
        if is_prime[i]:
            for j in range(i, max_mob + 1, i):
                is_prime[j] = False
                mob[j] *= -1
            mob[i] = 0
    
    # Precompute number of divisors up to sqrt_max
    div_count = [0] * (max_mob + 1)
    for i in range(1, max_mob + 1):
        for j in range(i, max_mob + 1, i):
            div_count[j] += 1
    
    # Precompute answers for all N up to max_n
    answers = [0] * (max_n + 1)
    
    for n in range(1, max_n + 1):
        # Count number of rectangles with area <= n
        # This is equivalent to counting the number of pairs (a, b) such that a*b <= n
        # Which is the same as sum_{k=1 to sqrt(n)} (floor(n/k) - floor(n/(k+1)))
        # But we need to compute it efficiently using inclusion-exclusion
        # Using the precomputed divisors and Möbius function
        res = 0
        for k in range(1, int(math.isqrt(n)) + 1):
            cnt = 0
            for d in range(1, div_count[k] + 1):
                cnt += mob[d] * (n // (k * d) - n // ((k + 1) * d))
            res += cnt
        answers[n] = res % MOD
    
    for n in cases:
        print(answers[n])

if __name__ == '__main__':
    solve()
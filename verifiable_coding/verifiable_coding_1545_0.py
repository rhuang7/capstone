import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        # Compute S(n, m) mod 2
        # Using the recurrence relation mod 2
        # S(n, m) mod 2 = (m * S(n-1, m) + S(n-1, m-1)) mod 2
        # But for large n and m, we need an efficient way
        # The parity of S(n, m) is equal to the binomial coefficient C(n-1, m-1) mod 2
        # This is known as Lucas's theorem
        # So we compute C(n-1, m-1) mod 2
        # Using Lucas's theorem
        def comb_mod_2(n, k):
            # Compute C(n, k) mod 2 using Lucas's theorem
            # If k > n, return 0
            if k > n:
                return 0
            res = 1
            while n > 0 or k > 0:
                n_mod = n % 2
                k_mod = k % 2
                if k_mod > n_mod:
                    return 0
                res *= (n_mod - k_mod + 1) // (k_mod + 1)
                n //= 2
                k //= 2
            return res
        result = comb_mod_2(n-1, m-1)
        results.append(str(result))
    print('\n'.join(results))
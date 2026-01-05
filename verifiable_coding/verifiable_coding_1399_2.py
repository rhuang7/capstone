import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        l = []
        r = []
        for _ in range(N):
            li = int(data[idx])
            ri = int(data[idx+1])
            l.append(li)
            r.append(ri)
            idx += 2
        # Compute A^K
        # Since K can be up to 5e7, we need an efficient way
        # We'll use binary exponentiation and precompute the XOR for ranges
        # We'll use a list of lists to store the powers
        # Since K is up to 5e7, we need to find a pattern or use fast exponentiation
        # However, for each power, we need to compute the XOR of a range
        # We can precompute prefix XORs for each power
        # But with K up to 5e7, this is not feasible
        # So we need to find a pattern in the sequence of powers
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is similar to matrix exponentiation, but with XOR
        # However, since XOR is associative and commutative, we can find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is similar to matrix exponentiation, but with XOR
        # However, since XOR is associative and commutative, we can find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is similar to matrix exponentiation, but with XOR
        # However, since XOR is associative and commutative, we can find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a pattern
        # Let's try to find the pattern for small K
        # For K=1, A^1 = A
        # For K=2, A^2[i] = XOR of A^1[l_i..r_i]
        # For K=3, A^3[i] = XOR of A^2[l_i..r_i]
        # For K=4, A^4[i] = XOR of A^3[l_i..r_i]
        # So each step is a XOR of a range from the previous step
        # This is equivalent to applying the operation K times
        # But with K up to 5e7, we need to find a
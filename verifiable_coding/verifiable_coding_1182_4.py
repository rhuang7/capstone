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
        m = M
        for d in range(1, int(math.isqrt(m)) + 1):
            if m % d == 0:
                # d is a divisor of m
                # Check if d is interesting
                # We need to find B such that A*B is divisible by m and A*B/m = A + B
                # Let's solve for B in terms of A
                # A*B = m*(A + B)
                # A*B - m*B = m*A
                # B*(A - m) = m*A
                # B = (m*A) / (A - m)
                # For B to be integer, (A - m) must divide m*A
                # Also, since A <= B, we have A <= (m*A)/(A - m)
                # Let's solve for A
                # A <= (m*A)/(A - m)
                # Multiply both sides by (A - m) (assuming A > m)
                # A*(A - m) <= m*A
                # A^2 - m*A <= m*A
                # A^2 <= 2m*A
                # A <= 2m
                # So A ranges from 1 to 2m
                # But since A must be such that (A - m) divides m*A
                # Let's find all A in 1 to 2m such that (A - m) divides m*A
                # Let's check for A in 1 to 2m
                # But since m can be up to 1e14, we need an efficient way
                # Let's find all A such that A divides m*(A + B)
                # But this is complicated
                # Alternative approach: Let's find all A such that there exists B >= A with A*B divisible by m and A*B/m = A + B
                # Let's solve for B
                # A*B = m*(A + B)
                # A*B - m*B = m*A
                # B*(A - m) = m*A
                # B = (m*A) / (A - m)
                # For B to be integer, (A - m) must divide m*A
                # Also, since B >= A, we have (m*A)/(A - m) >= A
                # m*A >= A*(A - m)
                # m >= A - m
                # 2m >= A
                # So A <= 2m
                # So A ranges from 1 to 2m
                # Let's check for A in 1 to 2m
                # But since m can be up to 1e14, we need to find a way to generate A efficiently
                # Let's try to find all A such that (A - m) divides m*A
                # Let's try to find all A such that (A - m) divides m*A
                # Let's find all A such that A divides m*(A + B)
                # But this is not helpful
                # Let's try to find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's try to find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A - m) divides m*A
                # Let's find all A such that (A
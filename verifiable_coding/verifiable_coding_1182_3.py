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
        
        # Find all interesting numbers for M
        interesting = []
        # We need to find A such that there exists B >= A with A*B/M = A + B
        # Rearranging the equation: A*B = M*(A + B)
        # => A*B - M*A - M*B = 0
        # => A*B - M*A - M*B + M^2 = M^2
        # => (A - M)(B - M) = M^2
        # Let x = A - M, y = B - M => x*y = M^2
        # Since B >= A, then B - M >= A - M => y >= x
        # Also, since A is positive, x = A - M >= -M + 1
        # So x can be from -M + 1 to some upper bound
        # We need to find all x such that x divides M^2 and x <= y (y = M^2 / x)
        # Then A = x + M, B = y + M
        # But A must be positive, so x + M > 0 => x > -M
        # So x ranges from -M + 1 to M^2
        
        # Find all divisors of M^2
        def get_divisors(n):
            divisors = set()
            for i in range(1, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
            return divisors
        
        divisors = get_divisors(M * M)
        
        for d in divisors:
            x = d
            y = M * M // d
            if x <= y:
                A = x + M
                if A > 0:
                    interesting.append(A)
        
        # Sort the interesting numbers
        interesting.sort()
        
        # Output
        results.append(f"{len(interesting)}\n{'\n'.join(map(str, interesting))}")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
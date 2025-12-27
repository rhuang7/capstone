def check(candidate):
    assert candidate(10)==3.162277660168379
    assert candidate(2)==1.414213562373095
    assert candidate(9)==3.0


def babylonian_sqrt(n):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if n == 0:
        return 0.0
    guess = n / 2.0
    while True:
        next_guess = (guess + n / guess) / 2.0
        if abs(next_guess - guess) < 1e-10:
            return next_guess
        guess = next_guess

check(babylonian_sqrt)
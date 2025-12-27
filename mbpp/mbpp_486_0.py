def check(candidate):
    assert candidate(10, 5, 1.0/3) == 0.13656454808718185
    assert candidate(11, 6, 2.0/4) == 0.2255859375
    assert candidate(12, 7, 3.0/5) == 0.227030335488


def binomial_probability(n, k, p):
    from math import comb, pow
    
    # Calculate the binomial probability
    probability = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return probability

check(binomial_probability)
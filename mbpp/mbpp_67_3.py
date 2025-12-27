def check(candidate):
    assert candidate(2)==2
    assert candidate(10)==115975
    assert candidate(56)==6775685320645824322581483068371419745979053216268760300


def bell_number(n):
    """Compute the nth Bell number, which represents the number of ways to partition a set of n elements."""
    bell = [0] * (n + 1)
    bell[0] = 1  # Base case: one way to partition an empty set
    
    for i in range(1, n + 1):
        # Bell numbers can be computed using Stirling numbers of the second kind
        for j in range(i):
            bell[i] += bell[j]
    
    return bell[n]

check(bell_number)
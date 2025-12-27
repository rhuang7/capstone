def check(candidate):
    assert candidate(10) == 6
    assert candidate(2) == 1
    assert candidate(3) == 2


def newman_conway_sequence(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Initialize a list to store the sequence
    sequence = [0] * (n + 1)
    sequence[1] = 1
    for i in range(2, n + 1):
        sequence[i] = sequence[i - 1] + sequence[i - sequence[i - 1]]
    return sequence[n]

check(newman_conway_sequence)
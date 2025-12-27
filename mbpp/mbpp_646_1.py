def check(candidate):
    assert candidate(2,1) == 8
    assert candidate(5,2) == 64
    assert candidate(1,1) == 1


def count_cubes_in_cube(n, k):
    if k <= 0 or n < k:
        return 0
    return (n - k + 1) ** 3

check(count_cubes_in_cube)
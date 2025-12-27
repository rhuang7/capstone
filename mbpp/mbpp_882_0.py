def check(candidate):
    assert candidate(10,20)==400
    assert candidate(15,20)==600
    assert candidate(8,9)==144


def parallelogram_perimeter(base, side):
    return 2 * (base + side)

check(parallelogram_perimeter)
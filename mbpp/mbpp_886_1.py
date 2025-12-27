def check(candidate):
    assert candidate((8, 2, 3, 0, 7))==4.0
    assert candidate((-10,-20,-30))==-20.0
    assert candidate((19,15,18))==17.333333333333332


def calculate_mean(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

check(calculate_mean)
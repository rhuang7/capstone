def check(candidate):
    assert candidate(4,3) == 20
    assert candidate(1,2) == 2
    assert candidate(2,2) == 5


def count_squares_in_rectangle(width, height):
    count = 0
    for i in range(1, min(width, height) + 1):
        count += (width - i + 1) * (height - i + 1)
    return count

check(count_squares_in_rectangle)
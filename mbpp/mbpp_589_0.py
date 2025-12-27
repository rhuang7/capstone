def check(candidate):
    assert candidate(1,30)==[1, 4, 9, 16, 25]
    assert candidate(50,100)==[64, 81, 100]
    assert candidate(100,200)==[100, 121, 144, 169, 196]


def find_perfect_squares(start, end):
    squares = []
    n = 1
    while n * n <= end:
        square = n * n
        if start <= square <= end:
            squares.append(square)
        n += 1
    return squares

check(find_perfect_squares)
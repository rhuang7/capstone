def check(candidate):
    assert candidate("there are 70 flats in this apartment")==10
    assert candidate("every adult have 32 teeth")==17
    assert candidate("isha has 79 chocolates in her bag")==9


def separate_numbers_positions(s):
    result = []
    for index, char in enumerate(s):
        if char.isdigit():
            result.append((index, char))
    return result

check(separate_numbers_positions)
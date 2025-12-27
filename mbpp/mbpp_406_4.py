def check(candidate):
    assert candidate(12) == "Even Parity"
    assert candidate(7) == "Odd Parity"
    assert candidate(10) == "Even Parity"


def find_parity(number):
    return "even" if number % 2 == 0 else "odd"

check(find_parity)
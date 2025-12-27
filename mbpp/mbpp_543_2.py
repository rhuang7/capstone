def check(candidate):
    assert candidate(9875,10)==(4)
    assert candidate(98759853034,100)==(11)
    assert candidate(1234567,500)==(7)


def add_and_count_digits(a, b):
    total = a + b
    print(len(str(total)))

check(add_and_count_digits)
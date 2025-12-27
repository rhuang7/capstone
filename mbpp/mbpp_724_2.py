def check(candidate):
    assert candidate(2,100)==115
    assert candidate(8,10)==37
    assert candidate(8,15)==62


def sum_of_digits_of_base_power(base, power):
    number = base ** power
    return sum(int(digit) for digit in str(number))

check(sum_of_digits_of_base_power)
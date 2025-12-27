def check(candidate):
    assert candidate (12345) == False
    assert candidate(1212112) == True
    assert candidate(1212) == False


def difference_even_odd_digits(number):
    even_sum = 0
    odd_sum = 0
    for digit in str(abs(number)):
        digit_int = int(digit)
        if digit_int % 2 == 0:
            even_sum += digit_int
        else:
            odd_sum += digit_int
    return even_sum - odd_sum

check(difference_even_odd_digits)
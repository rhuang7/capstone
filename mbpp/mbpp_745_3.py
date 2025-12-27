def check(candidate):
    assert candidate(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert candidate(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert candidate(20,25)==[22, 24]


def find_divisible_numbers(start, end):
    def is_valid(n):
        digits = set(str(n))
        for d in digits:
            if d == '0':
                return False
            if n % int(d) != 0:
                return False
        return True

    result = []
    for num in range(start, end + 1):
        if is_valid(num):
            result.append(num)
    return result

check(find_divisible_numbers)
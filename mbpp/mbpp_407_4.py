def check(candidate):
    assert candidate(12)==21
    assert candidate(10)==False
    assert candidate(102)==120


def next_bigger(n):
    digits = list(str(n))
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return -1
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    return int(''.join(digits))

check(next_bigger)